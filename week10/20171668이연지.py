from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLineEdit, QToolButton
from PyQt5.QtWidgets import QSizePolicy
from PyQt5.QtWidgets import QLayout, QGridLayout





#일률적으로 버튼에 다른 효과도 줄 수 있게되었다. ´ ▽ ` )ﾉ

class Button(QToolButton):
    #버튼을 아예 클래스로 만듬

    def __init__(self, text, callback):
        super().__init__()
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.setText(text)#버튼의 얼굴이 text
        self.clicked.connect(callback)
        #callback에는 buttonClicked가 주어질것임. 버튼눌리면 buttonCLicked호출

    def sizeHint(self):
        #원래 QTool버튼에 있던 함수.. 를 오버라이드 한것
        size = super(Button, self).sizeHint()
        size.setHeight(size.height() + 20)
        size.setWidth(max(size.width(), size.height()))
        return size

        

class Calculator(QWidget):
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
        # Display Window
        self.display = QLineEdit('')
        #0나오게 하면안돼..
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setMaxLength(15)
        
        # Digit Buttons
        self.digitButton = [x for x in range(0, 10)]

        for i in range(10):
            self.digitButton[i] = Button(str(i),self.buttonClicked)

        # . and = Buttons
        self.decButton = Button('.', self.buttonClicked)
        self.eqButton = Button('=', self.buttonClicked)

        # Operator Buttons
        self.mulButton = Button('*', self.buttonClicked)
        self.divButton = Button('/', self.buttonClicked)
        self.addButton = Button('+', self.buttonClicked)
        self.subButton = Button('-', self.buttonClicked)

        # Parentheses Buttons
        self.lparButton = Button('(', self.buttonClicked)
        self.rparButton = Button(')', self.buttonClicked)

        # Clear Button
        self.clearButton = Button('C', self.buttonClicked)

        # Layout
        mainLayout = QGridLayout()
        mainLayout.setSizeConstraint(QLayout.SetFixedSize)

        mainLayout.addWidget(self.display, 0, 0, 1, 2)

        numLayout = QGridLayout()

        numLayout.addWidget(self.digitButton[0], 3, 0)
        for i in range(1,10):
            numLayout.addWidget(self.digitButton[i], 2-((i - 1) // 3), (i - 1) % 3)
            #123,456,789말고 789,456,123순으로 행이 배치되도록 2에서 빼줌.

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
    def buttonClicked(self):
        button =self.sender()
        key = button.text() #눌린버튼이름
        operator = ['*', '+', '-', '/', '.']
        if key == '=':
        # = 눌리면 창에입력된 연산 실행하고 결과창에표시
            try:
            #예외처리..
                result = str(eval(self.display.text()))
                self.display.setText(result)
            except:
                self.display.setText('error')
        
        elif key == 'C':
            self.display.setText("")
        else:
            if self.display.text() == ''and key in operator:
            #operator은 연산기호가 들어있는 리스트.
            #연산기호부터 입력못하도록함
                pass
            
            elif self.display.text() != ''and self.display.text()[-1] in operator:
                #가장마지막에 입력된 것이 연산기호 인 경우.. (**와 //를 제외하고, 연산기호가 연달아 입력되지 못하도록 할것임(.
                if self.display.text()[-1] == '*' and self.display.text()[-2] != '*' and key == '*':
                    self.display.setText(self.display.text()+key)
                    #가장마지막에 입력된 것이 *이고 *가 또 입력되었을때 이건 입력되게 함. (***는 불가능)
                elif self.display.text()[-1] == '/' and self.display.text()[-2] != '/' and key == '/':
                    self.display.setText(self.display.text()+key)
                    #가장 마지막에 입력된 것이 / 이고 /가 또 입력되었을때 이것도 입력되게 함. (///는 불가능)
                elif key not in operator:
                    self.display.setText(self.display.text()+key)
                    #연산기호가 아닌, 숫자들은 마음껏 입력되게함.
                else:
                    pass
                    #나머지 경우는 위를 제외하고 연산기호가 연달아 눌린 경우이므로 눌리지 않게함.
                
        
            #self.display.text()가 비어있을때 인덱스[-1]는 에러나서 저렇게 써줌
                
            #더 간단하게 조건문 만들 수 있는것 같은데..모르겠다..
            
            else:
                self.display.setText(self.display.text()+key)


if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())
