grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_list = list(students)
students_list = sorted(students_list)
students_dict = {}
i=0

while i < len(students_list):
    grade = int(sum(grades[i]))/len(grades[i])
    students_dict.update({students_list[i] : grade})
    i+=1

print(students_dict)