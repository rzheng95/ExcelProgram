from tkinter import *
from tkinter import filedialog



root = Tk()

label1 = Label(root, text="Name")
entry1 = Entry(root)

label1.grid(row=0, sticky=E)

entry1.grid(row=0, column=1)

c = Checkbutton(root, text="Sign in")
c.grid(columnspan=2)

#root.filename = filedialog.asksaveasfilename(initialdir="/", title="Select file,", filetypes=(("CSV files", "*.csv"), ("all files","*.*")))

root.filename = filedialog.askopenfilename(initialdir="/", title="Select file,", filetypes=(("CSV files", "*.csv"), ("all files","*.*")))
print(root.filename)


'''
topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
button1 = Button(topFrame, text="Button 1", fg="red")
button1.pack(side=LEFT)
'''

'''
theLabel = Label(root, text="This is too easy", bg="red", fg="white")
theLabel.pack(side=LEFT, fill=X)
'''

root.mainloop()