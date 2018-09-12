student = {'name':'John', 'age':25, 'courses':['Math', 'CpomSi']}
print(student)
print(student['name'])
print(student['courses'])
#print(student['phone']) Gives an error
print(student.get('name'))
print(student.get('phone'))
print(student.get('phone','Not Found'))
student['phone'] = '555-555'
print(student.get('phone','Not Found'))
student['name'] = 'Jane'
print(student)
#The name replaced the first name (Up)
student = {'name':'John', 'age':25, 'courses':['Math', 'CpomSi']}
print(student)
student.update({'name':'Jane','age':26,'phone':'555-5555'})
print(student)
del student['age']
print(student)
student = {'name':'John', 'age':25, 'courses':['Math', 'CpomSi']}
print(student)
age = student.pop('age')
print(student)
print(age)
print(len(student))
student = {'name':'John', 'age':25, 'courses':['Math', 'CpomSi']}
print(len(student))
print(student.keys())
print(student.values())
print(student.items())
student = {'name':'John', 'age':25, 'courses':['Math', 'CpomSi']}
for key in student:
    print(key)
for key, values in student.items():
    print(key, values)
