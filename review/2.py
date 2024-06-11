user_name = input("enter the user_name: ")
password = input("enter the password: ")

res = False
with open("all_users.txt", "r") as f:
   for p in f.read().split("|"):
       d = p.split(",")
       if d[0] == user_name and d[1] == password:
           print("login success")
           res = True
           break
       else:
           res = False
if res == False:
    print("login failed")
           
       


# with open("all_users.txt", "a") as f:
#     f.write(f"{user_name},{password}|")