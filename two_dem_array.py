rows = int(input("Input number of rows: "))
columns = int(input("Input number of columns: "))
res = []

for i in range(rows):
    row = []
    for j in range(columns):
        row.append(i*j)
    res.append(row)
print(res)