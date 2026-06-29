num_1=float(input("enter num_1 :"))
num_2=float(input("enter num_2 :"))

choice = input("enter your choice + - * / %")
if choice == '+':
    print(f'Addition: {num_1 + num_2}')
elif choice == '-':
    print(f'subtraction : {num_1-num_2}')
elif choice == '*':
    print(f'multiplication : {num_1*num_2}')
elif choice == '/':
    print(f'division : {num_1/num_2}')
elif choice == '%':
    print(f'modulas : {num_1%num_2}')
else:
    print("invalid choice")