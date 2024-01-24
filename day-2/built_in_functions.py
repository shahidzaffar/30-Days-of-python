# practicing some built in python functions 

age_groups=[1,15,8,6,3,15,78,4,2,0]

#minimum number from list
print("The least number in the list is : ",min(age_groups),'\n')   

#maximum number from list
print("The largest number in the list is : ",max(age_groups),'\n')


num_1,num_2,num_3=2,91,5

#minimum number in variables
print("smallest number is  : ",min(num_1,num_2,num_3),'\n')   

#maximum number in variables
print("The largest number is : ",max(num_1,num_2,num_3),'\n')


# \n moves the cursor to the next line 
# calculating length of the given String. i.e counting the 
# number of characters in String including space and other white space characters
print('\n',len('Shahid Zafar Pasha'))


# converts the given value to String. same like toString() in many other languages like java
string_value=str(105)
print (type(string_value))

# converts the given value to Integer. same like Integer.ParseInt() in  java
integer_value=int('25')
print (type(integer_value))

# other functions like int(), str() are also available for conversions like float()

#sum of a list
# it only takes the list as argument . 
print('sum of age groups : ', sum(age_groups))



#---------------------------------------------------------------
# type casting: means converting one type to another 

gravity=9.8
first_name='Shahid zafar'
print("gravity in integer : ",int(gravity)) # float to int 

print ("firstname as list : ",list(first_name)) # String to list 
