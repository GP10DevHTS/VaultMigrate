from tkinter import *
from resource import test_connection

# Function to handle the test button click for server 1
def test_server_1():
    server_1_log = test_connection(server_1.get(), server_username_1.get(), server_password_1.get())
    logText.insert(END, server_1_log + '\n')
    logText.see(END)  # Scroll to the end

# Function to handle the test button click for server 2
def test_server_2():
    server_2_log = test_connection(server_2.get(), server_username_2.get(), server_password_2.get())
    logText.insert(END, server_2_log + '\n')
    logText.see(END)  # Scroll to the end

# Main window
root = Tk()
root.title("VaultMigrate")



# Welcome text | sample label
welcomeLabel = Label(root, text="Welcome to VaultMigrate")
welcomeLabel.grid(row=0, column=0, columnspan=3)

# con1 section
con1Label = Label(root, text="Server 1", width=10)
con1Label.grid(row=1, column=0)

# con1 -> servername
server_1 = Entry(root, width=50)
server_1.insert(0, "server 1 name")
server_1.grid(row=2, column=0)

# con1 -> serverusername
server_username_1 = Entry(root, width=50)
server_username_1.insert(0, "server 1 username")
server_username_1.grid(row=3, column=0)

# con1 -> serverpassword
server_password_1 = Entry(root, width=50, show='*')
server_password_1.insert(0, "server 1 password")
server_password_1.grid(row=4, column=0)

# Button to test server 1
testButton1 = Button(root, text="Test Server 1", command=test_server_1)
testButton1.grid(row=5, column=0)

# con2 section
con2Label = Label(root, text="Server 2", width=10)
con2Label.grid(row=1, column=1)

# con2 -> servername
server_2 = Entry(root, width=50)
server_2.insert(0, "server 2 name")
server_2.grid(row=2, column=1)

# con2 -> serverusername
server_username_2 = Entry(root, width=50)
server_username_2.insert(0, "server 2 username")
server_username_2.grid(row=3, column=1)

# con2 -> serverpassword
server_password_2 = Entry(root, width=50, show='*')
server_password_2.insert(0, "server 2 password")
server_password_2.grid(row=4, column=1)

# Button to test server 2
testButton2 = Button(root, text="Test Server 2", command=test_server_2)
testButton2.grid(row=5, column=1)

# Log section using Text widget
logText = Text(root, wrap=WORD, height=10, width=80)
logText.grid(row=6, column=0, columnspan=2)

# Main loop
root.mainloop()
