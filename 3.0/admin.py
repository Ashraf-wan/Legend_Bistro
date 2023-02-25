import os
from numpy import random 

x = random.randint(99999)

print("""

                 __            _            __         
 /  _ _ _   _/  / _)' __/_    /_| _/_  '   /__)_   _ / 
(__(-(/(-/)(/  /(_)/_) // () (  |(///)//) /   (//)(-(  
    _/                                              
      Welcome to admin panel for Legend Bristo

[1]change menu          [3]print profit 
[2]review & change code [4]List of worker
""")

panel = input("What do you want to do?\n")

if panel == "1":
    print("pepperoni pizza,home special,cheese pizza,ham and cheese pizza,sausage pizza")
elif panel == "2":
    print("https://github.com/Ashraf-wan/legend-bistro")

elif panel == "3":
    os.system("cat total.txt")
elif panel == "4":
    print("""
    
    """)
else:
    print("invalid options")