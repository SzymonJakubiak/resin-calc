from PyQt5.QtWidgets import QLineEdit, QLabel, QGridLayout
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QObjectCleanupHandler

class InputBoxes():
    """Class configuring input region for GUI"""
    def __init__(self):
        """InputBoxes constructor"""
        # General layout for input area
        self.inputGeneralLayout = QGridLayout()

        # Creating lists with QWidgets for input area
        self.inputQLineEdits = []
        self.inputQLabelList = []

        # Building input region with default widgets number
        self.buildInputRegion()

    def buildInputRegion(self, numberOfComponents=2):
        """Builds inputRegion for a given number of Mixture's components"""
        # Remove previous widgets from the inputRegion
        for lineEdit, label in zip(self.inputQLineEdits, self.inputQLabelList):
            # QObjectCleanupHandler destroys widgets after getting out of this scope
            QObjectCleanupHandler().add(lineEdit)
            QObjectCleanupHandler().add(label)
        # Empty the lists
        self.inputQLineEdits = []
        self.inputQLabelList = []

        # Creating QLineEdit and QLabel for every input box,  =numberOfComponents + 1
        for componentIndex in range(numberOfComponents+1):
            # +1, TotalMass's window included
            self.inputQLineEdits.append(QLineEdit())
            self.inputQLabelList.append(QLabel())

        # Setting text for input labels
        self.inputQLabelList[0].setText('TotalMass') # First label
        for number, qLabel in enumerate(self.inputQLabelList[1:], start=1): # Other labels
            qLabel.setText('Component{}Mass'.format(number))

        # Setting text allignment for every line edit
        for qLineEdit in self.inputQLineEdits:
            qLineEdit.setAlignment(Qt.AlignLeft)

        # Setting layout for input area
        for columnNumber in range(numberOfComponents+1):
            # Assigning shorter names
            qLineEdit = self.inputQLineEdits[columnNumber]
            qLabel = self.inputQLabelList[columnNumber]

            self.inputGeneralLayout.addWidget(qLineEdit, 0, columnNumber)
            self.inputGeneralLayout.addWidget(qLabel, 1, columnNumber)

    def attachInputBoxes(self, mainWindowLayout):
        """Attaches layout of inputRegion to mainWindowLayout"""
        mainWindowLayout.addLayout(self.inputGeneralLayout)

    def getAllLineEdits(self):
        """Returns a list containing all QLineEdits"""
        return self.inputQLineEdits

    def setAllLineEditsText(self, textList):
        """Set text in all line edits based on input textList"""
        # Check if lists' lengths are equal

        if len(textList) == len(self.inputQLineEdits):
            # Assign text to every QLineEdit
            for qLineEdit, text in zip(self.inputQLineEdits, textList):
                qLineEdit.setText(text)
        # If input textList has incorrect length
        else:
            print("Cannot set text for QLineEdits. List's length does not match")

    def setAllLabels(self, textList):
        """Set the text for every QLabel"""
        # Check if lists' lengths are equal

        if len(textList) == len(self.inputQLabelList) - 1:
            # Assign text to every QLabel
            for qLabel, text in zip(self.inputQLabelList[1:], textList):
                qLabel.setText(text)
        # If input textList has incorrect length
        else:
            print("Cannot set text for QLabels. List's length does not match")
