from queue import PriorityQueue

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_in_alphabetical_order = sorted(students)
print(students_in_alphabetical_order)
average_score = {"Aaron": [5, 3, 3, 5, 4],
"Bilbo": [2, 2, 2, 3],
"Johnny": [4, 5, 5, 2],
"Khendrik": [4, 4, 3],
"Steve": [5, 5, 5, 4, 5]}

grades[0] = sum(grades[0]) / len(grades[0])
grades[1] = sum(grades[1]) / len(grades[1])
grades[2] = sum(grades[2]) / len(grades[2])
grades[3] = sum(grades[3]) / len(grades[3])
grades[4] = sum(grades[4]) / len(grades[4])
average_score["Aaron"] = grades[0]
average_score["Bilbo"] = grades[1]
average_score["Johnny"] = grades[2]
average_score["Khendrik"] = grades[3]
average_score["Steve"] = grades[4]
print(average_score)


#average_score["Aaron"]=grades[0]
#print(average_score)




















# students_1 = sum(grades[0]) / len(grades[0])
# print(students_1)
# students_2 = sum(grades[1]) / len(grades[1])
# print(students_2)
# students_3 = sum(grades[2]) / len(grades[2])
# print(students_3)
# students_4 = sum(grades[3]) / len(grades[3])
# print(students_4)
# students_4 = sum(grades[4]) / len(grades[4])
# print(students_4)




#print(sum(grades[0])),sum(grades[1]),(sum(grades[2]),sum(grades[3]),sum(grades[4]))
#print(students_in_alphabetical_order[0])+average_score[0]

from time import sleep



