# ------------------------------------------------>
# Exercise 
a,b='Shahid ','Zafar'
first_name,last_name,age,full_name,country,city,birth_year,is_married='Shahid','Zafar',25,a+b,'Pakistan','islamabad',1999,False

print("Data type : ", type(first_name))
print("Data type : ", type(last_name))
print("Data type : ", type(age))
print("Data type : ", type(full_name))
print("Data type : ", type(country))
print("Data type : ", type(city))
print("Data type : ", type(birth_year))
print("Data type : ", type(is_married))

print("length of my full name is : ", len(full_name))

print('\n','\n')

num1,num2=5,4
total=num1+num2 # can also use num1+num2
print('Sum : ',total)
diff=num2-num1
print('Subtraction : ', diff)
prod=num1*num2
print('Product or multiplication  : ', prod)
division=num1/num2
print('Division : ', division)
reminder=num1%num2
print('Reminder  : ', reminder)
exp=num1**num2
print("Power : ", exp)

pi=3.14
radius=30
area_of_circle= pi*(radius**2) # can be writen as pi*radius*radius
circum_circle=2*pi*radius
print('Area of circle is : ', area_of_circle)
print('Circumference of circle is : ', circum_circle)


radius=int(input('Please enter radius of circle : ')) # python consider user input as a String only. you need to explicitly cast it to integer
area_of_circle= pi*radius*radius # can be writen as pi*radius*radius
circum_circle=2*pi*radius
print('Area of circle using dynamic input : ', area_of_circle)
print('Circumference of circle using dynamic input : ', circum_circle)

