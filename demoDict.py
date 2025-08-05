# demoDict.py


print("---형식 변환---")
a = set((1,2,3))
print(a)
b = list(a)
b.append(10)
print(b)
c=tuple(b)
print(c)


print("---dict---")
colors = {"apple":"red", "banana":"yellow"}
#입력
colors["cherry"] = "red"
colors["cherry"] = "blue"
print(colors)
print(colors["apple"])

#삭제
del colors["apple"]
print(colors)


#변수지정
device = {"맥북":0, "아이폰":0}

#입력
device["맥북"]=20
print(device)
device["아이폰"]=6
print(device)
#삭제
del device["맥북"]
#반복문
for item in device.items():
    print(item)

for k,v in device.items():
    print(k,v)