try:
    num=int(input("Enter numerator: "))
    den=int(input("Enter denominator: "))
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Please enter valid integers")
else:
    print(num/den)
finally:
    print("program executed")