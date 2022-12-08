number = int(input("Type a number: "))

list1 = []

for i in range(1,11):
    list1.append(i*number)

print(f"\n time tables: \n{list1}")