# variable (변수)
a = 1   # global variable (전역변수)
b = 2
# print(a+b)


# Function (함수): 나중에 실행할 코드를 미리 적어두는 것
def multiply():
    c = a * b   # local variable (지역변수)
    print(c)

def substract():
    c = a - b
    print(c)

print(type(multiply))


# data type (데이터형)
# primitive data type : 메모리에 데이터 값이 저장됨

x = 1       # integer (숫자형), int
x2 = "1"
y = "data"  # string (문자형), str
z = True    # boolean (논리형), bool - 참, 거짓

# objective data type : 메모리에 주소값이 저장됨

m = [1, "ddd", False]                   # list (배열), list
n = {"name": "Yongsu", "age": 31}       # dictionary (객체), dict

# print(x, type(x))
# print(y, type(y))
# print(z, type(z))
# print(m, type(m))
# print(n, type(n))


# operator (연산자) : 사칙연산, 논리연산
# 사칙연산 : + - * /
# print(str(x) + y + str(z))

# 논리연산 : 비교(and or) -> Boolean type 의 결과값을 return 함
# print((1 < 3) and (False))    #하나라도 False 이면 False , 둘다 True 이면 True
# print(4 == 5 or True)   # 하나라도 True 이면 True
# print (4 != 5)  # ! 는 False 의 약어

# bitwise (비트연산자)
# print(True | False)
# print(True & False)


# list - 데이터가 순서대로 모여있는 집합체
# index 위치를 찾는다
list1 = [1, 2, "3", {}]     # 0, 1, 2, 3

# print(list1[2])
# print(list1[1:3])
# print(list1[1:])
# print(list1[3:1])
# print(list1[-3:-1])     # 음수는 뒤에서부터 찾는다


list2 = list1
list2[2] = "ㅋㅋㅋㅋ"

# list 자료형은 주소값이 메모리에 저장된다
# print(list2)
# print(list1)


# dictionary - key : value 로 이루어진 데이터 집합체
# key를 찾는다
dic1 = {"name": "Yongsu", "age": 31, "height": "174cm"}

# print(dic1["age"])
# print(dic1.get("age"))

# dic2 = dic1
# dic2["name"] = "허진우"
# print(dic1)


# copy : 깊은복사, 얕은복사
dic3 = dic1.copy()
dic3["name"] = "황병민"

# print(dic1)
# print(dic3)
