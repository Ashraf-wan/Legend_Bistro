import tkinter

# Create a window
window = tkinter.Tk()
# Set the title
window.title("Legend Bistro")
# Set the size
window.geometry("1000x1000")
# Set the background color
window.configure(background="")
# Create a button for menu       
button_menu = tkinter.Button(window, text="Menu", width=10, height=2, command=lambda: text:"pepperoni pizza : $1 \n ")
# Set the button to be in the center of the screen
button_menu.place(x=int(1),y=int(1))
# Create a button for order
button_order = tkinter.Button(window, text="Order", width=10, height=2, command=lambda: print("Order"))
# Set the button to be in the beside the menu button
button_order.place(x=int(1),y=int(40))
# Create a button for payment
button_payment = tkinter.Button(window, text="Payment", width=10, height=2, command=lambda: print("Payment"))
# Set the button to be in the below the order button
button_payment.place(x=int(1),y=int(80))
# Create a button for logout
button_logout = tkinter.Button(window, text="Logout", width=10, height=2, command=lambda: print("Logout"))
button_logout.place(x=int(1),y=int(120))
# Create a button for login
button_login = tkinter.Button(window, text="Login", width=10, height=2, command=lambda: print("Login"))
button_login.place(x=int(1),y=int(160))


# Start the window with all the buttons
window.mainloop()
