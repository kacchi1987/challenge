import csv

list = [["トップガン", "Risky Business", "Minority Report"], ["Titanic", "The Revenant", "Inception"], ["Training Day", "Man on Fire", "Flight"]]

with open("9-4.csv", "w", newline='', encoding="utf-8") as f:
    w = csv.writer(f, delimiter=",")
    w.writerow(list[0])
    w.writerow(list[1])
    w.writerow(list[2])
