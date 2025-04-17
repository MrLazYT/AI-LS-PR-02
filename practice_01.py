import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Name": ["Alice", "Bob", "Charlie", "Diana"],
    "Age": [25, 30, 35, 40],
    "Salary": [50000, 60000, 70000, 80000],
    "Experience": [1, 3, 5, 7]
}

df = pd.DataFrame(data)

average_salary = df["Salary"].mean()
std_salary = df["Salary"].std()
min_age = df["Age"].min()
max_age = df["Age"].max()

print(f"Average salary: {average_salary}")
print(f"Salary standard deviacion: {std_salary}")
print(f"Minimal age: {min_age}")
print(f"Maximum age: {max_age}")

plt.xlabel("Salary")
plt.ylabel("Age")
plt.title("Salary vs Age")
plt.plot([df["Salary"].min(), df["Salary"].max()], [df["Age"].min(), df["Age"].max()], color="red")
plt.show()