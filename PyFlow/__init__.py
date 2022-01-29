## Copyright 2015-2019 Ilgar Lunin, Pedro Cabrera

## Licensed under the Apache License, Version 2.0 (the "License");
## you may not use this file except in compliance with the License.
## You may obtain a copy of the License at

##     http://www.apache.org/licenses/LICENSE-2.0

## Unless required by applicable law or agreed to in writing, software
## distributed under the License is distributed on an "AS IS" BASIS,
## WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
## See the License for the specific language governing permissions and
## limitations under the License.


"""Common utils working with packags.
"""

# this line adds extension-packages not installed inside the PyFlow directory
__path__ = __import__('pkgutil').extend_path(__path__, __name__)

import importlib
import pkgutil
import collections
from copy import copy
import os
import json

from PyFlow.Packages import *


__all__ = [
    "INITIALIZE",
    "GET_PACKAGES",
    "GET_PACKAGE_CHECKED",
    "CreateRawPin",
    "getPinDefaultValueByType",
    "findPinClassByType",
    "getRawNodeInstance",
    "getAllPinClasses",
    "getHashableDataTypes",
]


__PACKAGES = {}
__PACKAGE_PATHS = {}
__HASHABLE_TYPES = []


def GET_PACKAGES():
    return __PACKAGES


def GET_PACKAGE_PATH(packageName):
    if packageName in __PACKAGE_PATHS:
        return __PACKAGE_PATHS[packageName]


def GET_PACKAGE_CHECKED(package_name):
    assert package_name in __PACKAGES
    return __PACKAGES[package_name]


def getAllPinClasses():
    result = []
    for package in list(__PACKAGES.values()):
        result += list(package.GetPinClasses().values())
    return result


def findPinClassByType(dataType):
    for package_name, package in GET_PACKAGES().items():
        pins = package.GetPinClasses()
        if dataType in pins:
            return pins[dataType]
    return None


def getPinDefaultValueByType(dataType):
    pin = findPinClassByType(dataType)
    if pin:
        return pin.pinDataTypeHint()[1]
    return None


def getHashableDataTypes():
    if len(__HASHABLE_TYPES) == 0:
        for pin in getAllPinClasses():
            t = pin.internalDataStructure()
            if t is not type(None) and t is not None:
                if isinstance(pin.internalDataStructure()(), collections.Hashable):
                    __HASHABLE_TYPES.append(pin.__name__)
    return copy(__HASHABLE_TYPES)


def getPinFromData(data):
    for pin in [pin for pin in getAllPinClasses() if pin.IsValuePin()]:
        pType = pin.internalDataStructure()
        if data == pType:
            return pin


def CreateRawPin(name, owningNode, dataType, direction, **kwds):
    pinClass = findPinClassByType(dataType)
    if pinClass is None:
        return None
    inst = pinClass(name, owningNode, direction, **kwds)
    return inst


def getRawNodeInstance(nodeClassName, packageName=None, libName=None, **kwargs):
    from PyFlow.Core.NodeBase import NodeBase
    package = GET_PACKAGE_CHECKED(packageName)
    # try find function first
    if libName is not None:
        for key, lib in package.GetFunctionLibraries().items():
            foos = lib.getFunctions()
            if libName == key and nodeClassName in foos:
                return NodeBase.initializeFromFunction(foos[nodeClassName])

    # try find node class
    nodes = package.GetNodeClasses()
    if nodeClassName in nodes:
        return nodes[nodeClassName](nodeClassName, **kwargs)

    # try find exported py nodes
    packagePath = GET_PACKAGE_PATH(packageName)
    pyNodesPath = os.path.join(packagePath, "PyNodes")
    if os.path.exists(pyNodesPath):
        for path, dirs, files in os.walk(pyNodesPath):
            for pyNodeFileName in files:
                pyNodeName, _ = os.path.splitext(pyNodeFileName)
                if nodeClassName == pyNodeName:
                    pythonNode = getRawNodeInstance("pythonNode", "PyFlowBase")
                    pyNodeFullPath = os.path.join(path, pyNodeFileName)
                    with open(pyNodeFullPath, "r") as f:
                        pythonNode._nodeData = f.read()
                    return pythonNode

    # try find exported compound nodes
    compoundNodesPath = os.path.join(packagePath, "Compounds")
    if os.path.exists(compoundNodesPath):
        for path, dirs, files in os.walk(compoundNodesPath):
            for compoundNodeFileName in files:
                compoundNodeName, _ = os.path.splitext(compoundNodeFileName)
                compoundNodeFullPath = os.path.join(path, compoundNodeFileName)
                with open(compoundNodeFullPath, 'r') as f:
                    compoundData = json.load(f)
                    if compoundData["name"] == nodeClassName:
                        compoundNode = getRawNodeInstance("compound", "PyFlowBase")
                        compoundNodeFullPath = os.path.join(path, compoundNodeFileName)
                        with open(compoundNodeFullPath, "r") as f:
                            jsonString = f.read()
                            compoundNode._rawGraphJson = json.loads(jsonString)
                        return compoundNode


