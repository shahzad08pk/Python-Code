# Write a program that take a number from user and printout its table

num=input("Enter a number: ")
number=int(num)
for i in range(1,11):
    print(num,'X',i,'=',number*i)
