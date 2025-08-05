# demoindex.py

strA = "파이썬은 강력해"
strB = "python is very powerful"

print(len(strA))
print(len(strB))
print(strA[:2])
print(strB[:6]) 
print(strB[-3:])  


strC = '"""이번에는 다중의 라인을 저장합니다."""'

print(strC)


print('---리스트 형식---')
list = [10,20,30]
print(len(list))
print(list[0])
list.append(40)
print(list)
list.remove(20)
print(list)

list.insert(len(list),100)
print(list)

# 함수를 정의

def calc(a,b):
    return a+b, a*b

# 함수를 호출
print(calc(3,4))

print("id:%s, name:%s" % ("kim", "김유신"))

args = (5,6)
print(calc(*args))


# 자료형식 변환

a = set((1,2,3))