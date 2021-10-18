weight = int(input("Enter Your Weight: "))
height = int(input("Enter Your Height: "))

bmi = weight / (height * height)
convert = bmi * 10000


print(round(convert, 2))
