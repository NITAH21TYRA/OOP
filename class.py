#A class is written in singular and it starts with a capital letter i.e Student
# It has properties,attribute and methods
# A constructor is a special type of function .
#Creating a class of a Student at witu

class Student:
    #StudentNo
    #name 
    #email
    #contact
    #age
    #cohort
    def __init__(self,student_no,name,email,contact,age,cohort):
        self.student_no = student_no
        self.name = name
        self.email = email
        self.contact = contact
        self.age= age
        self.cohort =cohort 

    def __str__(self):
        return(f"{self.student_no},{self.name},{self.email},{self.contact},{self.age},{self.cohort}")    

#Creating an instance (object)
#Each object has the same attributes from the class
     
student1 = Student('2023/DCSE/0079/SS','Nansalire Anitah','anitahnansa@gmail.com',21,782870428,3) 
student2 = Student('2023/DCSE/0074/SS','Nambuya Shamirah','ahmed@gmail.ug',741839283,21,3)
print(student1)


#Create a function that returns the student's name,their cohort and the email adress
# Acess this function using any instance of the class.
class User:
    def __init__(self,student_no,name,email,cohort):
        self.student_no = student_no
        self.name = name
        self.email = email
        self.cohort =cohort 
#Passing through a string literal
    def __str__(self):
        return (f"{self.name},{self.email},{self.cohort}")
user1 = User('2023/DCSE/0079/SS','Nansalire Anitah','anitahnansa@gmail.com',3)
print(user1)
     




    