def INITIALIZE(additionalPackageLocations=[], software=""):
    from PyFlow.UI.Tool import REGISTER_TOOL
    from PyFlow.UI.Widgets.InputWidgets import REGISTER_UI_INPUT_WIDGET_PIN_FACTORY
    from PyFlow.UI.Canvas.UINodeBase import REGISTER_UI_NODE_FACTORY
    from PyFlow.UI.Canvas.UIPinBase import REGISTER_UI_PIN_FACTORY
    from PyFlow import ConfigManager
    from Qt.QtWidgets import QMessageBox

    packagePaths = Packages.__path__

    def ensurePackagePath(inPath):
        for subFolder in os.listdir(inPath):
            subFolderPath = os.path.join(inPath, subFolder)
            if os.path.isdir(subFolderPath):
                if "PyFlow" in os.listdir(subFolderPath):
                    subFolderPath = os.path.join(subFolderPath, "PyFlow", "Packages")
                    if os.path.exists(subFolderPath):
                        return subFolderPath
        return inPath

    def recursePackagePaths(inPath):
        paths = []
        for subFolder in os.listdir(inPath):
            subFolderPath = os.path.join(inPath, subFolder)
            if os.path.isdir(subFolderPath):
                if "PyFlow" in os.listdir(subFolderPath):
                    subFolderPath = os.path.join(subFolderPath, "PyFlow", "Packages")
                    if os.path.exists(subFolderPath):
                        paths.append(subFolderPath)
        return paths

    # check for additional package locations
    if "PYFLOW_PACKAGES_PATHS" in os.environ:
        delim = ';'
        pathsString = os.environ["PYFLOW_PACKAGES_PATHS"]
        # remove delimeters from right
        pathsString = pathsString.rstrip(delim)
        for packagesRoot in pathsString.split(delim):
            if os.path.exists(packagesRoot):
                paths = recursePackagePaths(packagesRoot)
                packagePaths.extend(paths)

    for packagePathId in range(len(additionalPackageLocations)):
        packagePath = additionalPackageLocations[packagePathId]
        packagePath = ensurePackagePath(packagePath)
        additionalPackageLocations[packagePathId] = packagePath

    packagePaths.extend(additionalPackageLocations)

    for importer, modname, ispkg in pkgutil.iter_modules(packagePaths):
        try:
            if ispkg:
                mod = importer.find_module(modname).load_module(modname)
                package = getattr(mod, modname)()
                __PACKAGES[modname] = package
                __PACKAGE_PATHS[modname] = os.path.normpath(mod.__path__[0])
        except Exception as e:
            QMessageBox.critical(None, str("Fatal error"), "Error On Module %s :\n%s" % (modname, str(e)))
            continue

    registeredInternalPinDataTypes = set()

    for name, package in __PACKAGES.items():
        packageName = package.__class__.__name__
        for node in package.GetNodeClasses().values():
            node._packageName = packageName

        for pin in package.GetPinClasses().values():
            pin._packageName = packageName
            if pin.IsValuePin():
                internalType = pin.internalDataStructure()
                if internalType in registeredInternalPinDataTypes:
                    raise Exception("Pin with {0} internal data type already been registered".format(internalType))
                registeredInternalPinDataTypes.add(internalType)

        uiPinsFactory = package.UIPinsFactory()
        if uiPinsFactory is not None:
            REGISTER_UI_PIN_FACTORY(packageName, uiPinsFactory)

        uiPinInputWidgetsFactory = package.PinsInputWidgetFactory()
        if uiPinInputWidgetsFactory is not None:
            REGISTER_UI_INPUT_WIDGET_PIN_FACTORY(packageName, uiPinInputWidgetsFactory)

        uiNodesFactory = package.UINodesFactory()
        if uiNodesFactory is not None:
            REGISTER_UI_NODE_FACTORY(packageName, uiNodesFactory)

        for toolClass in package.GetToolClasses().values():
            supportedSoftwares = toolClass.supportedSoftwares()
            if "any" not in supportedSoftwares:
                if software not in supportedSoftwares:
                    continue
            REGISTER_TOOL(packageName, toolClass)
    getHashableDataTypes()
