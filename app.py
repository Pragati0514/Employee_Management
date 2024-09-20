# 2nd Task
def Add():
    Eid=input("emp id :")
    Ename=input("emp name :")
    Eadd=input("emp address :")
    Enum=input("emp contact no :")  
    fp=open("Emp_data.txt","a")
    fp.write(f"{Eid}\t")
    fp.write(f"{Ename}\t")
    fp.write(f"{Eadd}\t")
    fp.write(f"{Enum}\n")
    fp.close()
    print("Data added Successfully")
    print("---------------------------------------")
# 3rd Task
def Display():
    fp=open("Emp_data.txt","r")
    #1.read()
    #2.readlines()
    #3.readline()  

    # read()-----returns output as a string
    '''all=fp.read()
    print(all)
    print(type(all))
    count=0
    for x in all:
        count=count+1
    print(f"Total no of employees are {count}")'''

    #readlines()----returns output as a list
    all=fp.readlines()
    #print(all)
    count=0
    for x in all:
        count=count+1
        print(x,end="")
    print(f"Total no of employees are {count}")

    # readline()------reads a line of the file and returns in the form of string
    '''all=fp.readline()
    print(all)
    print(type(all))
    count=0
    for x in all:
        count=count+1
        print(x,end="")
    print(f"Total no of employees are {count}")'''
    fp.close()
    print("Data displayed Successfully")
    print("---------------------------------------")
# 4th Task
def Search():
    id=input("Enter the id to be searched from the file:  ")
    flag=False 
    with open("Emp_data.txt","r")as fp:
        all=fp.readlines() 
        for data in all:
            d=data.split("\t")
            if(d[0]==id):
                print(data,end="") 
                flag=True
                print("Employee has been searched successfully")
                print("------------------------------------------")
        if not flag:
                print("Data is not found")       
# 5th Task
def Delete():
    id=input("Enter the id to be deleted in the file:  ")
    flag=False
    with open("Emp_data.txt","r")as fp:
        all=fp.readlines()
    with open("Emp_data.txt","w")as fp:
        for data in all:
            d=data.split("\t")
            if(d[0]==id):
                flag=True
                print("Record deleted successfully")
                print("---------------------------------")
            else:
                fp.writelines(data)
        if not flag:
            print("Data is not found")
# 6th Task
def Update():
    id=input("Enter the id to be updated in the file:  ")
    flag=False
    with open("Emp_data.txt","r")as fp:
        all=fp.readlines()
    with open("Emp_data.txt","w")as fp:
        for data in all:
            d=data.split("\t")
            if(d[0]==id):
                nn=input("Name: ")
                na=input("Address: ")
                nc=input("Contact no: ")
                fp.writelines(f"{d[0]}\t {nn}\t {na}\t {nc}\n")
                flag=True
                print("Record updated successfully")
                print("---------------------------------")
            else:
                fp.writelines(data)
        if not flag:
            print("Data is not found")
# First Task: Create user menu
print("welcome Admin!!! You are in Employee management portal")
print("1. Add new record") 
print("2. Display records")
print("3. Search record")  
print("4. Delete record")
print("5. Update Record")
print("6. Exit from application")
while True:
    ch=int(input("which action do you want to perform: "))
    if ch==1:
        Add()
    elif(ch==2):
        Display()       
    elif(ch==3):
        Search()      
    elif(ch==4):
        Delete()
    elif(ch==5):
        Update()
    elif ch==6:
        break         
    else:
        print("Enter correct input")         