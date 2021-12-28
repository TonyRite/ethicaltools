#!/bin/python3
def who_am_i():
	name = "Heath"
	age ="30"
	print("My name is "+ name+ "and age is "+age)
	
who_am_i()


#adding parameters
def add_one_hundred(num):
	print(num + 100)
	
add_one_hundred(100)

#multiple parameters

def add(x,y):
	print(x+y)
	
add(7,7)

def multiply(x,y):
	return x * y
	
print(multiply(7,7))

## boolean functon
bool1 = True
bool2=3*3 == 9
print(bool1,bool2)
print(type(bool1))


#Relational and boolean operators
greater_than = 7>5
print(greater_than)


def drink(money):
	if money >= 2:
		return "you have small cash"
	else:
		return "bye"
print(drink(2))


