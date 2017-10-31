import pickle
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, 
    QHBoxLayout, QVBoxLayout, QApplication, QLabel, 
    QComboBox, QTextEdit, QLineEdit, QGridLayout)
from PyQt5.QtCore import Qt

class ScoreDB(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        self.scdb = []
        self.readScoreDB()
        self.showScoreDB()



    def initUI(self):

        self.dbfilename = 'assignment6.dat'
        #버튼 이름 or Widget리스트 관리하기 위한 List 일종의 1차 원재료모임
        label = ['Name', 'Age', 'Score', 'Amount']
        push = ['Add', 'Del', 'Find', 'Inc', 'Show']
        p_d = ['AddClick', 'DelClick', 'FindClick', 'IncClick', 'ShowClick' ]
        self.list = []
        self.list2 = []
        plist = []
        self.txt = QTextEdit()
        self.combo = QComboBox(self)
        key = QLabel("key", self)
        result = QLabel("Result", self)
        self.scdb = self.readScoreDB()
        #실행시 맨 위줄에 위치하게 되는 라벨과 빈칸 리스트로 저장
        for i in label:
            self.list.append(QLabel(i, self))
            self.list2.append(QLineEdit(self))
            if i != 'Amount':
                self.combo.addItem(i)

        #첫번째 박스에 위에서 저장한 리스트 배치
        hbox1 = QHBoxLayout()
        for i in range(4):
            hbox1.addWidget(self.list[i])
            hbox1.addWidget(self.list2[i])

        #실행시 두번째 줄에 위치하게 되는 라벨과 버튼 저장
        plist.append(key)
        plist.append(self.combo)
        cnt = 0
        for i in push:
            plist.append(QPushButton(i, self))

        #버튼 이벤트
        plist[2].clicked.connect(self.AddClick)
        plist[3].clicked.connect(self.DelClick)
        plist[4].clicked.connect(self.FindClick)
        plist[5].clicked.connect(self.IncClick)
        plist[6].clicked.connect(self.ShowClick)




        #두번째 박스에 위에서 저장한 리스트 배치
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        for i in plist:
            hbox.addWidget(i)
        #세번째 박스에 위에서 저장한 리스트 배치
        hbox3 = QHBoxLayout()
        hbox3.addWidget(result)


        #네번째 박스 정의 후 txtedit 배치
        hbox2 = QHBoxLayout()
        hbox2.addWidget(self.txt)


        #만든 세 개의 박스를 하나의 큰 박스에 배치
        vbox = QVBoxLayout()
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox)
        vbox.addLayout(hbox3)
        vbox.addLayout(hbox2)
        self.setLayout(vbox)




        #Window창
        self.setGeometry(600, 600, 750, 500)
        self.setWindowTitle('Assignment6')

        self.show()


    def closeEvent(self, event):

        self.writeScoreDB()

    def readScoreDB(self):
        try:
            fH = open(self.dbfilename, 'rb')
        except FileNotFoundError as e:
            print("New DB: ", self.dbfilename)
            return []

        self.scdb = []
        try:
            self.scdb = pickle.load(fH)
        except:
            print("Empty DB: ", self.dbfilename)
        else:
            print("Open DB: ", self.dbfilename)

        fH.close()
        return self.scdb
    # write the data into person db
    def writeScoreDB(self):
        fH = open(self.dbfilename, 'wb')
        pickle.dump(self.scdb, fH)
        fH.close()


    #TextEdit인 txt에 pickle한 데이터출력
    #단 age와 score가 정수가 아닌 데이터는 삭제하여 출력한다.
    def showScoreDB(self):
        list = []
        for p in range(len(self.scdb)):
            try:
                self.scdb[p]['Score']=int(self.scdb[p]['Score'])
                self.scdb[p]['Age']=int(self.scdb[p]['Age'])
            except ValueError:
                list.append(p)
        for i in range(len(list)):
            del self.scdb[list[i] - i]

        for i in range(len(self.scdb)):

            self.txt.append("%d %5s %29s %29s %29s %29s %29s" %(i+1,'Name', str(self.scdb[i]['Name']),
                                                       'Age', str(self.scdb[i]['Age']),
                                                       'Score', str(self.scdb[i]['Score'])))
    #추가하는 이벤트 이름,나이,성적 3개의 인자 중 하나라도 빈칸일시 Add안됨
    def AddClick(self):
        record = {'Name':self.list2[0].text(), 'Age':self.list2[1].text(), 'Score':self.list2[2].text()}
        if len(self.list2[0].text()) * len(self.list2[1].text()) * len(self.list2[2].text()) == 0:
            pass
        else:
            self.scdb += [record]
            self.txt.setText("")
            self.showScoreDB()

    #삭제하는 이벤트
    def DelClick(self):
        list = []

        for p in range(len(self.scdb)):
            if self.scdb[p]['Name'] == self.list2[0].text():
                list.append(p)

        print(list)

        for i in range(len(list)):
            del self.scdb[list[i] - i]

        self.txt.setText("")
        self.showScoreDB()

    def FindClick(self):
        list = []
        for p in range(len(self.scdb)):
            if self.scdb[p]['Name'] == self.list2[0].text():
                list.append(p)
        self.txt.setText("")
        for i in list:
            self.txt.append("%5s %29s %29s %29s %29s %29s" %('Name', str(self.scdb[i]['Name']),
                                                       'Age', str(self.scdb[i]['Age']),
                                                       'Score', str(self.scdb[i]['Score'])))

    def IncClick(self):
        list = []
        try:
            self.list2[3] = int(self.list2[3].text())

            for p in range(len(self.scdb)):
                if self.scdb[p]['Name'] == self.list2[0].text():
                    list.append(p)

            for i in list:
                self.scdb[i]['Score'] += int(self.list2[3].text())
        except ValueError:
            pass
        self.txt.setText("")
        self.showScoreDB()



    def ShowClick(self):
        self.txt.setText("")
        key = self.combo.currentText()

        for i in sorted(self.scdb, key=lambda person: person[key]):
            self.txt.append("%5s %29s %29s %29s %29s %29s" % ('Name', str(i['Name']),
                                                              'Age', str(i['Age']),
                                                              'Score', str(i['Score'])))
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ScoreDB()
    sys.exit(app.exec_())


