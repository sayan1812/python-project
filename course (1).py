import csv
with open("Course.csv",mode="w") as csvfile:
    fieldnames=['COURSE ID','COURSE NAME','MARKS OBTAINED (student id:marks-student id:marks-….)'] 
    writer=csv.DictWriter(csvfile,fieldnames=fieldnames)
    writer.writeheader() 
    writer.writerow({"COURSE ID":"C001","COURSE NAME":"PYTHON PROGRAMMING",
    "MARKS OBTAINED (student id:marks-student id:marks-….)":"CSE2201:95-CSE2202:79-CSE2204:88" })
    writer.writerow({"COURSE ID":"C002","COURSE NAME":"PHYSICS",
    "MARKS OBTAINED (student id:marks-student id:marks-….)":"CSE2203:94-CSE2205:79-ECE2201:84" })
    writer.writerow({"COURSE ID":"C003","COURSE NAME":"MATH",
    "MARKS OBTAINED (student id:marks-student id:marks-….)":"ECE2202:99-ECE2203:70-CSE2201:70" })
