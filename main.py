from os import system
from time import sleep
t = 1
system('cls')
print("Starting...")
sleep(t)

print("Reading Students List...")
sleep(t)
f = open('st_list.txt')
student_list = f.read().splitlines()
while '' in student_list:
    student_list.remove('')
print("Successfully Read", len(student_list), 'Students!!')
sleep(t+1)

print("Creating Projects List...")
sleep(t)
projects_list = [x for x in range(1, 14)]
projects_list *= 3 # each project can be used by 3 people

from random import randint
# we have some students with no due project, adding more random project for them (43 > 13 * 3 = 39):
while len(projects_list) != len(student_list): 
    projects_list.append(randint(1, 13))
print("Successfully Created", len(projects_list), 'Projects!!')
sleep(t+1)

print('-----------------------------')
print("Creating Projects-to-Student List...")
sleep(t)
projects_to_student = {x:[] for x in range(1, 14)}

print("Now Let's Assign...")
sleep(t)
# assigning projects to students
while student_list or projects_list:
    random_student = student_list.pop(randint(0, len(student_list)-1))
    random_project = projects_list.pop(randint(0, len(projects_list)-1))
    projects_to_student[random_project].append(random_student)
    print(43 - len(student_list), ': Student:', random_student, 'got:', random_project)
    sleep(t)
print('Finished!')
sleep(t)

print('-----------------------------')
print('The Final Resault is as follows:')
sleep(t)
for i in projects_to_student.items():
    print(i)
    sleep(1/4)
sleep(t)
print('All done!! Good Luck!')