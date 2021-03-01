import csv

# with open('text.csv') as f:
#     data = csv.reader(f)
#     for row in data: # rows
#         for column in row: # column
#             print(column)
#         print("    ")


# returns list
# with open('text.csv') as f:
#     data = csv.reader(f)
#     for row in data:
#         print(row[0].ljust(15), row[1].ljust(15), row[2])


with open('text.csv') as f:
    data = csv.DictReader(f)
    for row in data:
        print(row['f_Name'].ljust(15), row['l_Name'].ljust(15), row['email'])









