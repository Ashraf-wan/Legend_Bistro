import requests

passcode = input("Enter passcode: ")
if passcode == "3031":
    print("""

                 __            _            __         
 /  _ _ _   _/  / _)' __/_    /_| _/_  '   /__)_   _ / 
(__(-(/(-/)(/  /(_)/_) // () (  |(///)//) /   (//)(-(  
    _/                                              
      Welcome to admin panel for Legend Bistro
""")
    print("[1] Check if website is running \n[2] Check total income")
    activity = input("What do you want to do? ")
    if activity == "1":
        url = input("Enter url: ")
        try:
            r = requests.get(url)
            print("Website is running")
        except:
            print("Website is down")
    elif activity == "2":
        url = input("Enter url: ")
        r = requests.get(url + '/api/v1/admin', allow_redirects=True)

        open('total.txt', 'wb').write(r.content)
        file_object = open('total.txt', 'r')
        total = file_object.read()
        print("Total income: " + total)
        file_object.close()
    else:
        print("Wrong input")
else:
    print("Access Denied")