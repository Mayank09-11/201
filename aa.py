from tkinter import *
window=Tk()

# add widgets here


window.title('interest Calculator')
window.geometry("380x400")
window.configure(bg='lightcyan')

#function for button
   
def calculate_its():
    p=float(principal.get())
    r=float(rate.get())
    t=float(time.get())
    SI=(p*r*t)/100
    result_label.configure(text="simple interest is "+str(SI))
    show_label.destroy()

    it=""
    
    if its < 7:
        it="low interest"
    elif its > 7 and bmi <=14:
      it=" Normal interest"
    elif its > 15 and bmi <=34:
      it="very hige interest"
    elif its > 35:
      it="super interest"
    else:
      msg="Something Went Wrong"
    
    output_message=Label(result_frame,text=p+", your Its is "+str(its)+" and "+it, si = "lightcyan", font=("Calibri", 12), width=42)
    output_message.place(x=20,y=40)
    output_message.pack()

app_label=Label(window, text="Si CALCULATOR", fg = "black", bg = "lightcyan", font=("Calibri", 20),bd=5)
app_label.place(x=50, y=20)

name_label=Label(window, text="P", fg = "black", bg = "lightcyan", font=("Calibri", 12),bd=1)
name_label.place(x=20, y=90)

username=Entry(window, text="", bd=2, width=22)
username.place(x=150, y=92)

height_label=Label(window, text="Enter R", fg = "black", bg= "lightcyan", font=("Calibri", 12))
height_label.place(x=20, y=140)

height_entry=Entry(window, text="", bd=2, width=15)
height_entry.place(x=150, y=142)

weight_label=Label(window, text="Enter T", fg = "black", bg = "lightcyan", font=("Calibri", 12))
weight_label.place(x=20, y=185)

weight_entry=Entry(window, text="", bd=2, width=15)
weight_entry.place(x=150, y=187)

calculate_button=Button(window,text="CALCULATE",fg = "black", bg = "cyan",bd=4,command=calculate_its)
calculate_button.place(x=20,y=250)

result_frame = LabelFrame(window,text="Result", bg = "lightcyan", font=("Calibri", 12))
result_frame.pack(padx=20, pady=20)
result_frame.place(x=20,y=300)

result_label=Label(result_frame,text=" ", bg = "lightcyan", font=("Calibri", 12), width=33)
result_label.place(x=20,y=20)
result_label.pack()


window.mainloop()
