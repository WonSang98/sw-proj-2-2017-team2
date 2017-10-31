import pickle
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, 
    QHBoxLayout, QVBoxLayout, QApplication, QLabel, 
    QComboBox, QTextEdit, QLineEdit,QMessageBox)
from PyQt5.QtCore import Qt, pyqtSignal, QObject

class Communicate(QObject):
    closeApp = pyqtSignal()



class ScoreDB(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        self.dbfilename = 'assignment6.dat'
        self.scoredb = []
        self.readScoreDB()
        self.showScoreDB()
        
    def initUI(self):
        self.c = Communicate()
        self.c.closeApp.connect(self.msgBox)
        
        name_title = QLabel('Name')
        age_title = QLabel('Age')
        score_title = QLabel('Score')
        amount_title = QLabel('Amount')
        #self를 인자로 주는것은 (pyqt5 menual에 나와있는데)
        #아마도 얘가 self의 하위레벨인 위젯임을 나타내는 뜻 같음.
        key_title = QLabel('Key')
        result_title =QLabel('Result')
        #label widget들을 만듬.

        self.name_edit = QLineEdit()
        #와 얘네앞에 self안붙이면 밑에서 text()함수로 내용못읽어오네?
        self.age_edit = QLineEdit()
        self.score_edit = QLineEdit()
        self.amount_edit = QLineEdit()
        self.comboBox = QComboBox() 
        self.comboBox.addItem("Score")
        self.comboBox.addItem("Age")
        self.comboBox.addItem("Name")
        #'콤보박스'객체에 아이템 추가하는 함수 -> addItem()
        self.result_text = QTextEdit()
        #mytext = self.textEdit.toPainTest() 으로 내용 따올수 있음.
        #QLineEdit, QComboBox, QTextEdit 위젯들을 만듬.
        #앞에 self. 을 붙이지 않으면 다른함수에서 쓰지를 못하나?그런것같음.

        add_button = QPushButton("add")
        del_button = QPushButton("del")
        find_button = QPushButton("find")
        inc_button = QPushButton("inc")
        show_button = QPushButton("show")
        #버튼 위젯들을 만듬.

        add_button.clicked.connect(self.buttonClicked)
        del_button.clicked.connect(self.buttonClicked)
        find_button.clicked.connect(self.buttonClicked)
        inc_button.clicked.connect(self.buttonClicked)
        show_button.clicked.connect(self.buttonClicked)
        #버튼이 눌릴때마다 슬롯에 연결 (슬롯은 내가 정의함)

        #위젯은 전부 만들었습니다.........................-_-
        #---------------------------------------------------------


        box1 = QHBoxLayout()
        box1.addStretch(1)
        box1.addWidget(name_title)
        box1.addWidget(self.name_edit)
        box1.addWidget(age_title)
        box1.addWidget(self.age_edit)
        box1.addWidget(score_title)
        box1.addWidget(self.score_edit)
        #첫번째줄 box1완성

        box2 = QHBoxLayout()
        box2.addStretch(1)
        box2.addWidget(amount_title)
        box2.addWidget(self.amount_edit)
        box2.addWidget(key_title)
        #box2.addWidget(self.key_edit)
        box2.addWidget(self.comboBox)
        #두번째줄 box2완성

        box3 = QHBoxLayout()
        box3.addStretch(1)
        box3.addWidget(add_button)
        box3.addWidget(del_button)
        box3.addWidget(find_button)
        box3.addWidget(inc_button)
        box3.addWidget(show_button)
        #세번째줄 box3완성_ 버튼들

        box4 = QHBoxLayout()
        box4.addWidget(result_title)
        #result 라벨 하나를 위한 box4완성
        
        box5 = QHBoxLayout()
        box5.addWidget(self.result_text)
        #result 텍스트 하나를 위한 box5완성

        allbox = QVBoxLayout()
        allbox.addStretch(1)
        allbox.addLayout(box1)
        allbox.addLayout(box2)
        allbox.addLayout(box3)
        allbox.addLayout(box4)
        allbox.addLayout(box5)
        #allbox는 메인 레이아웃(세로박스)
        
        self.setLayout(allbox)

        self.setGeometry(600, 400, 350, 300)
        self.setWindowTitle('Assignment6')
        self.show()
    def msgBox(self):
        reply = QMessageBox.question(self,'Message',"끌거야?",QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        
    def error(self):
        self.c.closeApp.emit()


    def closeEvent(self, event):
        
        self.writeScoreDB()

    def readScoreDB(self):
        
        try:
            fH = open(self.dbfilename, 'rb')
        except FileNotFoundError as e:
            self.scoredb = []
            return

        try:
            self.scoredb =  pickle.load(fH)
        except:
            pass
        else:
            pass
        fH.close()


    # write the data into person db
    def writeScoreDB(self):
        fH = open(self.dbfilename, 'wb')
        pickle.dump(self.scoredb, fH)
        fH.close()

    def showScoreDB(self):
        pass
    def buttonClicked(self):
        #어떤 버튼이라도 눌리면 이 함수로.
        sender = self.sender()
        button = sender.text()
        #눌른 버튼의 이름 == sender.text()
        if button == "add":
            name = self.name_edit.text()
            #.text()함수로 QEdit 에서 내용가져올수있음.
            age = self.age_edit.text()
            score = self.score_edit.text()
            print(name,age,score)
            record = {'Name':name, 'Age':int(age),'Score':int(score)}
            self.scoredb += [record]

        elif button == "del":
            name = self.name_edit.text()
            
            remlist = []
            for p in self.scoredb:
                if p['Name'] == name:
                    remlist.append(p)
            for p in remlist:
                    self.scoredb.remove(p)
                    
        elif button == "show":
            #mytext = self.result_text.toPlainText()
            #textEdit에서 글자 가져오는함수.//그냥 써본것..
            
            display =""
            key = self.comboBox.currentText()
            #콤보박스에서 고른 아이템 리턴하는 함수.
            for p in sorted(self.scoredb, key = lambda person: person[key]):

                for attr in p:
                    display += attr+" = "+str(p[attr])+" "
                    #str() 안하면 에러..
                display += '\n'
            self.result_text.setPlainText(display)
            self.error()
            #textEdit에 글자 쓰는 함수.

            
                    
        elif button == "find":
            name = self.name_edit.text()
            display = ""
            for p in self.scoredb:
                if p["Name"] == name:
                    
                    display += 'name = '+name+' age = '+str(p['Age']) +' Score = '+str(p['Score'])+'\n'
            self.result_text.setPlainText(display)            
            
        elif button == "inc" :
            name = self.name_edit.text()
            amount = self.amount_edit.text()
            for p in self.scoredb:
                if p["Name"] == name:
                   p["Score"] += int(amount)
            
        
if __name__ == '__main__':

    
    app = QApplication(sys.argv)
    ex = ScoreDB() # ScoreDB실행.
    sys.exit(app.exec_())


#self.을 안붙이고 하면 창이그냥 꺼진다.
#뭐든간에 에러가발생하면 에러이유안뜨고 그냥 창이 꺼진다..(스트링을 인트로바꾼다던지)


#나도 예외처리 할거야..
