# tuple은 common operations만 가능
# tuple을 만드는 방법은 [] 대신 ()로 감싸주면 된다.

days = ("Mon", "Tue", "Wed", "Thur", "Fri", "Sat")

print(type(days))  # <class 'tuple'>
# 이 리스트의 어떤 것도 변경하고 싶지 않다면 tuple을 사용한다.

# varible 정의 시 key = value 같은 느낌으로 작성.
me = {
    "name": "lhc",
    "age": 20,
    "korean": True,
    "fav_food": ["pizza", "air"]
}

print(me)
print(me["age"])
me["handsome"] = True
# {'name': 'lhc', 'age': 20, 'korean': True, 'fav_food': ['pizza', 'air'], 'handsome': True}
print(me)
# dictionary 안에 정보를 list, tuple, boolean, number 등 다양한 type으로 저장할 수 있음
