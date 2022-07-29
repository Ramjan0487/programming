# Given two integer numbers return their product only if the product is equal to or lower than 1000, else return their sum.
# number1 = 20
# number2 = 30

# number1 = 40
# number2 = 30
# #python 2.7.15
# num1=int(input("enter no. 1: " ))
# num2=int(input("enter no. 2: "))
# product = num1*num2
# res= (num1+num2) if product > 1000 else product 
# print(res)
num1 =int(input("Enter First Number: "))
num2 =int(input("Enter Second_Number: "))
product = num1 * num2
sum = num1 + num2
if product <= 1000:
    print(product) 
#else:
   #print(sum)

result = product or sum
print("The Sum is =",sum)
print("The Product is =",product)
print("The result is = ", result)

# result = pri_or_sum(50,10)
# print("The result is = ", result)

