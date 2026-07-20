salary = float(input("Enter Basic Salary: "))

hra = salary * 20 / 100
da = salary * 10 / 100

gross = salary + hra + da

print("HRA =", hra)
print("DA =", da)
print("Gross Salary =", gross)