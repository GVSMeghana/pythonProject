# a = 3
# b = 2.65
# d = 2+5j
# print ("int is",a)
# print ("float is",b)
# print ("complex is",d)

# dict={1: "teja",2:"sai",3:"shaku"}
# print(dict)

# tuple1=('greeks','for',18)
# print(tuple1)

#
# dict={[(1: 'greeks',2:'for')]}
# print(dict)

# dict={1:'greeks',2:'for'}
# u=((x,y)for x,y in dict.items())
# print(u)


# print("\n\nTicket Booking System\n")
# restart = ('Y')
#
# while restart != ('N','NO','n','no'):
#   print("1.Check PNR status")
#   print("2.Ticket Reservation")
#   option = int(input("\nEnter your option : "))
#
#   if option == 1:
#     print("Your PNR status is t3")
#     exit(0)
#   elif option == 2:
#     people = int(input("\nEnter no. of Ticket you want : "))
#     name_l = []
#     age_l = []
#     sex_l = []
#     for p in range(people):
#       name = str(input("\nName : "))
#       name_l.append(name)
#       age  = int(input("\nAge  : "))
#       age_l.append(age)
#       sex  = str(input("\nMale or Female : "))
#       sex_l.append(sex)
#       print("\nTotal Ticket : ",people)
#       print("Ticket : ",p)
#       print("Name : ", name_l)
#       print("Age  : ", age_l)
#       print("Sex : ",sex_l)
import exprrr
n=random.randbytes(3)
print(n)
print(random.randrange(1,8))
print(random.randint(100,211))
mylist=["jadeja","ashwin","rahmane","shami","dhoni","virat"]
mylist1=["jadeja","ashwin","rahmane","shami","dhoni","virat"]
print(random.choice(mylist))
#print(random.choice(mylist1))
random.shuffle(mylist)