def first_function(str1,str2):
    print(str1)
    print(str2)
first_function("i m a boy", 'i m a girl')
first_function('the thing i got is an apple','other thing is its juice')

def second_function(name,age):
    print('my name is ' + name)
    print('my age is ' + str(age))
second_function('Prem','20')

def third_function(name,age):
    print('my name is ',name)
    print('my age is ' , age)
third_function('Prem','20')

def function(*resource):
    for item in resource:
        print(' this item is', item)
function('book','tabke','bottle')
