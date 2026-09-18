#Positional arguments
#Order matters:

def student(name, age):
    print(name, age)

student("Vipul", 22)

#Keyword arguments
#Names matter, order doesn't:

student(age=22, name="Vipul")    #both outputs will be same 

def laptop(brand, ram, price):
    print(price, ram, brand)
    
laptop(brand="Dell", ram="16GB", price="₹60000")
