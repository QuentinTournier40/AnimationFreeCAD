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


from PyFlow import getHashableDataTypes
from PyFlow.Core import NodeBase
from PyFlow.Core.NodeBase import NodePinsSuggestionsHelper
from PyFlow.Core.Common import *


class makeAnyDict(NodeBase):
    def __init__(self, name):
        super(makeAnyDict, self).__init__(name)
        self.KeyType = self.createInputPin('KeyType', 'AnyPin', defaultValue=str(""), constraint="1", supportedPinDataTypes=getHashableDataTypes())
        self.KeyType.hidden = True

        self.arrayData = self.createInputPin('data', 'AnyPin', structure=StructureType.Dict)
        self.arrayData.enableOptions(PinOptions.AllowMultipleConnections | PinOptions.AllowAny | PinOptions.DictElementSupported)
        self.arrayData.disableOptions(PinOptions.ChangeTypeOnConnection | PinOptions.SupportsOnlyArrays)
        self.outArray = self.createOutputPin('out', 'AnyPin', structure=StructureType.Dict)
        self.outArray.enableOptions(PinOptions.AllowAny)
        self.outArray.disableOptions(PinOptions.ChangeTypeOnConnection)
        self.result = self.createOutputPin('result', 'BoolPin')
        self.arrayData.onPinDisconnected.connect(self.inPinDisconnected)
        self.arrayData.onPinConnected.connect(self.inPinConnected)
        self.KeyType.typeChanged.connect(self.updateDicts)

    @staticmethod
    def pinTypeHints():
        helper = NodePinsSuggestionsHelper()
        helper.addInputDataType('AnyPin')
        helper.addOutputDataType('AnyPin')
        helper.addOutputDataType('BoolPin')
        helper.addInputStruct(StructureType.Dict)
        helper.addOutputStruct(StructureType.Dict)
        helper.addOutputStruct(StructureType.Single)
        return helper

    @staticmethod
    def category():
        return 'GenericTypes'

    @staticmethod
    def keywords():
        return []

    @staticmethod
    def description():
        return 'Creates a list from connected pins'

    def updateDicts(self,dataType):
        self.arrayData.updateConnectedDicts([],self.KeyType.dataType)

    def inPinConnected(self,inputpin):
        inp = inputpin.getDictElementNode([])
        if inp and inputpin.owningNode() != inp:
            dataType = self.KeyType.dataType
            if not inp.key.checkFree([]):
                dataType = inp.key.dataType
            if self.KeyType not in inp.constraints[inp.key.constraint]:
                inp.constraints[inp.key.constraint].append(self.KeyType)
            if inp.key not in self.constraints[inp.key.constraint]:    
                self.constraints[inp.key.constraint].append(inp.key)
            for i in self.constraints[inp.key.constraint]:
                i.setType(dataType)  


    def inPinDisconnected(self,inp):
        inp = inp.getDictElementNode([])
        elements = [i.getDictElementNode([]) for i in self.arrayData.affected_by]
        if inp is not None :
            if self.KeyType in inp.constraints[inp.key.constraint]:
                inp.constraints[inp.key.constraint].remove(self.KeyType)
            if inp.key in self.constraints[inp.key.constraint]:    
                self.constraints[inp.key.constraint].remove(inp.key)

    def compute(self, *args, **kwargs):
        outArray = PFDict(self.KeyType.dataType)
        ySortedPins = sorted(self.arrayData.affected_by, key=lambda pin: pin.owningNode().y)

        for i in ySortedPins:
            if isinstance(i.getData(), DictElement):
                outArray[i.getData()[0]] = i.getData()[1]
            elif isinstance(i.getData(), PFDict):
                for key,value in i.getData().items():
                    outArray[key] = value

        self.outArray.setData(outArray)
        self.arrayData.setData(outArray)
        self.result.setData(True)

