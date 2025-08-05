# 수열 함수

print("---수열함수---")
print(list(range(1, 11)))
print(list(range(2000, 2026)))
print(list(range(1, 32)))

print("---리스트내장---")
list2 = list(range(1, 11))
print(list2)
print([i**2 for i in list2 if i > 5])

tp = ("apple", "kiwi")
print([len(i) for i in tp])


# 필터링 함수
print("---필터링 함수---")
lst = [10,25,30]
def getBiggerThan20(i):
    return i > 20

itemL = filter(getBiggerThan20,lst)

for item in itemL:
    print(item)

print("----람다 함수 사용----")

itemL = filter(lambda x:x>20, lst)
for item in itemL:
    print(item)