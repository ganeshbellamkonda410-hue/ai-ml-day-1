seconds = int(input("Seconds: "))

hours = seconds // 3600
seconds = seconds % 3600

minutes = seconds // 60
seconds = seconds % 60

print(hours, "Hour")
print(minutes, "Minute")
print(seconds, "Second")