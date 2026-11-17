hourlyWage = float(input("Hourly Wage: "))
hoursWorked = float(input("Hours Worked: "))

if hoursWorked > 40:
    checkTotal = (hourlyWage * 40) + ((hoursWorked - 40) * (hourlyWage * 1.5))
    print(f"{checkTotal:.2f}")
elif hoursWorked < 0:
    print("Invalid Input")
else:
    checkTotal = hourlyWage * hoursWorked
    print(f"{checkTotal:.2f}")