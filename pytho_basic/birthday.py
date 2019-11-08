birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}

while True:
    print('Enter a name: (blank to quit)')
    name = input()
    if name == '':
        break

    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
    else:
        print('I do not have birthday information for ' + name)
        print('What is their birthday?')
        bday = input()
        birthdays[name] = bday
        print('Birthday database updated.')
        


# Enter a name: (blank to quit)
# Eve
# I do not have birthday information for Eve
# What is their birthday?
# Dec 5
# Birthday database updated.
# Enter a name: (blank to quit)
# Eve
# Dec 5 is the birthday of Eve
# Enter a name: (blank to quit)
