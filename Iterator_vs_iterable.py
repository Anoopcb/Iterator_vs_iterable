## iterator vs iterables

numbers = [1, 2, 3, 4]## iterables

squares = map(lambda a: a**2, numbers)##iterator

print(squares)
for i in squares:

    print(i)





for i in numbers:

    print(i)
## step call iter function
#nex(iter(numbers))


