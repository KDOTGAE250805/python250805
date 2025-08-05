# 개발자 클래스를 정의

class Developer:
    def __init__(self, name, age, language):
        self.name = name
        self.age = age
        self.language = language

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Language: {self.language}")

# 인스턴스를 2개 생성
dev1 = Developer("Alice", 30, "Python")
dev2 = Developer("Bob", 25, "JavaScript")

# 정보 출력
print(dev1.display_info())
print(dev2.display_info())