# Средний балл 1вариант
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_sort= sorted(students)
grades_auto = []
for num in grades:
    s = sum(num)/len(num)
    grades_auto.append(s)
magazine = dict(zip(students_sort, grades_auto))
print(magazine)
# 2 вариант
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
grades_auto = [sum(grades[0])/len(grades[0]), sum(grades[1])/len(grades[1]), sum(grades[2])/len(grades[2]), sum(grades[3])/len(grades[3]),
               sum(grades[4])/len(grades[4])]
students_sort= sorted(students)
magazine = dict(zip(students_sort, grades_auto))
print(magazine)

