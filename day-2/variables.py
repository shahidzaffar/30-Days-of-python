# Day 2: 30 Days of python programming
# variable declaration and printing variables. 

first_name="Shahid"
last_name = "Zafar"
experience={
    "Java":"PROFESSIONAL",
    "Python":"NOVOICE"
}

print("full name : ",first_name,last_name)
print("Experience", experience)
print("Experience in java : ",experience.get("Java"))
print("Experience in python : ",experience.get("Python"))

#Declaring multiple variables in a single line 
address,country,age,is_studying="Islamabd","Pakistan",25,False
print('\n','\n')
print(" Address : ", address, country,'\n',"Age : ", age,'\n',"Are you a student ",is_studying)



