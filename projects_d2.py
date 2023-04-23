# Project Day 2 | 100 Days of Code with Python
# Project Name : Tip Generator

print('Welcome to Tip Generator 1.0')
bill = float(input('What was the total bill? $'))
tip = int(input('What percentage tip would you like to give? 10, 12, or 15? '))
people = int(input('How many people to split the bill? '))
total_tip = bill * (tip/100)
total_bill = bill + total_tip
people_bill = total_bill / people
result = '{:.2f}'.format(people_bill)
final_result = f'Each people should pay: ${result}'
print(final_result)
