import mysql.connector as s
import matplotlib.pyplot as p
from tabulate import tabulate
import random
mycon=s.connect(host="localhost", user="root", passwd="")
if mycon.is_connected:
    print("success")
else:
    print("sorry try again")
#SQL QUERIES FOR TABLE CONSTRUCTION
cursor=mycon.cursor()
cursor.execute("DROP DATABASE IF EXISTS INVESTIGATORY_PROJECT")
cursor.execute("CREATE DATABASE INVESTIGATORY_PROJECT")
cursor.execute("USE INVESTIGATORY_PROJECT")
cursor.execute('CREATE TABLE TOURIST( SLNO INTEGER, NAME VARCHAR(25),NO_OF_PERSON INTEGER,ADDRESSE VARCHAR(72),CONTACT_NO NUMERIC(10),TOUR_PACKAGE VARCHAR(40),TOTAL_FARE INTEGER,VALID_ID_PROOF VARCHAR(25),TRANSPORT VARCHAR(35))')
cursor.execute("CREATE TABLE INTERNATIONAL (TOUR_PACKAGE_CODE CHAR(4),DESTINATION VARCHAR(10), DAYS INTEGER, NIGHTS INTEGER, TOTALPRICE INTEGER)")
cursor.execute("INSERT INTO INTERNATIONAL VALUES('IE04','EUROPE',14,13,92990)")
cursor.execute("INSERT INTO INTERNATIONAL VALUES('IB25','BHUTAN',4,5,42750)")
cursor.execute("INSERT INTO INTERNATIONAL VALUES('IB65','BALI',5,4,34799)")
cursor.execute("INSERT INTO INTERNATIONAL VALUES('ID45','DUBAI',6,5,34999)")
cursor.execute("CREATE TABLE DOMESTIC (TOUR_PACKAGE_CODE VARCHAR(25),DESTINATION VARCHAR(10), DAYS INTEGER, NIGHTS INTEGER, TOTALPRICE INTEGER)")
cursor.execute("INSERT INTO DOMESTIC VALUES('DK76','KERALA',6,5,24715)")
cursor.execute("INSERT INTO DOMESTIC VALUES('DG78','GUJARAT',6,5,27734)")
cursor.execute("INSERT INTO DOMESTIC VALUES('DR23','RAJASTHAN',9,8,51132)")
cursor.execute("INSERT INTO DOMESTIC VALUES('DM56','MUMBAI-GOA',9,8,51132)")
cursor.execute("CREATE TABLE TRAINS(TRAIN_CODE VARCHAR(25),T_NAME VARCHAR(25), T_NO NUMERIC, STARTPOINT VARCHAR(25), ENDPOINT VARCHAR(25),RATE INT)")
cursor.execute("INSERT INTO TRAINS VALUES('DR12','RAJDHANI EXP',12803,'DELHI','HOWRAH',3000)")
cursor.execute("INSERT INTO TRAINS VALUES('DW13','WEST COAST EXP',12343,'AHMEDABAD','BENGALURU',2000)")
cursor.execute("INSERT INTO TRAINS VALUES('DC15','COROMANDEL EXP',15644,'HOWRAH','CHENNAI',3000)")
cursor.execute("INSERT INTO TRAINS VALUES('DR20','RAJHDHANI EXP',12897,'DELHI','KOCHI',3500)")
cursor.execute("INSERT INTO TRAINS VALUES('DS17','SHATAPDI EXP',22398,'LUCKNOW','JAIPUR',3000)")
cursor.execute("CREATE TABLE FLIGHTS_INT (FLIGHT_CODE VARCHAR(25),FLIGHT VARCHAR(25), FROM_ VARCHAR(25), TO_ VARCHAR(25), RATE INTEGER)")
cursor.execute("INSERT INTO FLIGHTS_INT VALUES('IFE10','FLY EMIRATES','DELHI','DUBAI',10273)")
cursor.execute("INSERT INTO FLIGHTS_INT VALUES('II20','INDIGO','DELHI','PARIS',15573)")
cursor.execute("INSERT INTO FLIGHTS_INT VALUES('IV40','VISTARA','DELHI','LONDON',14999)")
cursor.execute("INSERT INTO FLIGHTS_INT VALUES('IAI30','AIR INDIA','MUMBAI','NEWYORK',20599)")
cursor.execute("INSERT INTO FLIGHTS_INT VALUES('IL50','LUFTHANSA','MUMBAI','BANGKOK',6400)")
cursor.execute("CREATE TABLE  FLIGHTS_DOM (FLIGHT_CODE VARCHAR(25),FLIGHT VARCHAR(30), FROM1 VARCHAR(25), TO1 VARCHAR(25), RATE INTEGER)")
cursor.execute("INSERT INTO FLIGHTS_DOM VALUES('DI22','INDIGO','DELHI','MUMBAI',5045)")
cursor.execute("INSERT INTO FLIGHTS_DOM VALUES('DAI39','AIRINDIA','KOLKATA','PANAJI',7500)")
cursor.execute("INSERT INTO FLIGHTS_DOM VALUES('DS16','SPICEJET','KOLKATA','DELHI',6000)")
cursor.execute("INSERT INTO FLIGHTS_DOM VALUES('DV32','VISTARA','DELHI','CHENNAI',8000)")
cursor.execute("INSERT INTO FLIGHTS_DOM VALUES('DG34','GOAIR','MUMBAI','BENGALURU',5500)")
#----------------------------------------------------------------------------------------------------------------------------------------------

