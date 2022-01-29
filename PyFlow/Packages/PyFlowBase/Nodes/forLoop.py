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
from PyFlow.Packages.PyFlowBase.Nodes import FLOW_CONTROL_COLOR


class forLoop(NodeBase):
    def __init__(self, name):
        super(forLoop, self).__init__(name)
        self.inExec = self.createInputPin('inExec', 'ExecPin', None, self.compute)
        self.firstIndex = self.createInputPin('Start', 'IntPin')
        self.lastIndex = self.createInputPin('Stop', 'IntPin')
        self.step = self.createInputPin('Step', 'IntPin')
        self.step.setData(1)

        self.loopBody = self.createOutputPin('LoopBody', 'ExecPin')
        self.index = self.createOutputPin('Index', 'IntPin')
        self.completed = self.createOutputPin('Completed', 'ExecPin')
        self.headerColor = FLOW_CONTROL_COLOR

    @staticmethod
    def pinTypeHints():
        helper = NodePinsSuggestionsHelper()
        helper.addInputDataType('ExecPin')
        helper.addInputDataType('IntPin')
        helper.addOutputDataType('ExecPin')
        helper.addOutputDataType('IntPin')
        helper.addInputStruct(StructureType.Single)
        helper.addOutputStruct(StructureType.Single)
        return helper

    @staticmethod
    def category():
        return 'FlowControl'

    @staticmethod
    def keywords():
        return ['iter']

    @staticmethod
    def description():
        return 'For loop'

    def compute(self, *args, **kwargs):
        indexFrom = self.firstIndex.getData()
        indexTo = self.lastIndex.getData()
        step = self.step.getData()
        if step == 0:
            self.completed.call(*args, **kwargs)
        else:
            for i in range(indexFrom, indexTo, step):
                self.index.setData(i)
                push(self.index)
                self.loopBody.call(*args, **kwargs)
            self.completed.call(*args, **kwargs)
