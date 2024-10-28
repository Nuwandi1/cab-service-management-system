print()
name= input("Enter your Name:")
print()
print("Have a Nice Day "+name+",Welcome our cab service!")

#1 Book Vehicle line6-line98
def bookvehicle():
    print("1-Car")
    print("2-Van")
    print("3-3 Wheelers")
    print("4-Trucks")
    print("5-Lorry")
    print("6-go back")
    print()
    Vehicletype=input("Enter Vehicle Type:")

#select car
    if(Vehicletype=="1"):
        Noofseat= int(input("Enter nuber of seats:"))
        while(Noofseat<=0 or Noofseat>4 ):
            print("Cars has maximum of of seat 3&4")
            Noofseat = int(input("Enter valid nuber of seats:"))
            print()

        actype=int(input("Input 1 for AC or 2 for nonAC:"))
        while (actype < 1 or actype >2):
            print("please try again")
            actype = int(input("Enter correct number:"))
            print()

        if (actype==1):
            print("you select \"Ac car\" option is available")
            print(accar[0])
            first()
        else:
            print("you select \"NonAc car\" available ")
            print(nonaccar[0])
            first()

#select van
    elif(Vehicletype=="2"):
        Noofseat = int(input("Enter nuber of seats:"))
        while (Noofseat <= 0 or Noofseat > 8):
            print("Van has maximum of of seat 6&8")
            Noofseat = int(input("Enter valid nuber of seats:"))
            print()

        actype = int(input("Input 1 for AC or 2 for nonAC:"))
        while (actype < 1 or actype > 2):
            print("please try again")
            actype = int(input("Enter correct number:"))
            print()

        if (actype ==1):
            print("you select \"Ac Van\" option is available")
            print(acvan[0])
            first()
        else:
            print("you select \"NonAc\" Van available ")
            print(nonacvan[0])
            first()

#select 3 wheeler
    elif (Vehicletype == "3"):
        Noofseat = int(input("Enter nuber of passengers:"))
        while (Noofseat <= 0 or Noofseat > 3):
            print("3 Wheelers has maximum of seat 3")
            Noofseat = int(input("Enter valid nuber of seats:"))
            print()

        print("you select \"3 Wheelers\" option is available")
        print(wheel[0])
        first()

#select truck
    elif (Vehicletype == "4"):
        size = int(input("Enter Size :"))
        while (size <=0 or size > 12):
            print("truck size is  7 ft and 12 ft")
            size = int(input("try again:"))
            print()

        if (size <7):
            print("you select \"7ft truck\" option is available")
            print(s_truck[0])
            first()
        else:
            print("you select \"12ft truck\" available ")
            print(m_truck[0])
            first()
#select lorry
    elif (Vehicletype == "5"):
        load = int(input("load(Kg):"))
        while (load <= 0 or load > 2500):
            print("max load is 2500Kg")
            load = int(input("Enter agin:"))
            print()
        size = int(input("size(Kg):"))
        while (size <= 0 or size > 3500):
            print("max size is 3500Kg")
            size = int(input("Enter agin:"))
            print()

        print("you select \"Lorry\" option is available")
        print(lorry[0])
        first()
    elif(Vehicletype == "6"):
        first()

    else:
        print("enter correct option")
        bookvehicle()

vehicle1="1-AC Car"
vehicle2="2-NonAC Car"
vehicle3="3-AC Van"
vehicle4="4-NonAC van"
vehicle5="5-3 Wheelers"
vehicle6="6-7ft truck"
vehicle7="7-12ft truck"
vehicle8="8-Lorry"



accar = ["AB002", "AB003", "AB004"]
nonaccar=["ABC001","ABC002","ABC003"]
acvan = ["AD002", "AD003", "AD004"]
nonacvan = ["ABD002", "ABD003", "ABD004"]
wheel= ["WE001","WE003","WE005"]
s_truck = ["SL002", "SL005", "SL006"]
m_truck = ["ML002","ML005","ML006"]
lorry = ["LL002","LL003","LL004"]


def second():
    print("     a - Add a new vehicle ")  #line144
    print("     b - Remove a vehicle .")   #line146
    print("     c - Assign a job (hire).")  #line148
    print("     d - Release from assigned job (hire) after completing.")  #line150
    print("     e - See available vehicle .")  #line152

    option2=input("select one:")

    if(option2=="a"):   #line157-206
        a()
    elif(option2=="b"):  #line208-305
        b()
    elif(option2=="c"):
        c()
    elif (option2== "d"):
        d()
    elif (option2 == "e"):  #line318-357
        e()
    else:
        print("enter corrct letter")
        second()

