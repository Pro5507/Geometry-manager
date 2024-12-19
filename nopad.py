from tkinter import *
w= Tk()
w.title("Number Pad")
w.geometry("500x500")
n= [[9,8,7],[6,5,4],[3,2,1],["#",0,"*"]]
for i in range(4):
    w.columnconfigure(i, weight=1, minsize=75)
    w.rowconfigure(i, weight=1, minsize=50)
for i in range(4):
    for j in range(3):
        frame= Frame(master= w, relief= SUNKEN, borderwidth=1, bg= "yellow")
        frame.grid(row= i, column=j, sticky="nsew")
        l= Label(master= frame, text= n[i][j], bg= "green", font= ('Arial', 20))
        l.pack(expand= True, fill= "both", padx= 5, pady= 5)
w.mainloop()