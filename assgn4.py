#OBJECT ORIENTED PROGRAMING INTRODUCTION
#Models/Class/Resources
#1.User
     #*id
     #Email
     #contacto
     #fast and last name (we concertinate the two strings to make a name)
     #Password
     #Image (optional)
     #User-type(customer)
#2.Food
       #id
       #name
       #description
       #price 
       #image
       #category
       
#Creating a user class with properties(Name,Age and Location)
class User:
    def __init__(my,name,age,location):
        my.name = name
        my.age = age
        my.location = location
def user_details(my):
    return  (f"Name: {my.name},Age:{my.age}, Location:{my.location}")
user1 = User("Nansalire Anitah", 21, "Makerere")
print(user1.name)
print(user1.age)


#Print the User's location using the function
def my_location(my):
    print("My location:",my)
my_location("Makerere")