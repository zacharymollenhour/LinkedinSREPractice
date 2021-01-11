#Sum to One with Recursion
def sum_to_one(n):
    sum = 0
    #Base Case
    if n == 1:
        return n
    else:
        print("Recursing with input: {0}".format(n))
        return n + sum_to_one(n-1)
print(sum_to_one(7))

#Recursion and Big O
#Factorial function that given a positive integer as input, 
#returns the product of every integer from 1 up to the input
def factorial(n):
  if n < 2:
    return n
  else:
    return n * factorial(n-1)

print(factorial(12))

#No Nested Lists Anymore, I want them to turn flat
#Flatten function that removes nested lists within a list
#But keeps the values contained
# define flatten() below...
def flatten(my_list):
  result = []
  for element in my_list:
    if isinstance(element, list):
      print("List found!")
      flat_list = flatten(element)
      result += flat_list
    if not isinstance(element,list):
        result.append(element)
  return result

### reserve for testing...
planets = ['mercury', 'venus', ['earth'], 'mars', [['jupiter', 'saturn']], 'uranus', ['neptune', 'pluto']]
print(flatten(planets))