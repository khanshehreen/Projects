from random import randint;

n=input("Do you want to roll the dice? ")
while n== "yes":
	print("Dice is rolling ...")
	num=randint(1,6)
	print("Your number is",num)
	if num==6:
		print("Yayiee you got !! ")

	n=input("Do you want to roll the dice again? ")
	if n=="yes":
		continue