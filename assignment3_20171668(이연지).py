import pickle

dbfilename = 'assignment3.dat'

def readScoreDB():
    try:
        fH=open(dbfilename, 'rb')
    except FileNotFoundError as e:
        print("New DB: ", dbfilename)
        return[]
    scdb =[]
    try:
        scdb = pickle.load(fH)
    except:
        print("Empty DB: ", dbfilename)
    else:
        print("Open DB: ", dbfilename)
    fH.close()
    return scdb

def writeScoreDB(scdb):
    fH = open(dbfilename, 'wb')
    pickle.dump(scdb, fH)
    fH.close()
def doScoreDB(scdb):
    while(True):
        inputstr=(input("Score DB >"))
        if inputstr =="": continue

        parse = inputstr.split(" ")
        if parse[0] =='add':
            if len(parse) == 4:
                try:
                    record = {'Name':parse[1], 'Age':int(parse[2]),'Score':int(parse[3])}
                    scdb += [record]
                except ValueError :
                    print("나이와 점수는 정수로 입력해주세요")
                    #정수로 입력안하면 거절 (ex.21살, 70점)
            else:
                print("'add 이름 나이 점수' 양식을 맞춰주세요")

        elif parse[0] == 'del':
            remlist=[]
            #지울 것들을 빈 리스트에 담자
            if len(parse) == 2:
                for p in scdb:
                    if p['Name'] == parse[1]:
                        remlist.append(p)
                for p in remlist:
                    scdb.remove(p)
                    #remlist 따로만들어서 귀찮게 이 짓을 하는 이유:for loop 안에서 scde.remove(p)하니까 1,3,5,7..번째만 지워진다..왜 그런지는 모르겠다..
    
            else:
                print("'del name' 양식을 맞춰주세요")
        elif parse[0] =='show':
            if len(parse) == 1:
            #show 만 입력시
                sortkey = 'Name'
                showScoreDB(scdb, sortkey)

            elif len(parse) == 2:
            #show + sortkey 입력시
                sortkeylist = ["Age","Name","Score"]
                if parse[1] in sortkeylist:
                    sortkey = parse[1]
                    showScoreDB(scdb, sortkey)
                else:
                    print("sort key에는 Name,Age,Score 이 있습니다")
            else:
                print("sortkey는 하나만 써요")
                
        elif parse[0] == 'find':
            if len(parse) == 2:
                finder(scdb,parse[1])
                #함수 실행
            else:
                print("'find name' 양식을 맞춰주세요")
        elif parse[0] == 'inc':
            if len(parse) == 3:
                try:
                    inc(scdb, parse[1], int(parse[2]))
                    #함수 실행
                except ValueError:
                    print("amount 는 정수여야 합니다")
                    #amount가 정수가 아닐때 에러 처리                 
            else:
                print("'inc name amount'양식을 맞춰 주세요")
                
        elif parse[0] =='quit':
            break
        else:
            print("Invalid command:" + parse[0])
def showScoreDB(scdb, keyname):
    for p in sorted(scdb, key=lambda person: person[keyname]):
        for attr in sorted(p):
            print(attr , "=" , p[attr],end=' ')
        print()

def finder(scdb, who):
    for p in scdb:
        if p["Name"] == who:
            print(p)
def inc(scdb, who, amount):
    for p in scdb:
        if p["Name"] == who:
            p["Score"] += amount


scoredb=readScoreDB()
doScoreDB(scoredb)
writeScoreDB(scoredb)

