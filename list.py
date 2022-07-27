# 1. append()

def append_list():
    list_a = ["a", "p", "p", "l", "e"]

    print("before : ", list_a)
    list_a.append("s")

    print("after : ", list_a)


# append_list()


# 2.clear()
def clear_list():
    list_a = ["a", "p", "p", "l", "e"]

    print("before : ", list_a)
    list_a.clear()

    print("after : ", list_a)

# clear_list()


# 3.copy()
def copy_list():
    list_a = ["a", "p", "p", "l", "e"]

    list_b = list_a.copy()  # list_a 의 원본값을 유지하기 위해 복사

    list_c = list_b         # list_b 와 list_c는 같은 주소값을 공유함

    list_b.append("s")

    print("list_a : ", list_a)
    print("list_b : ", list_b)
    print("list_c : ", list_c)
    

# copy_list()


# 4.count()
def count_list():
    list_a = ["a", "p", "p", "l", "e"]

    cnt_all = len(list_a)
    cnt_p = list_a.count("p")

    print(cnt_all)
    print(cnt_p)

# count_list()
    

# 5.extend()
def extend_list():
    list_a = ["a", "p", "p", "l", "e"]

    print("before : ", list_a)
    
    list_a.extend(["s", "w"])   # 새로운 list 의 요소들을 꺼내서 요소들을 넣어줌
    print("extend : ", list_a)

    list_a.append(["s", "w"])   # 새로운 list 자체를 넣어줌
    print("append : ", list_a)

# extend_list()

# 6.index()
def index_list():
    list_a = ["a", "p", "p", "l", "e"]

    print("index l :", list_a.index("l"))
    # print("index l :", list_a.index("l", 0, 2))   # 지정된 범위안에 요소가 없으면 error 발생
    print("index l :", list_a.index("l", 3, 4))

# index_list()


# 7.insert()
def insert_list():
    list_a = ["a", "p", "p", "l", "e"]

    print("before : ", list_a)
    list_a.insert(2, [5, 8])
    print("after : ", list_a)

# insert_list()


# 8.pop()
def pop_list():
    list_a = ["a", "p", "p", "l", "e"]

    print("before : ", list_a)
    value = list_a.pop(2)
    print("value : ", value)
    print("after : ", list_a)

# pop_list()

# 9.remove()
def remove_list():
    list_a = ["a", "p", "p", "l", "e"]

    print("before : ", list_a)
    list_a.remove("p")              # 중복된 요소가 있으면 제일 앞 요소를 지운다
    print("after : ", list_a)

# remove_list()

#### use set : set 은 중복을 허용하지 않는 list ,  set = {"a", "p", "p", "l", "e"}
#print({"a", "p", "p", "l", "e"})
def remove_list_dup():
    list_a = ["a", "p", "p", "p", "p", "l", "e"]

    print("before : ", list_a)
    list_a = list(set(list_a))
    print("after : ", list_a)


# 10, 11. remove_list_dup()
def sort_list():
    list_a = ["a", "p", "P", "p", "b", "l", "e", "B"]

    print("list_a : ", list_a)
    
    list_a.reverse()
    print("reversed list_a : ", list_a)

    list_a.sort(reverse=True)      # parameter 가 없을경우 : reverse=False (오름차순) / reverse=True (오름차순)
    print("list_a : ", list_a)

# sort_list()

# 12-1. join()
def join_list():
    list_a = ["a", "p", "p", "l", "e"]

    print("".join(list_a))
    print(" ".join(list_a))
    print("!".join(list_a))

    # list_b = [1, 2, 3, 4, 5]
    # print("".join(list_b))    # int 타입 요소는 join 할수 없음 > str 으로 형변환 해줘야함
    
# join_list()

# 12-2. split()
def split_str():
    str_a = "hello, sexy, guys"

    print(str_a.split())        # 기본적으로 공백으로 잘라서 list 로 return
    print(str_a.split(" "))
    print(str_a.split(","))

# split_str()

# 12-3. del list
def del_list():
    list_a = ["a", "p", "p", "l", "e"]

    del list_a[2:3]     # keyword del 사용
    print(list_a)

# del_list()