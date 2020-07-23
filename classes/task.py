# Exception handling
a = input('Enter a number')
try:
    result = int(a) * 5
    print(result)
except Exception as e:
    print(e)
finally:
    print('Re-enter a number')
