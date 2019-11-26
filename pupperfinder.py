from dao import *
"""
Use this module to selcect and insert data from tables BREED OR PUPPER
USAGE:  select 1 for Read & 2 for Write & 3 for Delete
             THEN select table name BREED OR PUPPER
                 THEN enter either ID for read 
                        OR   each field values in respective tables to insert a row 
                             AND throw exception if one or more varaible missing
"""
choice=input("Select 1 for read and 2 for write &  3 for Delete :")

if choice=="1":
    table = input("Select TABLE BREED OR PUPPER :")
    if table == "BREED":
        Id=input("Enter Breed Id or ALL :")
        print(readBreedDB(Id))
    elif table == "PUPPER":
        Id=input("Enter Pupper ID  or ALL :")
        print(readPupperDB(Id))
    else: print("Exiting: select either table BREED OR PUPPER")
elif choice=="2":
    table = input("Select Table BREED OR PUPPER :")
    if table == "BREED":
        name=input("Enter name: ")
        temparment = input("Enter temparment: ")
        coat = input("Enter coat: ")
        breedobject=Breed(name,temparment,coat)
        writeDB(breedobject,table)
    elif table == "PUPPER":
        name = input("Enter name: ")
        sex = input("Enter sex: ")
        weight = input("Enter weight: ")
        height = input("Enter height: ")
        color = input("Enter color: ")
        date_of_birth = input("Enter date_of_birth: ")
        breed_id = input("Enter breed_id: ")
        pupperobject = Pupper(name, sex, weight, height, color, date_of_birth, breed_id)
        print(pupperobject)
        writeDB(pupperobject, table)
    else: print("Exiting: select either table BREED OR PUPPER")
elif choice=="3":
    Id = input("Enter Pupper ID :")
    print(deletePupperDB(Id))
else: print("Exiting: select either choice 1 or 2")

