from tkinter import *
import urllib
import os
import requests
url = "http://192.168.0.118/t/logins.py"
r = requests.get(url).text
with open('logins.py', 'w') as output_file:
	output_file.write(r)
from logins import *
root = Tk()
#=====================functions================
def check(event):
	a = e1.get()
	b = e2.get()
	if a == Logins[0] or a == Logins[1]:
		if b == Passwords[0] or b == Passwords[1]:
			l['text'] = "You are log in"
			l['fg'] = "green"
			os.system("python3 logins.py")
			handle = open("logs", "a")
			handle.write("\nBodia is log in;")
			handle.close()

		else:
			l['fg'] = "red"
			l['text'] = "Uncorrect login or password"
			handle = open("logs", "a")
			handle.write("\nPassword from Bodia is incorrect;")
			handle.close()
	else:
		l['fg'] = "red"
		l['text'] = "Uncorrect login or password;"
		handle = open("logs", "a")
		handle.write("\nLogin is incorrect")
		handle.close()

#=====================objects==================
l = Label(fg="green", text="All is ok")
l1 = Label(text="Login: ")
l2 = Label(text = "Password: ")
e1 = Entry()
e2 = Entry()
b1 = Button(text = "Log in")
#=====================bind=====================

b1.bind("<Button-1>", check)

#=====================pack=====================
l.pack()
l1.pack()
e1.pack()
l2.pack()
e2.pack()
b1.pack()
#==============================================
root.mainloop()