# example of variable
# let name = variable; JS
name = "Daphane" #STRING
age = 30 #INTEGER
height = 5.7 #FLOAT
is_student = False #BOOLEAN

print (f"Name: {name}, age: {age}, height: {height}") #PRINTS TEXT TO THE TERMINAL
print ("Type of age:", type(name))

#EXAMPLE OF AN IF STATEMENT
age = 42 #INTEGER
if age < 13:
    print("Child")
elif age < 20:
    print("Teenager")
else:
    print("Adult")

# EXAMPLE OF A FOR LOOP 
for i in range(5):
    if i == 3:
        continue
    print(i)

for numbers in range(5):
    print(numbers)

# LIST (JS ARRAY) EXAMPLE
fruits = ["Apple", "Banana", "Cherry"]
print(fruits)
fruits.append("Date")
print(fruits)
print(fruits[1:3])

# DICTIONARY
student = {
    "name": "Daphane",
    "age": 30,
    "courses": ["FSDI101", "FSDI102", "FSDI103", "FSDI104", "FSDI105", "FSDI106", "FSDI107"]
}

print(student["age"])
print(student["courses"])
student["grade"] = "A"
student.update({"email":"daphane.elizabeth@gmail.com"})
print(student)

# FUNCTIONS
def say_hello():
    print("Hello")

def say_goodbye():
    print("Goodbye")
# CALLING THE FUNCTIONS
say_hello()
say_goodbye()

# CONCATENATE USING PYTHON
print("Hello my name is " + name + " and i am "+ str(age) + "years old")