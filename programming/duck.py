#A school decided to replace the desks in three classrooms. each desks sits two students. Given the number of students
#in each class , print the smallest possible number of desks to be purchased.
#the program should read three integers:the number of sudents in each of the three classes a,b and c respectvely.
no_student_class1=int(input('enter the number of students in first class '))
no_student_class2=int(input('enter the number of students in second class '))
no_student_class3=int(input('enter the number of students in third class '))
desks_class1=(no_student_class1//2)
print(f"the required number of desk for first class is {desks_class1}")
desks_class2=(no_student_class2//2)
print(f"the required number of desks for second class is {desks_class2}")
desks_class3=(no_student_class3//2)
print(f'the required number of desk for third class is {desks_class3}')
remain_class1=(no_student_class1 % 2)
print(f"remaining desk for second class is {remain_class1}")
remain_class2=(no_student_class2 % 2)
print(f'the remaining number of desk for second class is {remain_class2}')
remain_class3=(no_student_class3 % 2)
print(f'the remaining desk for third class is {remain_class3}')
total_desk=desks_class1+ desks_class2 + desks_class3 + remain_class1 +remain_class2 + remain_class3
print(f"total number of desks that can be purchased is {total_desk}")

