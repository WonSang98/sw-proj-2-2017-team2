from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLineEdit, QToolButton
from PyQt5.QtWidgets import QSizePolicy
from PyQt5.QtWidgets import QLayout, QGridLayout


class Button(QToolButton):

    def __init__(self, text):
        super().__init__()
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.setText(text)

    def sizeHint(self):
        size = super(Button, self).sizeHint()
        size.setHeight(size.height() + 20)
        size.setWidth(max(size.width(), size.height()))
        return size


class Calculator(QWidget):
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
        # Display Window
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setMaxLength(15)
        self.txt = ""
        self.txt2 = ""
        # Digit Buttons
        numbers = ['7', '8', '9', '4', '5', '6', '1', '2', '3', '0']
        self.digitButton = [x for x in range(0, 10)]
        for i in range(len(numbers)):
            self.digitButton[i] = Button(numbers[i])

        options = ['*', '/', '+', '-', '(', ')', 'C', '.', '=']
        self.optionButton = [y for y in range(0, 10)]
        for i in range(len(options)):
            self.optionButton[i] = Button(options[i])

        # Layout
        mainLayout = QGridLayout()
        mainLayout.setSizeConstraint(QLayout.SetFixedSize)

        mainLayout.addWidget(self.display, 0, 0, 1, 2)

        numLayout = QGridLayout()

        j = 0
        for i in range(len(numbers)):
            numLayout.addWidget(self.digitButton[i], j, i%3)
            j = j + 1 if (i+1)%3 == 0 else j + 0

        numLayout.addWidget(self.optionButton[7], 3, 1)
        numLayout.addWidget(self.optionButton[8], 3, 2)

        mainLayout.addLayout(numLayout, 1, 0)

        opLayout = QGridLayout()

        j = 0
        for i in range(7):
            opLayout.addWidget(self.optionButton[i], j, i%2)
            j = j + 1 if (i+1)%2 == 0 else j + 0

        mainLayout.addLayout(opLayout, 1, 1)

        self.setLayout(mainLayout)
        
        self.setWindowTitle("My Calculator")

        #ButtonClicked Event
        for i in range(10):
            self.digitButton[i].clicked.connect(self.ButtonClicked)
        for j in range(len(options)):
            self.optionButton[j].clicked.connect(self.ButtonClicked)



    def ButtonClicked(self):
        sender = self.sender()
        button = sender.text()
        if button != '=' and button != 'C':
            self.txt += button
            self.display.setText(self.txt)

        elif button == "=":

            try:
                self.txt2 = str((eval(self.txt2+self.txt)))
            except :
                self.display.setText("")
            else:
                self.display.setText(self.txt2)
                self.txt = ""
        elif button == "C":
            self.txt = ""
            self.txt2 = ""
            self.display.setText(self.txt)



if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())

