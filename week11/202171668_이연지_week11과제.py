from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLineEdit, QToolButton
from PyQt5.QtWidgets import QSizePolicy
from PyQt5.QtWidgets import QLayout, QGridLayout

from keypad2 import numPadList, operatorList, constantList, functionList
from calcFunctions import factorial, decToBin, binToDec


#일률적으로 버튼에 다른 효과도 줄수있어 ..이렇게하면 ´ ▽ ` )ﾉ

class Button(QToolButton):
    #버튼을 아예 클래스로 만듬

    def __init__(self, text, callback):
        super().__init__()
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.setText(text)#버튼의 얼굴이 text
        self.clicked.connect(callback)

    def sizeHint(self):
        size = super(Button, self).sizeHint()
        size.setHeight(size.height() + 25)
        size.setWidth(max(size.width(), size.height()))
        return size

        

class Calculator(QWidget):
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
        # Display Window
        self.display = QLineEdit('')
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setMaxLength(25)

        numLayout = QGridLayout()
        opLayout = QGridLayout()
        conLayout = QGridLayout()
        funLayout = QGridLayout()
        
        buttonGroups = {
            'num':{'buttons':numPadList, 'layout':numLayout,'columns':3},
            'op':{'buttons':operatorList,'layout':opLayout,'columns':2},
            'con':{'buttons':constantList, 'layout':conLayout, 'columns':1},
            'fun':{'buttons':functionList, 'layout':funLayout, 'columns':1},
            }
        # 사전하나와 포문으로 버튼배열하기

        self.functiondic = {'factorial (!)' : factorial, '-> binary': decToBin, 'binary -> dec': binToDec}

        self.constantdic = { 'pi':3.141592, '빛의 이동 속도 (m/s)': 3E+8, '소리의 이동 속도 (m/s)': 340,'태양과의 평균 거리 (km)': 1.5E+8}
        # 밑에서 버튼이 눌렸을때 버튼이름(키)에 대응되는 함수나 상수를 키값으로 설정.


        
        for label in buttonGroups.keys():
            # 위에있는 사전의 키들 :label 은 num, op
            r = 0
            c = 0
            buttonPad = buttonGroups[label]
            for buttontext in buttonPad['buttons']:
                #버튼들 순환
                button = Button(buttontext, self.buttonClicked)
                buttonPad['layout'].addWidget(button, r, c)
                c += 1
                if c >= buttonPad['columns']:
                    c = 0; r += 1

        

        # Layout
        mainLayout = QGridLayout()
        mainLayout.setSizeConstraint(QLayout.SetFixedSize)
        mainLayout.addWidget(self.display, 0, 0, 1, 2)
        mainLayout.addLayout(numLayout, 1, 0)
        mainLayout.addLayout(opLayout, 1, 1)
        mainLayout.addLayout(conLayout, 2, 0)
        mainLayout.addLayout(funLayout, 2, 1)

        self.setLayout(mainLayout)
        
        self.setWindowTitle("My Calculator")
        self.equalPressed = False
        
    def buttonClicked(self):
        button =self.sender()
        key = button.text() #눌린버튼이름
        txt = self.display.text()
        operator = ['*', '+', '-', '/', '.']
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

        if self.display.text() == 'error':
            self.display.setText('')
            #에러메시지 뜬 상태로 아무버튼 누르면 리셋.
        
        elif key == '=':
        # = 눌리면 창에입력된 연산 실행하고 결과창에표시
            try:
            #예외처리..
                result = str(eval(txt))
                self.display.setText(result)
                self.equalPressed = True
            except:
                self.display.setText('error')
        
        elif key == 'C':
            self.display.setText("")
            self.equalPressed = False
            
        elif key in functionList:
            #함수 버튼 입력 했을때
            n = txt
            self.display.setText(self.functiondic[key](n))
            #함수명은 사전에 키, 함수는 키값
        elif key in constantList:
            self.display.setText(txt+str(self.constantdic[key]))
        elif key in operator:
            if txt == '':
            #처음부터 연산기호를 입력하지 못하도록함
                pass

            elif txt[-1] in operator:
                #연산기호를 두번연속 누르려 할떄..

                if txt[-1] in ['*', '/'] and txt[-2] != txt[-1] and key == txt[-1]:
                    self.display.setText(txt + key)
                    #두 조건문을 하나의 조건문으로 줄임
                    #*와 /만 2번연속으로 입력되는것을 허용함. (3번은불가능)

                else:
                    pass
                    #위에있는 case들을 제외하고 연산기호가 연달아 눌린 경우는 안되게함.
            
            else:
                self.display.setText(txt + key)
                self.equalPressed = False
                #여기서 False로 변경해줘야..한번 = 를 누른 뒤, 연산기호입력 후 숫자를 2개이상 쓸수있음
                #비어있지도 않고 연속도 아니면 연산기호를 누를수 있음.
        elif key in numbers:
                 if self.equalPressed == True:
                    # '=' 이 눌렸다면, 연산기호 부터 입력해야함
                    pass
                 else:
                    self.display.setText(txt + key)
        elif key == "(" or key ==")":
            self.display.setText(txt + key)

if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())


