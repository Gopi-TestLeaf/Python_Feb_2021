import csv

with open('text.csv', 'w', newline="") as file_obj:
    write = csv.writer(file_obj)
    head = ["f_Name", "l_Name", "email"]
    write.writerow(head)

    data = [
        ['Gopinath', 'Jayakumar', 'gopithri@gmail.com'],
        ['Sarath', 'M', 'sarath@gmail.com'],
        ['Balaji', 'M', 'balaji@gmail.com']
    ]

    write.writerows(data)

