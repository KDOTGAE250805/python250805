strName = "Not Class Member"

class DemoString:
    def __init__(self):
        self.strName = "" 
    def set(self, msg):
        self.strName = msg
    def print(self):
        #버그
        print(strName) # self 를 안붙으면 전역변수가 입려됨. 주의
        #정상
        print(self.strName)

d = DemoString()
d.set("First Message")
d.print()
