import os
from numpy import random

x = random.randint(99999)

print("Welcome to admin panel for Legend Bristo")

name = input("What is your name?\n")

print("""

                 __            _            __         
 /  _ _ _   _/  / _)' __/_    /_| _/_  '   /__)_   _ / 
(__(-(/(-/)(/  /(_)/_) // () (  |(///)//) /   (//)(-(  
    _/                                              

[1]change menu 
[2]review & change code
[3]print profit
[4]list of worker 
""")

panel = input("What do you want to do?\n")

if panel == "1":
    print("https://github.com/Ashraf-wan/legend-bistro/blob/main/menu.py")
elif panel == "2":
    print("https://github.com/Ashraf-wan/legend-bistro")

elif panel == "3":
    print("Total profit:" + str(x) + "$")
elif panel == "4":
    print("""
    
    
    
    
    
    
    
    """)
else:
    print("invalid options")
