import matplotlib.pyplot as plt

names = []
values = []

n = int(input("How many entries? "))

for i in range(n):
    name = input("Enter name: ")
    value = int(input("Enter value: "))
    names.append(name)
    values.append(value)

plt.bar(names, values)
plt.show()
