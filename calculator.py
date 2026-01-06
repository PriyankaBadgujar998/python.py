num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
choose = input("Enter the operation (+,-,*,%)")
match choose:
 case "+":
        print(num1+num2)
 case "-":
        print(num1-num2)
 case "*":
        print(num1*num2)
 case "%":
        print(num1%num2)       