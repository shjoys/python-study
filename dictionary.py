# 1. clear()

def dic_clear():
    dic = {
        "name": "Yongsu",
        "age": 31,
        "favorites": "animation"
    }

    print("before : ", dic)
    dic.clear()
    print("after : ", dic)

# dic_clear()


# 2. copy()
def dic_copy():
    dic = {
        "name": "Yongsu",
        "age": 31,
        "favorites": "animation"
    }
    dic1 = dic
    dic2 = dic.copy()

    print("dic : ", dic)
    print("dic1 : ", dic1)
    print("dic2 : ", dic2)

    dic.clear()
    print("dic : ", dic)
    print("dic1 : ", dic1)
    print("dic2 : ", dic2)

# dic_copy()


# 3.fromkeys
def dic_fromkeys():
    dic = {
        "name": "Yongsu",
        "age": 31,
        "favorites": "animation"
    }

    dic0 = {}
    dic1 = dic0.fromkeys(["age", "name", "favorites"])
    dic2 = dic0.fromkeys(dic, "123")                 

    print("dic0 : ", dic0)
    print("dic1 : ", dic1)
    print("dic2 : ", dic2)

    dic0.clear()
    print("dic0 : ", dic0)
    print("dic1 : ", dic1)
    print("dic2 : ", dic2)

# dic_fromkeys()

# 4. get()
def dic_get():
    dic = {
        "name": "Yongsu",
        "age": 31,
        "favorites": "animation"
    }

    name1 = dic.get("name")
    name2 = dic["name"]             # attributes

    print("name1 : ", name1)
    print("name2 : ", name2)

    dic["name"] = "Jinwoo"          # attributes
    print("dic : ", dic)
    print("name1 : ", name1)
    print("name2 : ", name2)


# dic_get()

# 5. keys()
# 6. values()
def dic_key_values():
    dic = {
        "name": "Yongsu",
        "age": 31,
        "favorites": "animation"
    }

    keys = list(dic.keys())
    values = list(dic.values())

    print("keys : ", keys)
    print("values : ", values)

    print(type(dic.keys()))
    print(type(list(dic.keys())))

# dic_key_values()

# 7. items
def dic_items():
    dic = {
        "name": "Yongsu",
        "age": 31,
        "favorites": "animation"
    }

    dic2 = dic.items()          # dic -> list[...tuple]

    print(list(dic2))

# dic_items()

# 8. pop
# 9. popitem
def dic_pop():
    dic = {
        "name": "Yongsu",
        "age": 31,
        "favorites": ["animation", "alcohol", "money"],
        "address": "suwon",
        "sex": "male",
    }

    list = dic.pop("favorites")      # 기존 데이터 삭제,  삭제된 데이터 return

    print("dic : ", dic)
    print("list : ", list)

    tup = dic.popitem()
    print("dic : ", dic)
    print("tup : ", tup)

# dic_pop()


# 10. update
def dic_update():
    dic = {
        "name": "Yongsu",
        "age": 31,
        "favorites": ["animation", "alcohol", "money"],
        "address": "suwon",
        "sex": "male",
    }

    dic["age"] = 34
    dic.update({"address": "seoul"})
    dic.update({"height": "174"})

    print(dic)


# dic_update()
