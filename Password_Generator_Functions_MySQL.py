import mysql.connector
import random
# db = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   passwd="Idanid1",
# )
#
# cursor = db.cursor()
# #
# cursor.execute("CREATE DATABASE idan_passwords")


db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="Idanid1",
  database="idan_passwords"
)
# cursor.execute("CREATE TABLE general_passwords (website VARCHAR(255), user_name VARCHAR(255), password VARCHAR(255))")

cursor = db.cursor()


def generate_pass(pw):
    char = "abcdefghijklmnopqrstuvwxyx1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%&1234567890"
    new_password = str()
    for c in range(pw):
        new_password += str(random.choice(char))
    return new_password


def old_pass():
    the_password = str(input("\n\rType your password: \n\r"))
    name_of_the_site = str(input("\n\rEnter the website's name: "))
    user_name = str(input("\n\rEnter the user name: "))
    sql = "INSERT INTO general_passwords (website, user_name, password) VALUES (%s, %s, %s)"
    val = (name_of_the_site, user_name, the_password)
    cursor.execute(sql, val)
    db.commit()
    print(cursor.rowcount, "record inserted.")


def new_pass():
    name_of_the_site = str(input("\n\rEnter the website's name: "))
    user_name = str(input("\n\rEnter the user name: "))
    password_length = int(input("\n\rEnter password length: "))
    sql = "INSERT INTO general_passwords (website, user_name, password) VALUES (%s, %s, %s)"
    val = (name_of_the_site, user_name, generate_pass(password_length))

    cursor.execute(sql, val)
    db.commit()
    print(cursor.rowcount, "record inserted.")


def main():
    already_have_password = str(input("\n\rDo you have your own password?  -  yes  /  no\n\r"))
    if already_have_password.lower() == "no":
        new_pass()
    elif already_have_password.lower() == "yes":
        old_pass()


main()


sql = "SELECT * FROM general_passwords"
cursor.execute(sql)
result = cursor.fetchall()
for x in result:
  print(x)
