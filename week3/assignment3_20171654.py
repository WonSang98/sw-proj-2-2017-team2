#20171654
#WonSangYeon
#SW-proj2 Second assignment
#Console and file I/O

import pickle

dbfilename = 'test3_4.dat'

#test3_4.dat 파일을 불러와서 scdb에 저장
def readScoreDB():
	try:
		fH = open(dbfilename, 'rb')
	except FileNotFoundError as e:
		print("New DB: ", dbfilename)
		return []

	scdb = []
	try:
		scdb =  pickle.load(fH)
	except:
		print("Empty DB: ", dbfilename)
	else:
		print("Open DB: ", dbfilename)
	fH.close()
	return scdb


# write the data into person db
#사람들 정보가 입력되어 변형된 scdb를 원래 데이터파일에추가
def writeScoreDB(scdb):
    fH = open(dbfilename, 'wb')
    pickle.dump(scdb, fH)
    fH.close()

#String형태의 Score와 Age 형 변환
def str_to_int(scdb):
	for p in scdb:
		#Score 와 Age가 int형으로 변환 불가능시 제거하고 예외처리
		try:
			p['Score']=int(p['Score'])
			p['Age']=int(p['Age'])
		except ValueError:
			print("Wrong Input")
			del p

def doScoreDB(scdb):
	while(True):

		inputstr = (input("\nScore DB > "))
		if inputstr == "": continue
		parse = inputstr.split(" ")

		str_to_int(scdb)
		#각 메뉴마다 필요로하는 인덱스 값이 다르므로 IndexError예외처리
		try:
			if parse[0] == 'add':#마지막에 str_to_int함수 사용하여 형 변환

				record = {'Age':parse[1], 'Name':parse[2], 'Score':parse[3]}
				scdb += [record]
				str_to_int(scdb)

			elif parse[0] == 'find':

				for p in scdb:
					if p['Name'] == parse[1]:
						print(p)

			elif parse[0] == 'inc':

				for p in scdb:
					if p['Name'] == parse[1]:
						p['Score']+=int(parse[2])

			elif parse[0] == 'del':#지워야 할 대상들이 있는 index number를 list에 저장후 해당하는 인덱스 제거

				list = []

				for p in scdb:
					if p['Name'] == parse[1]:
						list.append(scdb.index(p))
				for i in range (0,len(list)):
					del scdb[list[i]-i]

			elif parse[0] == 'show':

				#show만 입력시 ㄱㄴㄷ순 정렬, show 다음 이름입력시 그 이름기준 정렬
				sortKey ='Name' if len(parse) == 1 else parse[1]
				showScoreDB(scdb, sortKey)

			elif parse[0] == 'quit':

				break

			else:
				print("Invalid command: " + parse[0])

		except IndexError:
				print("retry")



def showScoreDB(scdb, keyname):
	for p in sorted(scdb, key=lambda person: person[keyname]):
		print(p, end=' ')
		print()




scoredb = readScoreDB()
doScoreDB(scoredb)
writeScoreDB(scoredb)

