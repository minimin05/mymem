work_hours = int(input("Enter number of hours worked: "))
pay_rate = int(input("pay rate: "))

if work_hours > 40:
    gross_pay = ((work_hours - 40) *1.5*pay_rate) + (40 * pay_rate)
else:
    gross_pay = (work_hours * pay_rate)

print("Gross pay: ", gross_pay)

