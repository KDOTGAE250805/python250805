print("---함수 이름 해석---")
x=5     # 글로벌 변수 (우선순위2) / 참고 : 빌트인 변수가 최우선
def func(a):
    return a+x


#호출
print(func(1))

def func2(a):
    x=10    # 로컬 변수 (우선순위1)
    return a+x

#호출

print(func2(1))



#----------------------------

# 기본값

print("기본값")

def times(a=5,b=10):
    return a*b

print(times())
print(times(2,5))
print(times(1,1))


# 키워드 인자

def connectURI(server, port):
    strUrl = "http://" + server + ":" + port
    return strUrl


#호출
print(connectURI("multi.com","80"))
print(connectURI(port="80",server="multi.com"))

                 