print("\t\t\tWELCOME TO GLOBAL TOURS AND TRAVELS")
print("\t\t\t___________________________________")
print("\n")
print("\t\t\tWE ASSURE YOU THE CHEAPEST PRICE")
print("\n\n\n")
print("----------------------TRENDING HOLIDAY DESTINATIONS:--------------------------")
print("Please sign up to enjoy great deals....")
print("\n\n\n")
print('''Our website offers you with
1)Best tour package
2)Destination popularity
3)Amazing iternary
4)Visa and Forex on international trip
5)Airfare or Railfare
6)Affordable luxury Hotel''')
print('\n\n\n')
#SIGNING_UP
name=input("enter your username: ")
while True:                                             
    print('PLEASE ENTER IN LOWERCASE.',end="  ")
    print('THE EMAIL-ID MUST CONTAIN @.')
    email=input("Enter your email id: ")               
    a=0
    upper=0
    for k in range(len(email)):									
       if email[k] == '@':
            a+= 1
       if email[k].isupper():
            upper+=1   
    if a== 1 and upper==0:
        break
    else :
        print('Enter Correctly')
while True:                                                     
    phone1=input("Enter your first mobile number: ")
    x=str(phone1)
    if x.isdigit() and len(x)==10:
        phone1=int(x)
        break
    else:
        print("The no should not contain any alphabets and should only have 10 digits")
        continue
while True:                                                     
    phone2=input("Enter your second mobile number: ")
    x=str(phone2)
    if x.isdigit() and len(x)==10:
        phone1=int(x)
        break
    else:
        print("The no should not contain any alphabets and should only have 10 digits")
        continue
print("\n\n")											
while True:
    print("We are sending you a 5 digit OTP. Use it to login....")
    otp=random.randint(10000,99999)
    print("Your 5 digit otp is",otp)
    print("\n\n")
    password=int(input("Please enter your OTP: "))
    if password!=otp:
        print("you have entered wrong OTP. Please re-enter...")
    else:
        print("Succesfully logged in. Thankyou for signing up.")
        break
    print('Resending the otp') 
