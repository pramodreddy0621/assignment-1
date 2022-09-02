# Question 1
from collections import Counter
from statistics import median
from math import pi

ages = [19, 22, 19, 24, 20, 25,26, 24, 25, 24]


#Sorting the list
sorted_ages = sorted(ages)

print("Sorted List : ",sorted_ages)

#Print the minmum age  
minimum_age = min(ages)
print("Minmum age : ",minimum_age)

#Print the maxmum age  
maximum_age = max(ages)
print("Maxmum age : ",maximum_age)

#Add the min age and the max age again to the list
sorted_ages.insert(0, 19)
sorted_ages.insert(10, 26)
print(sorted_ages)

#Find the median age (one middle item or two middle items divided by two)
median_age = median(sorted_ages)
print("median age : ",median_age)

#Find the average age (sum of all items divided by their number)
average_age = sum(sorted_ages) / len(sorted_ages)
print("average age : ",average_age)

#Find the range of the ages (max minus min)
range_ages = maximum_age = minimum_age
print("range of ages : ",range_ages)




# Question 2

print("***************************************")
print("\t\t\t\t\t***************************************")
print(                )
print("SOLUTION 2")
print(                )
print("****************************************")
#Create an empty dictionary called dog
dog = {}

#Add name, color, breed, legs, age to the dog dictionary

dog = {
    'color':'Brown',
    'breed':'German Shepherd',
    'legs':4,
    'age':'3',

    }

print(dog)
print("****************************************************")

#Create a student dictionary and add first_name, last_name, gender, age, marital status, 
#skills, country, city and address as keys for the dictionary
student = {
    'first_name': 'Robert',
    'last_name': 'Miller',
    'gender': 'Male',
    'age': 32,
    'marital_status': 'Married',
    'skills': ['SQL', 'Postgres', 'Flask', 'Javascript'],
    'country': 'Canada',
    'city': '',
    'address':{
        'street':'1570 19th Street',
        'zipcode':'80022'
    }
    }

print(student)

# Get the length of the student dictionary

print("Length: ",len(student))

#Get the value of skills and check the data type, it should be a list
print("Skills: ",student.get('skills'))
print("Data type: ",type(student.get('skills')))

#Modify the skills values by adding one or two skills
skills = student.get('skills')
skills.insert(0, "Typescript")
skills.insert(0, "AWS CDK")

print("The student dictionary with modified skills: ",student)



#Get the dictionary keys as a list
keys = student.keys()
print(keys)

#Get the dictionary values as a list
values = student.values()
print(values)


#Question 3

print("***************************************")
print("\t\t\t\t\t***************************************")
print(                )
print("SOLUTION 3")
print(                )
print("****************************************")

#Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)

brothers = ('Dante', 'Amos', 'Peter', 'Tommy')
print(brothers)

sisters = ('Kelly', 'Jessica', 'Eve', 'Ecleen')
print(sisters)

#Join brothers and sisters tuples and assign it to siblings

siblings = brothers + sisters
print(siblings)

#How many siblings do you have? 

print("Total siblings: ",len(siblings))

#Modify the siblings tuple and add the name of your father and mother and assign it to 
#family_members
family_members = siblings + ('Miller','Luciana')
print(family_members)


#Question 4

print("***************************************")
print("\t\t\t\t\t***************************************")
print(                )
print("SOLUTION 4")
print(                )
print("****************************************")

it_companies={'Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon'}
A={19,22,24,20,25,26}
B={19,22,20,25,26,24,28,27}
age=[22,19,24,25,26,24,25,24]

#length of the set it_companies using length method

length_of_it_companies=len(it_companies)
print("\n Length of it companies : {}".format(length_of_it_companies))
count=0
for i in it_companies:
    count=count+1

#add twitter to the it_companies

it_companies.add("Twitter")
print("\n After adding twitter to the it companies : \n{} ".format(it_companies))

#add multiple it companies to the set it_companies

it_companies.update(["Tcs","Tech Mahindra","Cap Gemini"])
print("\n After adding multiple companies  to the it companies : \n{} ".format(it_companies))

#remove one of the companies from set it_companies

it_companies.remove('Tcs')
print("\n Removing TCS from the set : \n{} ".format(it_companies))

#join A and B

join=A.union(B)
print("\n Joining A and B : \n{} ".format(join))


#A intersection B

intersect=A.intersection(B)
print("The intersection of A and B : \n  {}".format(intersect))

#Is A subset of B

print("Is A subset of B : \n {}".format(A.issubset(B)))


#Are A and B disjoint Sets

print("Are A and B are disjoint sets : \n {}".format(A.isdisjoint(B)))

#join a with b and b with a

joina=A.union(B)
joinb=B.union(A)
print("Joining A with B : \n {}".format(joina))
print("Joining B with A : \n {}".format(joinb))

#what is the symmetric difference between a and b

symmetric_difference=A.symmetric_difference(B)
print("The symmetric difference between A and B is : \n {}".format(symmetric_difference))

#delete the sets completely

A.clear()
B.clear()


#convert ages to set and compare the length of the list to the set

age_List=set(age)
print("Length of age in set format : \n {}".format(len(age_List)))
print("Length of age in List format: \n {}".format(len(age)))


#Question 5

print("***************************************")
print("\t\t\t\t\t***************************************")
print(                )
print("SOLUTION 5")
print(                )
print("****************************************")


#Calculate the area of a circle and assign the value to a variable name of _area_of_circle_
r = float(input ("Input the radius of the circle : "))

_area_of_circle_ =  pi * r**2
print ("area: ",_area_of_circle_)

#Calculate the circumference of a circle and assign the value to a variable name of
_circum_of_circle_ = 2 * pi *r
print ("circumference: ",_circum_of_circle_)


#Question 6
print("***************************************")
print("\t\t\t\t\t***************************************")
print(                )
print("SOLUTION 6")
print(                )
print("****************************************")


string = "I am a teacher and I love to inspire and teach people"
words = string.split(' ')
count_words = Counter(words)
unique = [w for w in words if count_words[w] == 1]

print("Unique words: ", unique)
print("Total unique words: ",len(unique))


#Question 7

print("***************************************")
print("\t\t\t\t\t***************************************")
print(                )
print("SOLUTION 7")
print(                )
print("****************************************")

#Use a tab escape sequence to get the following lines.

print('Name\t\tAge\tCountry\tCity') # adding tab space or 4 spaces 
print('Asabeneh\t250\tFinland\tHelsinki')



#Question 8


print("***************************************")
print("\t\t\t\t\t***************************************")
print(                )
print("SOLUTION 8")
print(                )
print("****************************************")


radius = 10
area = 3.14 * radius ** 2
print("The area of a circle with radius " +str(radius)+ " is " + str(area) + " meters square.")



#Question 9

print("***************************************")
print("\t\t\t\t\t***************************************")
print(                )
print("SOLUTION 9")
print(                )
print("****************************************")

#empty lists to hold weight in lbs and converted kg
L1 = []
kg = []

# Enter the number of students
N = int(input("Enter the number of students : "))

# Iterating through.....
for i in range(0, N):

    weights = int(input())

    kilo = weights * 0.453592
        # adding weights to the list
    L1.append(weights)    
    kg.append(kilo)
    print("L1: ",L1) 
    print(kg)