def a():
    print("\n"+vehicle1+"\n"+vehicle2+"\n"+vehicle3+"\n"+vehicle4+"\n"+vehicle5+"\n"+vehicle6+"\n"+vehicle7+"\n"+vehicle8)
    print()
    type = int(input(" select vehicle type:"))
    id = input("vehicle id:")
    if(type==1):
        print( ""+id+ "number Ac car added successful")
        accar.append(id)
        print(accar)
        first()
    elif(type==2):
        print( ""+id+ "number NonAc car added successful")
        nonaccar.append(id)
        print(nonaccar)
        first()
    elif (type == 3):
        print(""+id + "number Ac Van added successful")
        acvan.append(id)
        print(acvan)
        first()
    elif (type == 4):
        print(""+id + "number NonAc Van added successful")
        nonacvan.append(id)
        print(nonacvan)
        first()
    elif (type == 5):
        print(""+id + "number 3 Wheeler added successful")
        wheel.append(id)
        print(wheel)
        first()
    elif (type == 6):
        print(""+id + "number 7ft truck added successful")
        s_truck.append(id)
        print(s_truck)
        first()
    elif (type == 7):
        print(""+id + "number 12ft truck added successful")
        m_truck.append(id)
        print(m_truck)
        first()
    elif (type == 8):
        print(""+id + "number Lorry added successful")
        lorry.append(id)
        print(lorry)
        first()
    else:
        print()
        print("Try again")
        a()

def b():
    print(
        "\n" + vehicle1 + "\n" + vehicle2 + "\n" + vehicle3 + "\n" + vehicle4 + "\n" + vehicle5 + "\n" + vehicle6 + "\n" + vehicle7 + "\n" + vehicle8)
    print()
    type = int(input(" select vehicle type:"))

    if (type == 1):
        print(accar)
        id = input(" enter the vehicle id you want to remove:")
        if(id==accar):
            print("" + id + "number Ac car remove successful")
            accar.remove(id)
            print(accar)
            first()
        else:
            print("try again")
            b()
    elif (type == 2):
        print(nonaccar)
        id = input("enter the vehicle id you want to remove:")
        if (id == nonaccar):
            print("" + id + "number NonAc car remove successful")
            nonaccar.remove(id)
            print(nonaccar)
            first()
        else:
            print("try again")
            b()
    elif (type == 3):
        print(acvan)
        id = input("enter the vehicle id you want to remove:")
        if (id == acvan):
            print("" + id + "number Ac Van remove successful")
            acvan.remove(id)
            print(acvan)
            first()
        else:
            print("try again")
            b()
    elif (type == 4):
        print(nonacvan)
        id = input("enter the vehicle id you want to remove:")
        if (id == nonacvan):
            print("" + id + "number NonAc Van remove successful")
            nonacvan.remove(id)
            print(nonacvan)
            first()
        else:
            print("try again")
            b()
    elif (type == 5):
        print(wheel)
        id = input("enter the vehicle id you want to remove:")
        if (id == wheel):
            print("" + id + "number 3 Wheeler remove successful")
            wheel.remove(id)
            print(wheel)
            first()
        else:
            print("try again")
            b()
    elif (type == 6):
        print(s_truck)
        id = input("enter the vehicle id you want to remove:")
        if (id == s_truck):
            print("" + id + "number 7ft truck remove successful")
            s_truck.remove(id)
            print(s_truck)
            first()
        else:
            print("try again")
            b()
    elif (type == 7):
        print(m_truck)
        id = input("enter the vehicle id you want to remove:")
        if (id == m_truck):
            print("" + id + "number 12ft truck remove successful")
            m_truck.remove(id)
            print(m_truck)
            first()
        else:
            print("try again")
            b()
    elif (type == 8):
        print(lorry)
        id = input("enter the vehicle id you want to remove:")
        if (id == lorry):
            print("" + id + "number Lorry remove successful")
            lorry.remove(id)
            print(lorry)
            first()
        else:
            print("try again")
            b()
    else:
        print()
        print("Try again")
        b()

def c():
    print("Assign a job (hire).")
    print(
        "\n" + vehicle1 + "\n" + vehicle2 + "\n" + vehicle3 + "\n" + vehicle4 + "\n" + vehicle5 + "\n" + vehicle6 + "\n" + vehicle7 + "\n" + vehicle8)
    print()
    name = input("Add to hire: ")
    print(name + " is added successfully to your hire.")
    first()

def d():
    print("Release from assigned job (hire) after completing")
def e():
    print("select vehicle type:")
    print("\n" + vehicle1 + "\n" + vehicle2 + "\n" + vehicle3 + "\n" + vehicle4 + "\n" + vehicle5 + "\n" + vehicle6 + "\n" + vehicle7 + "\n" + vehicle8)
    print()
    option=input("enter  your option:")
    if(option=="1"):
        print("These vehicles are available ")
        print(accar)
        first()
    elif(option == "2"):
        print("These vehicles are available ")
        print(nonaccar)
        first()
    elif (option == "3"):
        print("These vehicles are available ")
        print(acvan)
        first()
    elif (option == "4"):
        print("These vehicles are available ")
        print(nonacvan)
        first()
    elif (option == "5"):
        print("These vehicles are available ")
        print(wheel)
        first()
    elif (option == "6"):
        print("These vehicles are available ")
        print(s_truck)
        first()
    elif (option == "7"):
        print("These vehicles are available ")
        print(m_truck)
        first()
    elif (option == "8"):
        print("These vehicles are available ")
        print(lorry)
        first()
    else:
        print("try again")
        e()






def first():
    print()
    print("----------cab service----------")
    print()
    print("1-Book Vehicle") #6-98
    print("2-owners ")
    print("3-exit")
    print()
    option1=int(input("enter your option:"))
    print()
    if(option1==1):
        bookvehicle()
    elif(option1==2):
        second()
    elif (option1 == 3):
        print("Exit")
    else:
        print("try again")
        first()
first()