#FUNCTION
def view():
   while True:
        print("""
        1.HOLIDAY PACKAGES
        2.FLIGHTS
        3.TRAINS""")
        print("\n\n")
        print("Please choose from above menu bar")        
        while True:                                             
           op=input("Enter your choice:")
           jl=op
           if jl.isdigit() and len(jl)==1 and jl in ["1","2","3"]:
               op=int(jl)
               break
           else:																							8
               print("enter correctly")
               continue 
                
        print("""
        1.INTERNATIONAL
        2.DOMESTIC""")
        while True:                                             
            choice=input("Enter your choice:")
            x=choice
            if x.isdigit() and len(x)==1 and x in ["1","2"]:
                choice=int(x)
                break
            else:
                print("enter correctly")
                continue             
        if op == 1:
            if choice == 1:
               cursor.execute('SELECT * FROM INTERNATIONAL')
               info1 = cursor.fetchall()
               print(tabulate(info1, headers=["TOUR_PACKAGE_CODE","DESTINATION","DAYS","NIGHTS","TOTALPRICE"],tablefmt="psql"))
            else:
                cursor.execute('SELECT * FROM DOMESTIC')
                info2 = cursor.fetchall()
                print(tabulate(info2, headers=["TOUR_PACKAGE_CODE","DESTINATION","DAYS","NIGHTS","TOTALPRICE"],tablefmt="psql"))
        elif op == 2:
            if choice == 1:										
                cursor.execute('SELECT * FROM FLIGHTS_INT')
                info3 = cursor.fetchall()
                print(tabulate(info3,headers=["TOUR_PACKAGE_CODE","FLIGHT","FROM","TO","RATE"],tablefmt="psql"))
            else:
                cursor.execute('SELECT * FROM FLIGHTS_DOM')
                inf04 = cursor.fetchall()
                print(tabulate(inf04,headers=["TOUR_PACKAGE_CODE","FLIGHT","FROM","TO","RATE"],tablefmt="psql"))
        else :
            cursor.execute('SELECT * FROM TRAINS')
            info5 = cursor.fetchall()
            print(tabulate(info5,headers=["TOUR_PACKAGE_CODE","TRAIN NAME","TRAIN NO","FROM","TO","RATE"],tablefmt="psql"))
        print('Do you want to exit y/n?')
        x = input('y or n:')
        if x == 'y' or 'Y':
            break
def registration():
    global no_of_person
    global station
    global select
    global From
    global To
    global net
    d2=0
    no_of_person = int(input('Enter no. of person:'))						
    addresse = input('Enter your addresee:')
    print("\n")
    print("please enter your addhar no, pan no, or anyother valid id proof")
    ID_PROOF = input('Enter your ID_PROOF:')
    print('View various options you want to see:')
    print('Book you trip , flights , trains ')
    print("please enter 1 to book hotels. Booking of flights and trains will be followed afterwards")
    view()
    station = input('Enter tour type? International or Domestic:')
    station=station.title()
    select = input('Enter tour package type code:')
    cursor.execute('SELECT COUNT(*) FROM TOURIST')
    count = cursor.fetchall()
    for i in count:
        slno = i[0] + 1
    cursor.execute( 'INSERT INTO TOURIST(SLNO ,NAME ,NO_OF_PERSON ,ADDRESSE ,CONTACT_NO ,TOUR_PACKAGE ,VALID_ID_PROOF)  VALUES ( {} ,"{}" , {} ,"{}",{},"{}","{}")'.format(slno,name,no_of_person,addresse,phone1,select,ID_PROOF))
    if station == 'International':
        print('Book you desirable flight to go to your destinations')
        cursor.execute('SELECT * FROM FLIGHTS_INT')
        info3 = cursor.fetchall()
        print(tabulate(info3,headers=["TOUR_PACKAGE_CODE","FLIGHT","FROM","TO","RATE"],tablefmt="psql"))
        From = input('FROM-')
        To = input('To-')
        cursor.execute('SELECT RATE FROM FLIGHTS_INT WHERE FROM_ = "{}" AND TO_ = "{}"'.format(From ,To))
        d = cursor.fetchall()																						
        for d1 in d:
            d2 += d1[0]
        net = (no_of_person)*(d2)
        cursor.execute('SELECT FLIGHT, FLIGHT_CODE FROM FLIGHTS_INT WHERE FROM_ = "{}" AND TO_ = "{}"'.format(From ,To))
        a1 = cursor.fetchall()
        x = a1[0][0]+'('+a1[0][1]+')'
        cursor.execute('UPDATE TOURIST SET TRANSPORT = "{}" WHERE NAME="{}"'.format(x,name))      
        mycon.commit()
    else:
        print("book your flights or trains for your destination")
        print('''Press 1 to book Flights
Press 2 to book Train''')
        op = input()
        if op == '1':
            print('Book you desirable flight')
            cursor.execute('SELECT * FROM FLIGHTS_DOM')
            inf04 = cursor.fetchall()
            print(tabulate(inf04,headers=["TOUR_PACKAGE_CODE","FLIGHT","FROM","TO","RATE"],tablefmt="psql"))
            From = input('FROM-')
            To = input('To-')
            cursor.execute('SELECT RATE FROM FLIGHTS_DOM WHERE FROM1 = "{}" AND TO1 = "{}"'.format(From ,To))
            d = cursor.fetchall()
            for d1 in d:
                d2 = d1[0]
            net = (no_of_person)*(d2)								
            cursor.execute('SELECT FLIGHT, FLIGHT_CODE FROM FLIGHTS_DOM WHERE FROM1 = "{}" AND TO1 = "{}"'.format(From ,To))
            a1 = cursor.fetchall()
            x = a1[0][0]+'('+a1[0][1]+')'
            cursor.execute('UPDATE TOURIST SET TRANSPORT ="{}" WHERE NAME="{}"'.format(x,name))
            mycon.commit()
        else:
            print('Book you desirable train')
            cursor.execute('SELECT * FROM TRAINS')
            info5 = cursor.fetchall()
            print(tabulate(info5,headers=["TOUR_PACKAGE_CODE","TRAIN NAME","TRAIN NO","FROM","TO","RATE"],tablefmt="psql"))
            From = input('FROM-')
            To = input('To-')
            cursor.execute('SELECT RATE FROM TRAINS WHERE STARTPOINT = "{}" AND ENDPOINT = "{}"'.format(From ,To))
            d = cursor.fetchall()
            for d1 in d:
                d2 = d1[0]
            net = (no_of_person)*(d2)
            cursor.execute('SELECT T_NAME FROM TRAINS WHERE STARTPOINT = "{}" AND ENDPOINT = "{}"'.format(From ,To))
            a1 = cursor.fetchall()
            x = a1[0][0]
            cursor.execute('UPDATE TOURIST SET TRANSPORT = "{}" WHERE NAME="{}"'.format(x,name))     
            mycon.commit()
