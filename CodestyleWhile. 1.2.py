my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
variables = 0
while variables <= len(my_list):
    if my_list[variables] == 0:
        variables = variables + 1
        continue
    if my_list < [0]:
        break
    if my_list[variables] < 0:
        break

    print(my_list[variables])
    variables = variables + 1
    if variables == len(my_list):
            break











