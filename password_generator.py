#password generator
import random
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers=['0','1','2','3','4','5','6','7','8','9']
special_characters=['!','#','$','%','&','*','(',')','+','^']
print("PASSWORD GENERATOR!")
l=int(input("How many letters would you like in your password? \n"))
n=int(input("How many numbers would you like? \n"))
s=int(input("How many symbols would you like? \n"))
password = []
password.extend(random.choices(letters, k=l))
password.extend(random.choices(numbers, k=n))
password.extend(random.choices(special_characters, k=s))
random.shuffle(password)
Password=''.join(password)
print(f"Your Password is: {Password}")





