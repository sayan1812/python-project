import csv
with open("Department.csv",mode="w") as csvfile:
    fieldnames=['DEPARTMENT ID','DEPARTMENT NAME','LIST OF BATCH'] 
    writer=csv.DictWriter(csvfile,fieldnames=fieldnames)
    writer.writeheader() 
    writer.writerow({"DEPARTMENT ID":"CSE","DEPARTMENT NAME":"COMPUTER SCIENCE AND ENGINEERING",
    "LIST OF BATCH":"CSE22" })
    writer.writerow({"DEPARTMENT ID":"CSE","DEPARTMENT NAME":"COMPUTER SCIENCE AND ENGINEERING",
    "LIST OF BATCH":"CSE22" })
    writer.writerow({"DEPARTMENT ID":"CSE","DEPARTMENT NAME":"COMPUTER SCIENCE AND ENGINEERING",
    "LIST OF BATCH":"CSE22" })
    writer.writerow({"DEPARTMENT ID":"ECE","DEPARTMENT NAME":"ELECTRONICS AND COMMUNICATION ENGINEERING",
    "LIST OF BATCH":"ECE22" })
    writer.writerow({"DEPARTMENT ID":"ECE","DEPARTMENT NAME":"ELECTRONICS AND COMMUNICATION ENGINEERING",
    "LIST OF BATCH":"ECE22" })
    writer.writerow({"DEPARTMENT ID":"ECE","DEPARTMENT NAME":"ELECTRONICS AND COMMUNICATION ENGINEERING",
    "LIST OF BATCH":"ECE22" })
