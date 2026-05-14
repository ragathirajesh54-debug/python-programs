import matplotlib.pyplot as plt

names = []
values = []

n = int(input("Enni months / items kavali? : "))

for i in range(n):
    name = input(f"{i+1} item name enter cheyandi: ")
    value = int(input(f"{name} value enter cheyandi: "))
    names.append(name)
    values.append(value)

plt.plot(names, values, marker='o')
plt.xlabel("Names / Months")
plt.ylabel("Values")
plt.title("User Input Sales Graph")

plt.show()
