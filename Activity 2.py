try:
    num1, num2 = eval(input("Etner 2 numbers, separated with a comma: "))
    result = num1/num2
    print("Result is", result)
except ZeroDivisionError:
    print ("Division by zero is error!")
except SyntaxError:
    print ("Missing Comma, Enter numebr separated by a comma")
except:
    print ("Wrong input")
else:
    print("No exceptions")
finally:
    print("This will execute no matter what!")