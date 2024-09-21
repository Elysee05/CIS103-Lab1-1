# CIS 103: Introduction to Programming
# Assignment 03: "Coding practice"
# Instructor: Md Ali
# Date: 09/20/2024
#Coding exercises
#Creating a list of fruits
fruits = ['apple', 'banana', 'orange', 'grape']
print(fruits)
#removing banana
fruits.remove('banana')
print(fruits)
#adding strawberry
fruits.append('strawberry')
print(fruits)
#creating a Tuples called colors
colors = ('red', 'green', 'blue', 'yellow')
print(colors)
#accessing elements in the tuple
print(colors[0::3])
#changing element 2 in the tuple
#colors.remove('blue')
#print(colors) - returns the following error because tuples can be immutable
#File
#"C:\Users\17736\PycharmProjects\sample00\Assignment 3.py", line
#21, in < module >
#creating a dictionary called Students_scores
students_scores = {"John":85, "Emma":92, "Sophia":78, "James":89}
print(students_scores)
#accesing Emma name and score
print("Emma's score", students_scores["Emma"])
#adding new student to the dictionary
students_scores["Oliver"] = 82
print(students_scores)
#updating a students score in the dictionary
students_scores["Sophia"]=82
print(students_scores)