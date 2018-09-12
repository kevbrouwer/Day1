courses = ['History', 'Math', 'Physics','CompSci']
print(courses)
print(len(courses))
print  (courses[0])
print  (courses[3])
print  (courses[-2])
print  (courses[0:2])
print  (courses[:2])
print  (courses[2:])
courses.append('Art')
print(courses)
courses.insert(1,'Art')
print(courses)
Courses_2 = ['Art','Education']
courses.insert(0,Courses_2)
print(courses)
courses = ['History', 'Math', 'Physics','CompSci']
courses.extend(Courses_2)
print(courses)
courses = ['History', 'Math', 'Physics','CompSci']
courses.remove('Math')
print(courses)
courses.pop()
print(courses)
courses = ['History', 'Math', 'Physics','CompSci']
courses.pop()
popped = courses.pop()
courses = ['History', 'Math', 'Physics','CompSci']
print(courses)
courses.pop()
print(courses)
courses.pop()
popped = courses.pop()
print(popped)
courses = ['History', 'Math', 'Physics','CompSci']
courses.reverse()
print(courses)
courses = ['History', 'Math', 'Physics','CompSci']
courses.sort()
num = [0,1,4,6,7,4,3,5,6,9]
print(courses)
num.sort()
print(num)
courses = ['History', 'Math', 'Physics','CompSci']
courses.reverse()
print(courses)
courses = ['History', 'Math', 'Physics','CompSci']
courses.sort(reverse=True)
print(courses)
num = [0,1,4,6,7,4,3,5,6,9]
num.sort(reverse=True)
print(num)
sorted(courses)
print(courses)
sorted_courses = sorted(courses)
print(sorted_courses)
print(min(num))
print(max(num))
print(sum(num))
print(courses.index('CompSci'))
print('art'in courses)
print('Math'in courses)
print('Ma'in courses)
courses = ['History', 'Math', 'Physics','CompSci']
for item in courses:
    print(item)
for index, item in enumerate(courses):
    print(index,item)
for index, item in enumerate(courses, start=1):
    print(index,item)
courses_str = ', '.join(courses)
print(courses_str)
new_list = courses_str.split(', ')
print(new_list)
End = '________________________________________________'
print(End)
#Mutable
list_1 = ['History', 'Math', 'Physics','CompSci']
list_2 = list_1
print(list_1)
print(list_2)
list_1[0]='Art'
print(list_1)
print(list_2)
#Imutable
tuple_1 = ('History', 'Math', 'Physics','CompSci')
tuple_2 = tuple_1
print(tuple_1)
print(tuple_2)


#Sets
cs_courses = {'History', 'Math', 'Physics','CompSci'}
print(cs_courses)
cs_courses = {'History', 'Math', 'Physics','CompSci','Math'}
print(cs_courses)
cs_courses = {'History', 'Math', 'Physics','CompSci'}
print('Math' in cs_courses)
cs_courses = {'History', 'Math', 'Physics','CompSci'}
art_courses = {'History', 'Math', 'Art','Design'}
print(cs_courses.intersection(art_courses))
print(cs_courses.difference(art_courses))
print(cs_courses.union(art_courses))

# Empty list
empty_list = []
empty_list = list()

# Empty Tuples
empty_tuple = ()
empty_tuple = tuple()

# Empty Set
empty_set = {} # this is wrong. Its a dictionary
empty_set = set()
