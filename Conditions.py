# 조건문
# 원하는 값을 찾기위해 분기를 시키는 것

def test_if_1(num):

    if(num > 0):            # True / False
        print("양수!")
    elif(num < 0):
        print("음수!")
    else:
        print("0!")


# test_if_1(100)
# test_if_1(-90)
# test_if_1(0)


def test_if_2(num1, num2):
    # 곱셈 결과가 양수인지 음수인지 확인하는 함수
    if(num1 > 0 and num2 > 0):
        print("양수!")
    elif(num1 < 0 and num2 < 0):
        print("양수!")
    elif(num1 == 0 or num2 == 0):
        print("0!")
    else:
        print("음수")

# test_if_2(1, 5)
# test_if_2(0, 5)
# test_if_2(-0, -5)
# test_if_2(-2, 5)


# 반복문
# 원하는 값을 찾기위해 반복적으로 일을 수행하는 것
def test_roop_1():
    product = ["자동차", "비행기", "선박"]
    price = [1500, 4000, 2000]
    discount = [0.1, 0.15, 0.2]

    index = 0
    for value in product:
        print("index : "+str(index))
        new_price = price[index] * (1 - discount[index])
        print("new price : "+str(new_price))
        index = index + 1


# test_roop_1()

def test_roop_2():
    product = ["비행기", "자동차", "선박"]
    price = [1500, 4000, 2000]
    discount = [0.1, 0.15, 0.2]


    for (index, value) in enumerate(product):
        print("index : "+str(index))
        new_price = price[index] * (1 - discount[index])
        print("new price : "+str(new_price))

# test_roop_2()


def test_roop_3():
    catalog = [
        {'product': '자동차', 'price':1500, 'discount': 0.1},
        {'product': '비행기', 'price':4000, 'discount': 0.15},
        {'product': '선박', 'price':2000, 'discount': 0.2},
    ]

    for (index, value) in enumerate(catalog):
        print("index : "+str(index))
        new_price = value['price'] * (1 - value['discount'])
        print("new price : "+str(new_price))


# test_roop_3()