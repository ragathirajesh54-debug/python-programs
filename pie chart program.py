import matplotlib.pyplot as plt

names = []
values = []

n = int(input("Enni items kavali? : "))

for i in range(n):
    name = input(f"{i+1} item name enter cheyandi: ")
    value = int(input(f"{name} value enter cheyandi: "))
    names.append(name)
    values.append(value)

plt.pie(values, labels=names, autopct="%1.1f%%")
plt.title("Pie Chart (User Input)")

plt.show()
