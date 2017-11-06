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
        self.display = QLineEdit('0')
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setMaxLength(15)
        self.temp1 = ''
        self.temp2 = ''
        # Digit Buttons

        num = ['7','8','9','4','5','6','1','2','3','0']
        self.digitButton = [x for x in range(10)]
        for i in range(10):
            self.digitButton[i] = Button(num[i])

        self.decButton = Button('.')
        self.eqButton = Button('=')

        # Operator Buttons
        self.mulButton = Button('*')
        self.divButton = Button('/')
        self.addButton = Button('+')
        self.subButton = Button('-')

        # Parentheses Buttons
        self.lparButton = Button('(')
        self.rparButton = Button(')')

        # Clear Button
        self.clearButton = Button('C')

        # Layout
        mainLayout = QGridLayout()
        mainLayout.setSizeConstraint(QLayout.SetFixedSize)

        mainLayout.addWidget(self.display, 0, 0, 1, 2)

        numLayout = QGridLayout()

        for j in range(10):
            a = j%3
            b = j/3
            numLayout.addWidget(self.digitButton[j], b, a)

        numLayout.addWidget(self.decButton, 3, 1)
        numLayout.addWidget(self.eqButton, 3, 2)

        mainLayout.addLayout(numLayout, 1, 0)

        opLayout = QGridLayout()

        opLayout.addWidget(self.mulButton, 0, 0)
        opLayout.addWidget(self.divButton, 0, 1)
        opLayout.addWidget(self.addButton, 1, 0)
        opLayout.addWidget(self.subButton, 1, 1)

        opLayout.addWidget(self.lparButton, 2, 0)
        opLayout.addWidget(self.rparButton, 2, 1)

        opLayout.addWidget(self.clearButton, 3, 0)

        mainLayout.addLayout(opLayout, 1, 1)

        self.setLayout(mainLayout)

        self.setWindowTitle("My Calculator")

        for i in range(10):
            self.digitButton[i].clicked.connect(self.ButtonClicked)
        self.decButton.clicked.connect(self.ButtonClicked)
        self.eqButton.clicked.connect(self.ButtonClicked)
        self.mulButton.clicked.connect(self.ButtonClicked)
        self.divButton.clicked.connect(self.ButtonClicked)
        self.addButton.clicked.connect(self.ButtonClicked)
        self.subButton.clicked.connect(self.ButtonClicked)
        self.lparButton.clicked.connect(self.ButtonClicked)
        self.rparButton.clicked.connect(self.ButtonClicked)
        self.clearButton.clicked.connect(self.ButtonClicked)

    def ButtonClicked(self):
        sender = self.sender()
        button = sender.text()

        if button != 'C' and button != '=':
            self.temp1 += button
            self.display.setText(self.temp1)
        elif button == 'C':
            self.temp1 = ''
            self.temp2 = ''
            self.display.setText(self.temp1)
        elif button == '=':
            try:
                self.temp2 = str((eval(self.temp2 + self.temp1)))
            except:
                self.display.setText('')
            else:
                self.display.setText(self.temp2)
                self.temp1 = ''

if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())