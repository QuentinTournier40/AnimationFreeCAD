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


class commentNode(NodeBase):
    def __init__(self, name):
        super(commentNode, self).__init__(name)

    @staticmethod
    def category():
        return 'UI'

    @staticmethod
    def keywords():
        return []

    @staticmethod
    def description():
        return 'Can drag intersected nodes. You can also specify color and resize it.'
