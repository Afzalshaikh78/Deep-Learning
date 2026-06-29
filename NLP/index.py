




def greet(name):
  print(f'Hello {name}')



# greet('DeepLearning')



def is_even(number):
  if number % 2 == 0:
    return True
  else:
    return False
    
# print(is_even(4))


# def introduce(name,age,city):
#   print(f'Hi {name}, you are {age} years old and living in {city}')
# introduce('DeepLearning',25,'Bangalore')



fruits = ['apple','banana','orange']

print()


numbers = [1,2,3,4,5]

numbers.append(6)

print(numbers)



students = [
  {
    'name': 'DeepLearning',
    'age': 25,
    'city': 'Bangalore'
  },
  {
    'name': 'DeepLearning',
    'age': 25,
    'city': 'Bangalore'
  }
  
]

# for student in students:
#   for key,value in student.items():
#     print(key,value)
#   print('---')


for i in range(5,20,2):
  print(i)

name = 'DeepLearning'

for letter in name:
  print(letter)




names = ['Afzal','Mohammad','Rahul']


index = 0

for name in names:
  print(index,name)
  index += 1


for index,name in enumerate(names):
  print(index,name)


# numbers = []

# for i in range(10):
#   numbers.append(i)

# print(numbers)



# numbers = [i for i in range(10)]
# print(numbers)

# squares = [i**2 for i in range(10)]
# print(squares)

# evens = [i for i in range(10) if i % 2 == 0]
# print(evens)

# odds = [i for i in range(10) if i % 2 != 0]
# print(odds)

# words = ['python','ai','bert']

# upper = [word.upper() for word in words]
# print(upper)


numbers = [1,-2,5,-4,3]


result = [x if x>0 else 0 for x in numbers]
print(result)