def listdo(spam):
    result = ' '
    for i in range(len(spam)-1):
        result = result + spam[i] + ','
    result = result + 'and ' + spam[-1]
    print(result)


spam = ['apples', 'bananas', 'tofu', 'cats']
listdo(spam)