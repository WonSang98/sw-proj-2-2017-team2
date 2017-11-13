from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLineEdit, QToolButton
from PyQt5.QtWidgets import QSizePolicy
from PyQt5.QtWidgets import QLayout, QGridLayout

from keypad2 import numPadList, operatorList, constantList, functionList
from calcFunctions import factorial, decToBin, binToDec

#이전코드와의 차이점. 버튼이 커짐!!!!
#버튼클래스 따로 안만들었다면 버튼의 사이즈 각각 바꾸고싶으면..노답..

#일률적으로 버튼에 다른 효과도 줄수있어 ..이렇게하면 ´ ▽ ` )ﾉ

class Button(QToolButton):
    #버튼을 아예 클래스로 만듬

    def __init__(self, text, callback):
        super().__init__()
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        #버튼의 크기를 크게만듬..밑에 sizeHint가지고 한거
        # 아직 모르는걸로 하자..(￣□￣)
        self.setText(text)#버튼의 얼굴이 text
        self.clicked.connect(callback)
        #callback에는 buttonClicked가 주어질것임. 버튼눌리면 buttonCLicked호출

    def sizeHint(self):
        #원래 QTool버튼에 있던 함수.. 를 오버라이드 한거임
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
        #조금 늘려서

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
        
    def buttonClicked(self):
        button =self.sender()
        key = button.text() #눌린버튼이름
        operator = ['*', '+', '-', '/', '.']

        if self.display.text() == 'error':
            self.display.setText('')
            #에러메시지 뜬 상태로 아무버튼 누르면 리셋.
        
        elif key == '=':
        # = 눌리면 창에입력된 연산 실행하고 결과창에표시
            try:
            #예외처리..
                result = str(eval(self.display.text()))
                self.display.setText(result)
            except:
                self.display.setText('error')
        
        elif key == 'C':
            self.display.setText("")
            
        elif key in functionList:
            #함수 버튼 입력 했을때
            n = self.display.text()
            self.display.setText(self.functiondic[key](n))

        elif key in constantList:
            self.display.setText(self.display.text()+str(self.constantdic[key]))

        else:
            if self.display.text() == ''and key in operator:
            #연산기호부터 입력못하도록 예외처리.
                pass
            
            elif self.display.text() != ''and self.display.text()[-1] in operator:
                if self.display.text()[-1] == '*' and self.display.text()[-2] != '*' and key == '*':
                    self.display.setText(self.display.text()+key)
                elif self.display.text()[-1] == '/' and self.display.text()[-2] != '/' and key == '/':
                    self.display.setText(self.display.text()+key)
                elif key not in operator:
                    self.display.setText(self.display.text()+key)
                else:
                    pass
                
            #**랑 //제외하고, 연속으로 연산기호가 입력되지 않도록 예외처리
            #self.display.text()가 비어있을때 인덱스[-1]는 에러남!..

            
            else:
                self.display.setText(self.display.text()+key)


if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())


