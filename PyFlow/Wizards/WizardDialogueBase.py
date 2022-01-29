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


from Qt import QtCore
from Qt import QtGui
from Qt.QtWidgets import *
from docutils import core


def rst2html(rst):
    if rst is not None:
        return core.publish_string(rst, writer_name="html").decode("utf-8")
    return ""


class WizardDialogueBase(QDialog):
    """docstring for WizardDialogueBase."""
    def __init__(self, parent=None):
        super(WizardDialogueBase, self).__init__(parent)
        self.setWindowTitle("Package wizard")
        self.setWindowIcon(QtGui.QIcon(":LogoBpApp.png"))
        self.resize(700, 500)
        self.mainLayout = QVBoxLayout(self)
        self.mainLayout.setObjectName("mainLayout")
        self.mainLayout.setSpacing(1)
        self.mainLayout.setContentsMargins(1, 1, 1, 1)
        self.progress = QProgressBar()
        self.progress.setTextVisible(False)
        self.progress.setObjectName("progress")
        self.progress.setRange(0, 100)
        self.mainLayout.addWidget(self.progress)
        self.stackWidget = QStackedWidget()
        self.stackWidget.currentChanged.connect(self.updateMessage)

        # message section
        self.messageLayout = QHBoxLayout()
        self.messageWidget = QLabel()
        self.messageWidget.setTextFormat(QtCore.Qt.RichText)
        self.messageWidget.setWordWrap(True)
        self.messageWidget.setAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont("Consolas", 20)
        self.messageWidget.setFont(font)
        wizardImage = QLabel("test")
        wizardImage.setPixmap(QtGui.QPixmap(":wizard-cat.png").scaled(250, 250))
        wizardImage.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        self.messageLayout.addWidget(wizardImage)
        self.messageLayout.addWidget(self.messageWidget)
        self.mainLayout.addLayout(self.messageLayout)

        # add user input section
        # ...
        self.messages = {}
        self.pageValidationHooks = {}
        self.errorMessages = {}
        self.pageEnterCallbacks = {}
        self.addGreetPage()
        self.populate()
        self.addFinalPage()

        self.mainLayout.addWidget(self.stackWidget)

        # add navigation buttons
        # ...
        self.navigationLayout = QHBoxLayout()
        self.navigationLayout.setObjectName("navigationLayout")
        self.navigationLayout.setContentsMargins(5, 1, 5, 5)
        self.goBackButton = QPushButton("Go back")
        self.goBackButton.clicked.connect(self.onGoBack)
        self.goForwardButton = QPushButton("Go forward")
        self.goForwardButton.clicked.connect(self.onGoForward)
        self.navigationLayout.addWidget(self.goBackButton)
        spacerItem = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Maximum)
        self.navigationLayout.addItem(spacerItem)
        self.navigationLayout.addWidget(self.goForwardButton)
        self.mainLayout.addLayout(self.navigationLayout)

        self.updateNavigationVisibility()
        self.updateMessage(0)

    def updateMessage(self, pageNum):
        widget = self.stackWidget.widget(pageNum)
        if widget in self.messages:
            self.setMessageRst(self.messages[widget])
            return
        if pageNum == 0:
            return
        if pageNum == self.stackWidget.count() - 1:
            return

    def addGreetPage(self):
        self.addPageWidget(QWidget(), "**Hello buddy!** lets create some new stuff!")

    def addFinalPage(self):
        self.addPageWidget(QWidget(), "Have fun!")

    def updateProgress(self):
        numStates = self.stackWidget.count() - 1
        chunk = 100 / numStates
        self.progress.setValue(chunk * self.stackWidget.currentIndex())

    def updateNavigationVisibility(self):
        self.goBackButton.show()
        self.goForwardButton.show()
        self.goForwardButton.setText("Go forward")
        if self.stackWidget.currentIndex() == 0:
            self.goBackButton.hide()
        if self.stackWidget.currentIndex() == self.stackWidget.count() - 1:
            self.goForwardButton.setText("Done")
        self.updateProgress()

    def onGoBack(self):
        futureIndex = self.stackWidget.currentIndex() - 1
        self.stackWidget.setCurrentIndex(futureIndex)
        self.setMessageRst(self.messages[self.stackWidget.currentWidget()])
        self.updateNavigationVisibility()

    def onDone(self):
        self.accept()

    def onGoForward(self):
        futureIndex = self.stackWidget.currentIndex() + 1
        isCurrentPageValid = self.pageValidationHooks[self.stackWidget.currentWidget()]()
        if isCurrentPageValid:
            self.stackWidget.setCurrentIndex(futureIndex)
            self.updateNavigationVisibility()
            self.pageValidationHooks[self.stackWidget.currentWidget()]()
            self.pageEnterCallbacks[self.stackWidget.currentWidget()]()
            if futureIndex == self.stackWidget.count():
                self.onDone()
        else:
            self.setMessageRst(self.errorMessages[self.stackWidget.currentWidget()])

    def addPageWidget(self, widget, messageRst, errorMessageRst="Somethig is wrong!", validationHook=lambda: True, pageEnterCallback=lambda: None):
        self.stackWidget.addWidget(widget)
        self.messages[widget] = messageRst
        self.pageValidationHooks[widget] = validationHook
        self.errorMessages[widget] = errorMessageRst
        self.pageEnterCallbacks[widget] = pageEnterCallback

    def populate(self):
        pass

    def setMessageRst(self, rst):
        self.messageWidget.setText(rst2html(rst))

    @staticmethod
    def run():
        instance = WizardDialogueBase()
        instance.exec_()


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)

    w = WizardDialogueBase()
    w.show()

    sys.exit(app.exec_())
