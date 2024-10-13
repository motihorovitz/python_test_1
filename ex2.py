a = 0
sum_u = 0
sum_u_u = 0
num_1 = int(input("plies enter one number: "))
num_2 = int(input("plies enter two number: "))

while num_1 != -num_2 or num_2 != -num_1:
    a += 2
    sum_u += num_1 + num_2
    if num_1 == num_2:
        sum_u_u += 1

    num_1 = int(input("plies enter one number: "))
    num_2 = int(input("plies enter two number: "))
a += 2
sum_u += num_1 + num_2

print(f"כמה מספרים נקלטו.{a}")
print(f"סכום של כל המספרים החיוביים שנקלטו.  {sum_u}")
print(f"כמה זוגות של מספרים שווים נקלטו.  {sum_u_u}")