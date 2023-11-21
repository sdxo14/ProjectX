name=input("What is your name? ")
print(f"Hi {name}!")
weight=input(f'What is your weight? ')
unit=input(f"Your weight is in Kgs or lbs? ")
if unit.upper() == "KGS":
    print(float(weight)/0.45)
elif unit.upper() == "LBS":
    print(float(weight)*0.45)
else:
    print("Incorrect Input!")
secret_number = 1996
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    password = int(input("Password: "))
    guess_count += 1
    if password == secret_number:
        print("Access Granted.")
        break
else:
    print("Incorrect Answer!Try Again.")