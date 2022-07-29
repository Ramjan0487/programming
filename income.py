# Write a function to Calculate income tax for the given income by adhering to the below rules
#10000*0% + 10000*10%  + 25000*20% = 6000.
# income = 45000
# tax_payable = 0
# print("Given income", income)

# if income <= 10000:
#     tax_payable = 0
# elif income <= 20000:
#     # no tax on first 10,000
#     x = income - 10000
#     # 10% tax
#     tax_payable = x * 10 / 100
# else:
#     # first 10,000
#     tax_payable = 0
#     # next 10,000 10% tax
#     tax_payable = 10000 * 10 / 100
#     # remaining 20%tax
#     tax_payable += (income - 20000) * 20 / 100
# print("Total tax to pay is", tax_payable)


# income = int(input('What is your income? '))
# if income <= 10_000:
#     print('You have zero tax')
# elif 10_000 < income <= 20_000:
#     income_2 = (income - 10_000)*0.1
#     print(f"Your tax amount to be paid is ${income_2}")
# elif income > 20_000:
#     income_3_1 = ((income - 10_000)*0.1)
#     income_3_2 = ((income - 20_000)*0.2)
#     income_3 = income_3_1 + income_3_2
#     print(f"Your tax amount to be paid is ${income_3}")

# income = 45000
# tax_payable = 0
# print("Given income", income)

# if income <= 10000:
#     tax_payable = 0
# elif income <= 20000:
#     # no tax on first 10,000
#     x = income - 10000
#     # 10% tax
#     tax_payable = x * 10 / 100
# else:
#     # first 10,000
#     tax_payable = 0

#     # next 10,000 10% tax
#     tax_payable = 10000 * 10 / 100

#     # remaining 20%tax
#     tax_payable += (income - 20000) * 20 / 100

# print("Total tax to pay is", tax_payable)

income = int(input('What is your income? '))
if income <= 10_000:
    print('You have zero tax')
elif 10_000 < income <= 20_000:
    income_2 = (income - 10_000)*0.1
    print("Your tax amount to be paid is:",income_2)
elif income > 20_000:
    income_3_1 = ((income - 10_000)*0.1)
    income_3_2 = ((income - 20_000)*0.2)
    income_3 = income_3_1 + income_3_2
    print("Your Tax Amount to be paid is:",income_3)
    #print("Your tax amount to be paid is:",income_3")
