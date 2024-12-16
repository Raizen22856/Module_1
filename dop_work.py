grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
i = 0
b = []
for number in grades:
    b.append(sum(grades[i]) / len(grades[i]))
    i = i+1
a = list(students)
a.sort()
a = {a[0]: b[0], a[1]: b[1], a[2]: b[2], a[3]: b[3], a[4]: b[4]}
print(a)
