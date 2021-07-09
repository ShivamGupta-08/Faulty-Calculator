print("Your operator")
Operator = input()
print("Your first number")
first = int(input())
print("Your second number")
sec = int(input())
if Operator == "+" :
    ans = first + sec
elif Operator == "-":
    ans = first - sec
elif Operator == "*":
    ans = first * sec
elif  Operator == "/":
    ans = first / sec

if ans == 45 * 3:
    print("Your ans = 555")
elif ans == 56+9:
    print("Your ans = 77")
elif ans==56/6:
    print("Your ans = 4")
else:print("Your ans",ans)
