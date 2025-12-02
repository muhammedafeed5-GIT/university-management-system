name = input("Enter your name: ")
age = int(input("Enter your age: "))
years_left = 100 - age
for i in range(1, 4):
    print(f"Hello {name}, in {i*10} years you'll be {age + i*10} years old.")
print("Years left to reach 100:", years_left)
