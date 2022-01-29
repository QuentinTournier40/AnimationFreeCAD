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


class deltaTime(NodeBase):
    def __init__(self, name):
        super(deltaTime, self).__init__(name)
        self.bCachedEnabled = False
        self._deltaTime = 0.0
        self._out0 = self.createOutputPin('out0', 'FloatPin')

    @staticmethod
    def pinTypeHints():
        helper = NodePinsSuggestionsHelper()
        helper.addOutputDataType('FloatPin')
        helper.addOutputStruct(StructureType.Single)
        return helper

    @staticmethod
    def category():
        return 'Utils'

    @staticmethod
    def keywords():
        return []

    @staticmethod
    def description():
        return 'Editor delta time.'

    def Tick(self, deltaTime):
        self._deltaTime = deltaTime

    def compute(self, *args, **kwargs):
        self._out0.setData(self._deltaTime)
        push(self._out0)
