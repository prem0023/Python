***
here we perform some operation and if the return is an error then how we can escape from it and give the valid output so that
user can understand the problem.

***


a = int(input("Enter an integer: "))
b = int(input("Enter another integer: "))

try:
    print("Resource open")
    print(a/b)
    k = int(input("Enter a number: "))
    print(k)

except ValueError as e:
    print("Invalid input, ", e)

except Exception as e:
    print("Invalid operation, ", e)

finally:
    print("Resource close")

print("Bye")