def process():
    global station
    global select											
    global no_of_person
    global total_fare
    global net
    price=0
    if station == 'International':
        cursor.execute('SELECT TOTALPRICE FROM INTERNATIONAL WHERE TOUR_PACKAGE_CODE = "{}"'.format(select))
        G = cursor.fetchall()
        for j in G:
            price += j[0]
    else:
        cursor.execute('SELECT TOTALPRICE FROM DOMESTIC WHERE TOUR_PACKAGE_CODE = "{}"'.format(select))        
        G = cursor.fetchall()
        for j in G:
            price += j[0]
    total_fare = (price)*(no_of_person)+net
    cursor.execute('UPDATE TOURIST SET TOTAL_FARE = {} WHERE NAME = "{}"'.format(total_fare,name))
    mycon.commit()    
def delete(name1):
    d1=0
    cursor.execute('SELECT SLNO FROM TOURIST WHERE NAME = "{}"'.format(name1))
    change = cursor.fetchall()
    for d in change:
        d1 += d[0]
    cursor.execute('UPDATE TOURIST SET SLNO = SLNO-1 WHERE SLNO > {}'.format(d1))
    cursor.execute('DELETE FROM TOURIST WHERE NAME = "{}" '.format(name1))
    mycon.commit()										
    
def modify():    
    name1 = input('Enter tourist name:')
    t1=0
    while True:
        print('''1)Press 1 to delete
2)Press 2 to re-register''')
        choose = int(input("choose from above:"))
        if choose == 1:
            cursor.execute('SELECT TOTAL_FARE FROM TOURIST WHERE NAME = "{}" '.format(name1))
            f = cursor.fetchall()
            for t in f:
                t1 += t[0]
            print('You will be refunded only with 60%',t1*0.6)
            f = open('project.txt','r+')
            f.write('NAME - ')
            f.write(str(name1))
            f.write('\n\n')
            f.write('You will be refunded with only ')
            f.write(str(t1*0.6))
            f.close()
            delete(name1)
            break
        elif choose == 2:
            delete(name1)
            registration()
            process()																							
            break
        else:
            print('Enter correctly either 1 or 2')
def domestic():
    dom=["KERALA","GUJARAT","RAJASTHAN","MUMBAI-GOA"]
    customers=[40,25,36,50]
    p.suptitle("DESTINATION ANALYSIS")
    p.title("DOMESTIC DESTINATIONS")
    colors=["yellow","red","green","blue","cyan"]
    p.pie(customers,labels=dom,colors=colors,autopct="%1.2f%%")
    p.legend(dom, loc = 'best')
    p.show()
    
