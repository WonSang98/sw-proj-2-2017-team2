class Parent:
    money = 10000
    name = '부모'
    age = 100 #이건 클래스의 멤버 변수! Parent.name
    def __init__(self,name,age):
        self.name =name;
        self.age = age; #이건 인스턴스의 변수! p.name
    def introduce(self):
        print("안녕 나는 %s야" %(self.name))
p = Parent("lee",20)

class Child(Parent):#extends대신 이거
    def __init__(self,name,age,gender):
        super().__init__(name,age) #자바의 super() 생성자와 유사.
        self.gender = gender
    def introduce(self):
        print("안녕 나는 %s이구 %s야" %(self.name,self.gender))

c = Child("yoon",30,'남자')

c.introduce()

print(c.name)

    
