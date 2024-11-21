first = int(input())
second = int(input())
third = int(input())
if first == second == third:
    print(3)
elif first==second or second==third or third==first:
    print(2)
else:
    print(0)

# first = (input())  # Если убрать "int", то можно вводить текс и тоже будет проверяться, прикольно ;)
# second = (input())
# third = (input())
# if first == second == third:
#     print(3)
# elif first == second or second == third or third == first:
#     print(2)
# else:
#     print(0)
