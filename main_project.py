import mysql.connector
from datetime import datetime
#database creation
mydb = mysql.connector.connect(host ="localhost", user = "root", password = "lucknow")
mycursor = mydb.cursor()
mycursor.execute('create database if not exists Covid_Management')
mycursor.execute('use Covid_Management')
mycursor.execute('create table if not exists staff(sno varchar(25) not null, name varchar(25) not null,\
     age varchar(25) not null,gender char(1) not null, post varchar(25) not null,salary varchar(25) not null)')
mycursor.execute('create table if not exists patients(sno varchar(25) not null, name varchar(25) not null,\
     age varchar(25) not null,gender char(1) not null, date date not null)')
mycursor.execute('create table if not exists login(admin varchar(25) not null, password varchar(25) not null)')
mycursor.execute('create table if not exists sno(patient varchar(25) not null, staff varchar(25) not null)')
mycursor.execute('select* from sno')
z = 0
for i in mycursor:
    z = 1
if z == 0:
    mycursor.execute('insert into sno values("0","0")')
mydb.commit()
j = 0
mycursor.execute("select * from login")
for i in mycursor:
    j = 1
if j==0:
    mycursor.execute("insert into login values('Admin', 'ng' )")
    mydb.commit()
loop1 = "y"
while (loop1 == "y"):
    print("______________________________")
    print("1. Admin")
    print("2. Patient")
    print("3. Exit")
    print("______________________________")
    ch1 = int(input("Enter choice:"))
    if ch1 == 1:
        password_ = '12345678'
        pas = input('Enter password(12345678) :')
        mycursor.execute("select * from login")
        for i in mycursor:
            username,password = i
        if (pas == password_):
            loop2 = "n"
            while (loop2 == "n" ):
                print("______________________________")
                print("1. Add Patient")
                print("2. Add Staff")
                print("3. Display Patient's Records")
                print("4. Display Staff Records")
                print("5. View time")
                print("6. Remove Patient")
                print("7. Remove Staff")
                print("8. Logout")
                print("______________________________")
                ch2 = int(input("Enter Choice: "))
                if ch2==1:
                    loop3 = "y"
                    while loop3 == "y" :
                        name = input('Enter patients name: ')
                        age = input("Enter age: ")
                        gender=input('Enter gender(m/f/o): ')
                        date = (input("Enter Date of testing positive (yyyy-mm-dd): "))
                        mycursor.execute('select * from sno')
                        for i in mycursor:
                            patient,staff = i
                            patient = int(patient)+1
                        mycursor.execute("insert into patients values('"+str(patient)+"','"+name+"','"+age+"','"+gender+"','"+date+"')")
                        mycursor.execute("update sno set patient = '"+str(patient)+"'")
                        mydb.commit() 
                        print("data of Patient has been saved successfully")
                        mycursor.execute("select* from patients")
                        t = 0
                        for i in mycursor:
                            t+=1
                            t_id1,name1,age1,gender1,date1 = i
                        print(f"Active Corona infected patients : {patient}")
                        print(f"Active Corona Cases: {t}")
                        print(f"This patient with id{t_id1} will be in Quarantine for 14 days From {date1}")
                        loop3 = input("Do you want to add data of more patients(y/n): ").lower
                    loop2 = input("Do you want to logout?(y/n): ")
                elif ch2==2:
                    loop3 = "y"
                    while loop3 == "y" :
                        name = input("Enter Name of New Staff Memeber: ")
                        age = input('age: ')
                        gender=input('Enter gender(m/f/o): ')
                        post = input("Enter post: ")
                        salary =(input("Enter Salary: "))
                        mycursor.execute('select * from sno')
                        for i in mycursor:
                            patient,staff = i
                            staff = int(staff)+1
                        mycursor.execute("insert into patients values('"+str(patient)+"','"+name+"','"+age+"','"+gender+"','"+date+"')")
                        mycursor.execute("update sno set staff='"+str(staff)+"'")
                        mydb.commit()
                        print(f"staff with id {staff} has been saved successfully")
                        mycursor.execute("Select * from staff")
                        t = 0
                        for i in mycursor:
                            t+=1
                        print(f"Active Staff Members: {t}")
                        loop3 = input("Do you wnat to enter More Staff People?(y/n): ")
                    loop2 = input("Do you want to logout?(y/n): ")
                elif ch2==3:
                    idd = input("Enter patient's ID: ")
                    t_id2,name2,age2,gender2,date2 = ["","","","","",]
                    mycursor.execute("select * from patients where sno = '"+idd+"' ")
                    for i in mycursor:
                        t_id2,name2,age2,gender2,date2 = i
                    print("|ID|NAME|AGE|GENDER|CORONA DETECTED DATE|")
                    print(f"|{t_id2}|{name2}|{age2}|{gender2}|{date2}|")
                elif ch2 == 4:
                    idd = input("Enter Staff Member's ID: ")
                    t_id3,name3,age3,gender3,post3,salary3 = ["","","","","",""]
                    mycursor.execute("select * from staff where sn0 = '"+idd+"' ")
                    for i in mycursor:
                        t_id3,name3,age3,gender3,post3,salary3 = i
                    print("|ID|NAME|AGE|GENDER|POST|SALARY|")
                    print(f"|{t_id3}|{name3}|{age3}|{gender3}|{salary3}|")
                elif ch2 == 5:
                    now = datetime.now()
 
                    print("now =", now)
                elif ch2==6:
                    loop3 = "y"
                    while loop3 == "y" :
                        idd = input("Enter patient ID: ")
                        mycursor.execute("delete from patients where sno = '"+idd+"'")
                        mydb.commit()
                        print("Patient removed successfully")
                        loop3 = input("Do you want to Remove more Patients?(y/n): ")
                elif ch2==7:
                    loop3 = "y"
                    while loop3 == "y" :
                        idd = input("Enter staff ID: ")
                        mycursor.execute("delete from staff where sno = '"+idd+"'")
                        mydb.commit()
                        print("Staff removed successfully")
                        loop3 = input("Do you want to Remove more Staff?(y/n): ")
                elif ch2 ==8:
                    break
    elif ch1==2:
        print("Welcome to this short test for Covid-19")
        icough = input("Have you been coughing frequently?(y/n): ").lower()
        dry_cough = "n"
        if icough == "y" :
            dry_cough = input("Is it dry cough?(y/n): ").lower()
        sneeze = input("Have you been sneezing frequently?(y/n): ").lower()
        pain = input("Have you been experiencing body pain?(y/n): ").lower()
        weakness = input("Have you been experiencing weakness?(y/n): ").lower()
        mucus = input("Have you been experiencing mucus while coughing and/or otherwise?(y/n): ").lower()
        itemp = int(input("Enter your current body temprature in farahneit: "))
        if itemp<100 :
            temp = "Low"
        else:
            temp = "High"
        breathe = input("Have you been experiencing difficulty while breathing?(y/n): ").lower()
        if 'n' in {dry_cough,sneeze ,pain, weakness,breathe} and temp =='Low':
            print("You are not covid Positive, just rest, do consult a doctor if problem persists")
        elif 'y' in {dry_cough,sneeze ,pain, weakness,breathe} and temp == "High":
            print("Sorry to say, but according to the test results you maybe SUFFERING FROM CORONAVIRUS/COVID-19")
            name = input("Enter name: ")
            age = input("Enter age: ")
            gender = input("Enter gender(m/f/o): ")
            mycursor.execute("select * from sno")
            for i in mycursor:
                patient,staff = i
                patient = int(patient)+1
            mycursor.execute("insert into patients values('"+str(patient)+"','"+name+"','"+age+"','"+gender+"',now())")
            mycursor.execute("update sno set patient = '"+str(patient)+"'")
            mydb.commit()
            print("data of patient has been saved")
            print(f"Total number of CORONA INFECTED PATIENTS: {patient}")
            mycursor.execute("select * from patients")
            t = 0
            for i in mycursor:
                t+=1
            print(f"Active CORONA CASES: {t}")
            mycursor.execute("select * from patients")
            for i in mycursor:
                t_id5,name5,age5,gender5,date5 = i
            print(f"This patient with ID {t_id5} will be in Quarantine for 14 days from {date5}")
        else:
            print("Dont worry.. Its probably just a cold")
    elif ch1 == 3:
        break