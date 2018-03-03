click("1520046446125.png")
wait("1520046700961.png")
type("Anderson")
click("1520046831593.png")
wait("1520046720138.png")
type("Avenida dos Pioneiros")
click("1520048491462.png")
click("1520048461952.png")


import csv

with open("C:\\Apps\\file.csv") as csvfile:
    readCSV = csv.reader(csvfile, delimiter=",")
    for row in readCSV:
        print(row)
        print(row[0])
        print(row[0],row[1],row[2],row[3])