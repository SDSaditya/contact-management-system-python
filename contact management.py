#!/usr/bin/env python
# coding: utf-8

# In[3]:


contactlist=[]
def createcontact():
    firstname=input("enter first name")
    lastname=input("enter last name")
    phonenumber=int(input("enter the phone number"))
    email=input("enter the email")
    newcontact={"Name":firstname+lastname,"phone no":phonenumber,"email":email}
    contactlist.append(newcontact)


def contactsinfo():
    if not contactlist:
        print("No contacts found.")
    else:
        print("Contacts info:")
        for contact in contactlist:
            print("Name:", contact["Name"])
            print("Phone:", contact["phone no"])
            print("Email:", contact["email"])
            print("-" * 20)


def findcontact():
    findname = input("Enter name to search: ")
    foundcontacts = []
    for newcontact in contactlist:
        if findname.lower() in newcontact["Name"].lower():
            foundcontacts.append(newcontact)
    if not foundcontacts:
         print("No matching contacts found.")
    else:
        print("Matching Contacts:")
        for newcontact in foundcontacts:
            print("Name:", newcontact["Name"])
            print("Phone:", newcontact["phone no"])
            print("Email:", newcontact["email"])
            print("-" * 20)

def main():
    while True:
        print("\nMenu:")
        print("1.create contact")
        print("2.contacts info")
        print("3.find contact")
        print("4.Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            createcontact()
        elif choice == "2":
            contactsinfo()
        elif choice == "3":
            findcontact()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()



# In[ ]:




