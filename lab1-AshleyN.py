# --------------------------------------------------------
# Lab 1: Getting Started with Python
# CIS 103: Introduction to Programming
# Instructor: Md Ali
# Student Name: Ashley Nunez
# Date: 8/30/24
# Description: First Python Script
# This script prints a greeting message to the user.
# --------------------------------------------------------

#the following line of code prints a greeting message
print("Hello, Welcome to CIS 103!")

#Part 3: Exploring Python Variables and Data Types
#this script prints a personalized greeting message
#and demonstrates the use of the variables and basic data types
#--------------------------------------------------------

#Get the user's name (string) and age(integer)
name=input("enter your name:")
age=int(input("Enter your age:"))

#Calculate the year the user was born
current_year=2024
birth_year=current_year-age

#Print a personalized greeting massage
print(f"Hello,{name}! You were born in {birth_year}")