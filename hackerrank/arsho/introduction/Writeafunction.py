'''
Title     : Write a function
Subdomain : Introduction
Domain    : Python
Author    : Ahmedur Rahman Shovon
Created   : 15 July 2016
Problem   : https://www.hackerrank.com/challenges/write-a-function/problem
'''
def is_leap(year):
    leap = False
    if (year % 400 == 0):
        leap = True
    elif year % 400 == 0 and year % 100 !=0:
        leap = True
    return leap