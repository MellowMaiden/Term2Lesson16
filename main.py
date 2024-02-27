#Lesson 16 Term 2
#Example 1
import xml.dom


class student:
    name=""
    number=""

stephen = student()
stephen.name="stephen easley-walsh"
stephen.number="1234567x"

print("The name is ", stephen.name, "and the number is", stephen.number)

#Example 2
class book:
    name = ""
    pub = ""
    lang =""
    pg =0
    isbn10=""
    isbn13=""
    dimCM=[]
    reviews=0.00
    bestSellers=[]

myBook = book()
myBook.name = "xxxxxxxxx"
myBook.pub = "aaaaaaaaa"
myBook.lang="English"
myBook.pg=336
myBook.isbn10="2123132"
myBook.isbn13="123241"
myBook.dimCm=[20.32,2.03,25.15]
myBook.reviews=4.5
myBook.bestSellers=["anne","tom","leo"]

print("The reviews for", myBook.name,"is", myBook.reviews)

#Example 3
class vector:
    x=0
    y=0

def length(v):
    return(v.x**2 + v.y**2)**0.5

r=vector()
r.x=3.0
r.y=4.0

print("The length is", length(r))

#Example 4
class circle:
    x = 0.0
    y = 0.0
    r = 0.0

def circumference(c):
    return 2*3.141592654*c.r

def area(c):
    return 3.141592654*(c.r**2)

c = circle()
c.x = float(input("What is the x?"))
c.y = float(input("What is the y?"))
c.r = float(input("What is the r?"))

print("circumference:",circumference(c))
print("Area:",area(c))

#Example 4
class vector:
    x = 0.0
    y = 0.0
    def length(self):
        return(self.x**2 + self.y**2)**0.5

v = vector()
v.x = 3.0
v.y = 4.0

print(v.length())

#Example 5
class circle:
    x = 0.0
    y = 0.0
    r = 0.0
    def circumference(self):
        return 2*3.141592654*self.r

    def area(self):
        return 3.141592654*(self.r)**2

myCircle = circle()
myCircle.x = 0
myCircle.y = 0
myCircle.r = 2.0
print("Area:",myCircle.area())
print("circumfrence:",myCircle.circumference())

#Example 6
class circle:
    name = "circle"
    def setX(self,X):
        self.x = X

    def setY(self,Y):
        self.y = Y

    def setR(self,R):
        self.r = R

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getR(self):
        return self.r

    def area(self):
        return 3.141592654*(self.r)**2
myCircle = circle()
myCircle = circle()
myCircle.setX(0)
myCircle.setY(0)
myCircle.setR(2.0)

print("Your shape is a ", myCircle.name,"It ha s a x value of ",myCircle.getX(),"and a y value of",myCircle.getY())
print("The radius is ",myCircle.getR())
print("Area:",myCircle.area())

#Eample 7
#Create a class called vactor which has variables dim,x,y and the function length()
#make sure to use getters and setters , also, the variable "dim is static and always 2
class vector:
    dim = 2
    def __init__(self,X,Y):
        self.x=X
        self.y=Y
    def setX(self,X):
        self.x = X
    def setY(self,Y):
        self.y=Y
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def length(self):
        return(self.x**2 + self.y**2)**0.5
v=vector(5,12)

print("The vector is in", v.dim,"dimensions")
print("The vector has x of",v.getX(),"and y of",v.getY())
print("The length is", v.length())