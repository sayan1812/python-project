import csv
with open("Student.csv",mode="w") as csvfile:
    fieldnames=['Student id','NAME','Roll no','Batch name'] 
    writer=csv.DictWriter(csvfile,fieldnames=fieldnames)
    writer.writeheader() 
    writer.writerow({"Student id":"CSE2201","NAME":"RAM ROY","Roll no":"1",
    "Batch name":"CSE22" })
    writer.writerow({"Student id":"CSE2202","NAME":"SHYAM MALAKAR","Roll no":"2",
    "Batch name":"CSE22" })
    writer.writerow({"Student id":"CSE2203","NAME":"DEEP HALDER","Roll no":"3",
    "Batch name":"CSE22" })
    writer.writerow({"Student id":"CSE2204","NAME":"DIPALI DEB","Roll no":"4",
    "Batch name":"CSE22" })
    writer.writerow({"Student id":"CSE2205","NAME":"RAJA BISWAS","Roll no":"5",
    "Batch name":"CSE22" })
    writer.writerow({"Student id":"ECE2201","NAME":"SAYAN HALDER","Roll no":"6",
    "Batch name":"ECE22" })
    writer.writerow({"Student id":"ECE2202","NAME":"ALIVIA BANERJEE","Roll no":"7",
    "Batch name":"ECE22" })
    writer.writerow({"Student id":"ECE2203","NAME":"DEEPA MALAKER","Roll no":"8",
    "Batch name":"ECE22" })
