import csv
with open("Batch.csv",mode="w") as csvfile:
    fieldnames=['BATCH ID','BATCH NAME','DEPARTMENT NAME','LIST OF THE COURSE',
    'LIST OF THE STUDENT ID'] 
    writer=csv.DictWriter(csvfile,fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({"BATCH ID":"CSE22","BATCH NAME":"CSE 2022-26","DEPARTMENT NAME":"CSE",
    "LIST OF THE COURSE":"C001-C002","LIST OF THE STUDENT ID":"CSE2201"})
    writer.writerow({"BATCH ID":"CSE21","BATCH NAME":"CSE 2021-25","DEPARTMENT NAME":"CSE",
    "LIST OF THE COURSE":"C001-C002","LIST OF THE STUDENT ID":"CSE2101"})
    writer.writerow({"BATCH ID":"ECE22","BATCH NAME":"ECE 2022-26","DEPARTMENT NAME":"ECE",
    "LIST OF THE COURSE":"C002","LIST OF THE STUDENT ID":"ECE2201:ECE2202"})
    