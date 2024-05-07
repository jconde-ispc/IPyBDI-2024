name = input("What is your name? ")
# Out: What is your name? Bob
print(name)
# Out: Bob

while True:
    try:
        x = int(input('Enter a number: '))
        break
    except ValueError:
        print('This is not a number, try again.')

# Out: Write a number: 10
x / 2
# Out: TypeError: unsupported operand type(s) for /: 'str' and 'int'
print(float(x) / 2)
# Out: 5.0