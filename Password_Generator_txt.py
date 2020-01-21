import random

print(""" 


██████╗  █████╗ ███████╗███████╗██╗    ██╗ ██████╗ ██████╗ ██████╗                ██████╗ ███████╗███╗   ██╗███████╗██████╗  █████╗ ████████╗ ██████╗ ██████╗ 
██╔══██╗██╔══██╗██╔════╝██╔════╝██║    ██║██╔═══██╗██╔══██╗██╔══██╗              ██╔════╝ ██╔════╝████╗  ██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
██████╔╝███████║███████╗███████╗██║ █╗ ██║██║   ██║██████╔╝██║  ██║    █████╗    ██║  ███╗█████╗  ██╔██╗ ██║█████╗  ██████╔╝███████║   ██║   ██║   ██║██████╔╝
██╔═══╝ ██╔══██║╚════██║╚════██║██║███╗██║██║   ██║██╔══██╗██║  ██║    ╚════╝    ██║   ██║██╔══╝  ██║╚██╗██║██╔══╝  ██╔══██╗██╔══██║   ██║   ██║   ██║██╔══██╗
██║     ██║  ██║███████║███████║╚███╔███╔╝╚██████╔╝██║  ██║██████╔╝              ╚██████╔╝███████╗██║ ╚████║███████╗██║  ██║██║  ██║   ██║   ╚██████╔╝██║  ██║
╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝ ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝                ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝
                                                                                                                                                              


""")




char = "abcdefghijklmnopqrstuvwxyx1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%&1234567890"

number_of_passwords = 1
already_have_password = str(input("\n\rDo you have your own password?  -  yes  /  no\n\r"))
password_length = int(input("\n\rEnter password length: "))
name_of_the_site = str(input("\n\rEnter the website's name: "))
user_name = str(input("\n\rEnter the user name: "))

while True:
   if already_have_password.lower() == "no":
      for p in range(number_of_passwords):
         password = ''
         for c in range(password_length):
            password += random.choice(char)
         print("\n\rThe new password is - " + password + "\n\r")

         f = open("Password_Generator.txt", "a")
         f.write(name_of_the_site + "     -     " + user_name + "     -     " + password + "\n\r")
         f.close()

         f = open("Password_Generator.txt", "r")
         print(f.read())

   elif already_have_password == "yes":
      the_password = str(input("\n\rType your password: \n\r"))

      f = open("Password_Generator.txt", "a")
      f.write(name_of_the_site + "     -     " + user_name + "     -     " + the_password + "\n\r")
      f.close()

      f = open("Password_Generator.txt", "r")
      print(f.read())
   break