def international():
    int_=["EUROPE","BHUTAN","BALI","DUBAI"]
    customers=[46,10,12,38]
    p.suptitle("DESTINATION ANALYSIS")
    p.title("INTERNATIONAL DESTINATIONS")
    colors=["yellow","red","green","blue","cyan"]
    p.pie(customers,labels=int_,colors=colors,autopct="%1.2f%%")
    p.legend(int_ , loc = 'best')
    p.show()   
def show():
    print("\n\n")
    print("""press 1 for international analysation
press 2 for domestic analysation""")
    h = 'y'																							
    while h == 'y':
        h = 'y'
        print("\n\n")
        op=input("Enter your choice(1 or 2):")
        if op=="1":
            international()
        elif op=="2":
            domestic()            
        else:
            print("please enter correctly.")            
        h = input('Do you want to continue?y/n:')
        print("\n\n")
def bill():
    f =open('project.txt','w+')
    f.write('NAME- ')
    f.write(str(name))
    f.write('\n\n')
    f.write('EMAIL- ')
    f.write(str(email))
    f.write('\n\n')
    f.write('FIRST PHONE NUMBER- ')
    f.write(str(phone1))
    f.write('\n\n')
    f.write('SECOND PHONE NUMBER- ')
    f.write(str(phone2))
    f.write('\n\n')
    cursor.execute('SELECT NAME ,NO_OF_PERSON ,ADDRESSE ,TOUR_PACKAGE ,TOTAL_FARE ,VALID_ID_PROOF,TRANSPORT FROM TOURIST')							
    d = cursor.fetchall()
    f.write('PERSONAL DETAILS-')
    f.write('\n')
    f.writelines(str(tabulate(d,headers = ['NAME','NO_OF_PERSON','ADDRESSE','TOUR_PACKAGE','TOTAL_FARE','VALID_ID_PROOF','FLIGHT/TRAIN'],tablefmt = 'psql')))
    f.write('\n\n')
    if station == 'International':
        cursor.execute('SELECT * FROM FLIGHTS_INT WHERE  FROM_ = "{}" AND TO_ = "{}"'.format(From ,To))
        c = cursor.fetchall()
        f.write('FLIGHT_')
        f.write('\n')
        f.writelines(str(tabulate(c,headers=['FlightCode','Flight','From','To','Rate'],tablefmt='psql')))
    else:
        print('''1)Press 1 to enter flight
2) Press 2 to enter train''')
        op = input()
        if op == '1':
            cursor.execute('SELECT * FROM FLIGHTS_DOM WHERE  FROM1 = "{}" AND TO1 = "{}"'.format(From ,To))
            c = cursor.fetchall()
            f.write('FLIGHT-')
            f.write('\n')
            f.writelines(str(tabulate(c,headers=['FlightCode','Flight','From','To','Rate'],tablefmt='psql')))
        else:
            cursor.execute('SELECT * FROM TRAINS WHERE  STARTPOINT = "{}" AND ENDPOINT = "{}"'.format(From ,To))
            c = cursor.fetchall()																					
            f.write('TRAIN-')
            f.write('\n')
            f.writelines(str(tabulate(c,headers=['TrainCode','Train','TrainNo','From','To','Rate'],tablefmt='psql')))
    f.write('\n\n')
    f.write('NET AMOUNT(TRANSPORT)- ')
    f.write('\t')
    f.write(str(net))
    f.write('\n')
    f.write('TOTAL AMOUNT- ')
    f.write(str(net + total_fare))
    f.close()   
#MAIN CODING    
print("\n\n\n")
print('-----------------WELCOME TO OUR WEBSITE FACILITY-------------------')
print("\n\n")
print('''1)Press 1 to see our options
2) Press 2 to view destination popularity
3)Press 3 if you want to register as our tourist
4)Press 4 if you want certain change
5)Press 5 to generate your finally registered bill''')
print("\n\n")
f = 'y'
while f =='y':    
    choice = input("choose what do you wnat to perform:")    
    if choice == '1':
        view()
    elif choice == '2':										
        show()
    elif choice == '3':
        registration()
        process()
    elif choice == '4':
        modify()
    elif choice == '5':
        bill()
    else:
        print('Enter correctly:')
        continue    
    f = input('Do yo want to continue (or exit) in our website? y/n')
    print("\n\n")
