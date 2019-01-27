employee_file = open("employees.txt","r")
#print(employee_file.readable()) #whether the file can be read
#print(employee_file.read()) #read the whole file
#print(employee_file.readline()) #reads the first line in a file

for employee in employee_file.readlines():
    print(employee)

employee_file.close()

