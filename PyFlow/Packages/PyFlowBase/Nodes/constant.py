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


from PyFlow.Core import NodeBase
from PyFlow.Core.NodeBase import NodePinsSuggestionsHelper
from PyFlow.Core.Common import *
from PyFlow import findPinClassByType, getAllPinClasses
from PyFlow import CreateRawPin
from copy import copy

class constant(NodeBase):
    def __init__(self, name):
        super(constant, self).__init__(name)
        self.input = self.createInputPin("in", 'AnyPin', defaultValue=0.0, structure=StructureType.Multi, constraint="1", structConstraint="1")
        self.output = self.createOutputPin("out", 'AnyPin', defaultValue=0.0, structure=StructureType.Multi, constraint="1", structConstraint="1")
        self.input.disableOptions(PinOptions.ChangeTypeOnConnection)
        self.output.disableOptions(PinOptions.ChangeTypeOnConnection)
        pinAffects(self.input, self.output)
        self.input.call = self.output.call
        self.pinTypes = []
        for pinClass in getAllPinClasses():
            if pinClass.IsValuePin() and pinClass.__name__ != "AnyPin":
                self.pinTypes.append(pinClass.__name__)
        self.bCacheEnabled = False

    @staticmethod
    def pinTypeHints():
        helper = NodePinsSuggestionsHelper()
        helper.addInputDataType('AnyPin')
        helper.addOutputDataType('AnyPin')
        helper.addInputStruct(StructureType.Multi)
        helper.addOutputStruct(StructureType.Multi)
        return helper

    @staticmethod
    def category():
        return 'GenericTypes'
        
    @staticmethod
    def keywords():
        return ["Make"]


    def serialize(self):      
        orig = super(constant, self).serialize()
        orig["currDataType"] = self.input.dataType
        return orig

    def postCreate(self, jsonTemplate=None):
        super(constant, self).postCreate(jsonTemplate)
        if "currDataType" in jsonTemplate:
            self.updateType(self.pinTypes.index(jsonTemplate["currDataType"]))

    def onPinConected(self,other):
        self.changeType(other.dataType)

    def overrideTypeChanged(self,toogle):
        if bool(toogle):
            self.input.enableOptions(PinOptions.ChangeTypeOnConnection)
            self.output.enableOptions(PinOptions.ChangeTypeOnConnection)
        else:
            self.input.disableOptions(PinOptions.ChangeTypeOnConnection)
            self.output.disableOptions(PinOptions.ChangeTypeOnConnection)            

    def updateType(self,dataTypeIndex):
        self.input.enableOptions(PinOptions.ChangeTypeOnConnection)
        self.output.enableOptions(PinOptions.ChangeTypeOnConnection)        
        self.changeType(self.pinTypes[dataTypeIndex],True)
        self.input.disableOptions(PinOptions.ChangeTypeOnConnection)
        self.output.disableOptions(PinOptions.ChangeTypeOnConnection)  
     
    def changeType(self,dataType,init=False):
        a = self.input.initType(dataType,init)
        b = self.output.initType(dataType,init)

    def selectStructure(self,name):
        self.input.changeStructure(StructureType(name),True)
        self.output.changeStructure(StructureType(name),True)


    def compute(self, *args, **kwargs):
        self.output.setData(self.input.getData())
