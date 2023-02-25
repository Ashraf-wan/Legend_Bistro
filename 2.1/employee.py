import os

access = input("Please put the code. ")

if access == "2021":


  print("""

                 __           ___                 __         
 /  _ _ _   _/  / _)' __/_   (_  _    /    _ _   /__)_   _ / 
(__(-(/(-/)(/  /(_)/_) // () /__//)/)(()(/(-(-  /   (//)(-(  
    _/                            /     /                   
        Welcome to Legend Bistro Employee Panel

[1]List the order [3]List ingredient in home special
[2]LIst the menu

""")

  panel = input("What do you want to do?\n")

  if panel == "1":
      print("")
  elif panel == "2":
      print("pepperoni pizza,home special,cheese pizza,ham and cheese pizza,sausage pizza")
  elif panel == "3":
      print("cheese and squared pepperoni")
else:
  print("Sorry wrong code.")      