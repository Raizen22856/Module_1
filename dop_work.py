grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
number_1 =(sum(grades[0]))/len(grades[0])
number_2 =(sum(grades[1]))/len(grades[1])
number_3 =(sum(grades[2]))/len(grades[2])
number_4 =(sum(grades[3]))/len(grades[3])
number_5 =(sum(grades[4]))/len(grades[4])
a = list(students)
a.sort()
a = {a[0]: number_1, a[1]: number_2, a[2]: number_3, a[3]: number_4, a[4]: number_5}
print(a)