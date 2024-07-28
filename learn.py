from tkinter import *

# main window
root = Tk()

# welcome text | sample label
welcomeLabel = Label(root, text="Welcome to VaultMigrate")
#  add label to window
welcomeLabel.pack()

# =============================================================================
# # sample grid system
# # one element can be managed by either grid or pack
# for i in range(3):
#     for j in range(3):
#         Label(root, text="{}{}".format(i, j)).grid(row=i, column=j)



# =============================================================================
# sample entry
e = Entry(root, width=50, fg="red", bg="blue", borderwidth=5)
e.insert(0, "Enter your name")
# e = Entry(root, width=50)
e.pack()

# =============================================================================
# buttons
# def myClick():
#     helloLabel = Label(root, text="Hello World")
#     helloLabel.pack()
# myButton = Button(root, text="click me", command=myClick, fg="blue", bg="red").pack()
# myButton = Button(root, text="click me").pack()
# myButton = Button(root, text="click me", padx=100, pady=50).pack()
# myButton = Button(root, text="click me", state=DISABLED,padx=100, pady=50).pack()

#  button to capture text and print it
def myClick():
    helloLabel = Label(root, text=e.get())
    helloLabel.pack()
myButton = Button(root, text="click me", command=myClick, fg="blue", bg="red").pack()


# main loop
root.mainloop()