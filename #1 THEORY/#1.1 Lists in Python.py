days = ["Mon", "Tue", "Wed", "Thur", "Fri", "Sat"]

print(type(days))  # <class 'list'>

print(days[3])  # Thur
print(len(days))  # 6

days.append("Sun")  # list에 Sun 추가.

print(days)
print(len(days))

days.reverse()  # List의 순서를 반대로
print(days)
# mutable =함수에서 변경 가능 값
# immutable = 변경 불가능한 값
