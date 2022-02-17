import numbers


first_name = 'Matt'
print(first_name)

last_name = 'Muchnok'
print(last_name)

# print(f"Hello, {first_name}.")

age = 33 # int
bank_account = 234.53 # float
loves_code = True # boolean

# age = 'thirty three'
# print(age)
print(type(age))

if age >= 18:
    print('I am an adult!')
elif age >= 13:
    print('I am a teen.')
else:
    print('I am a child.')

numbers = [1,2,3,4,5,6,7,8,9,10]

for number in numbers:
    print(number)

my_cats = ['jake', 'buddy', 'gogi', 'macy']

for cat in my_cats:
    print(cat.capitalize())

open_file = open('FinalGrades.csv')

for row in open_file:
    print(row)

for row in open_file:
    row = row.split(',')
    for value in row:
        if value.startwith('J'):
            print(value)

open_file.close()