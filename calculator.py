from tkinter import *
import tkinter
import customtkinter

customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('dark-blue')
customtkinter.set_widget_scaling(1.3)

root = customtkinter.CTk()
root.title('Calculator')
root.resizable(width=False, height=False)


#define entry
font = customtkinter.CTkFont(family='Roboto', size=32)
e = customtkinter.CTkEntry(master=root, width=35, placeholder_text='0')
e.grid(row=0, column =0, columnspan=3, ipadx=200, ipady =10, pady =30)



def butn_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str (number))

    return number

def btn_clear():
    cl = e.delete(0, END)

def but_add():
    # e.delete(0, END)
    first_number = e.get()
    global f_num 
    global math
    math = 'addition'
    f_num = int(first_number)
    e.delete(0, END)

def butn_subtraction():
    first_number = e.get()
    global f_num 
    global math
    math = 'subtraction'
    f_num = int(first_number)
    e.delete(0, END)

def butn_multiply():
    first_number = e.get()
    global f_num 
    global math
    math = 'multiply'
    f_num = int(first_number)
    e.delete(0, END)

def butn_division():
    first_number = e.get()
    global f_num 
    global math
    math = 'division'
    f_num = int(first_number)
    e.delete(0, END)

# def butn_dot():
#     first_number = e.get()
#     global f_num 
#     global math
#     math = 'dot'
#     f_num = float(first_number)
#     dot= e.insert(1, '.')
#     # e.delete(0, END)
 

def butn_equal(): 
    second_number = e.get()
    global s_num 
    s_num = int(second_number)
    e.delete(0, END)
    if math == 'addition':
        e.insert(0, f_num + s_num)
    elif math == 'subtraction':
        e.insert(0, f_num - s_num)
    elif math == 'multiply':
        e.insert(0, f_num * s_num)  
    elif math == 'division':
        if s_num == 0:
            e.insert(0, s_num)
        else:
            e.insert(0, f_num / s_num)



#define buttons 
btn1 = customtkinter.CTkButton(master=root, text='1',  command=lambda: butn_click(1))
btn2 = customtkinter.CTkButton(master=root, text='2', command=lambda: butn_click(2))
btn3 = customtkinter.CTkButton(master=root, text='3',  command=lambda: butn_click(3))
btn4 = customtkinter.CTkButton(master=root, text='4', command=lambda: butn_click(4))
btn5 = customtkinter.CTkButton(master=root, text='5',  command=lambda: butn_click(5))
btn6 = customtkinter.CTkButton(master=root, text='6',  command=lambda: butn_click(6))
btn7 = customtkinter.CTkButton(master=root, text='7', command=lambda: butn_click(7))
btn8 = customtkinter.CTkButton(master=root, text='8', command=lambda: butn_click(8))
btn9 = customtkinter.CTkButton(master=root, text='9',  command=lambda: butn_click(9))
btn0 = customtkinter.CTkButton(master=root, text='0', command=lambda: butn_click(0))
btn_equal = customtkinter.CTkButton(master=root, text='=', command= butn_equal)
btn_clearAll = customtkinter.CTkButton(master=root, text='Clear', command=btn_clear)
btn_plus = customtkinter.CTkButton(master=root, text='+', command=but_add)
btn_minus = customtkinter.CTkButton(master=root, text='-', command=butn_subtraction)
btn_divide = customtkinter.CTkButton(master=root, text='/', command= butn_division)
btn_multiply = customtkinter.CTkButton(master=root, text='*', command=butn_multiply)
# btn_dot= customtkinter.CTkButton(master=root, text='.', command=butn_dot)

#place buttons on the screen
btn1.grid(row = 1, column =0, padx=10, pady = 10)
btn2.grid(row = 1, column =1 , padx=10, pady = 10)
btn3.grid(row = 1, column =2 , padx=10, pady = 10)

btn4.grid(row = 2, column =0 , padx=10, pady = 10)
btn5.grid(row = 2, column =1 , padx=10, pady = 10)
btn6.grid(row = 2, column =2 , padx=10, pady = 10)

btn7.grid(row = 3, column =0 , padx=10, pady = 10)
btn8.grid(row = 3, column =1 , padx=10, pady = 10)
btn9.grid(row = 3 , column =2 , padx=10, pady = 10)

btn0.grid(row = 4, column =0 , padx=10, pady = 10)
btn_equal.grid(row = 4,  column =1,  columnspan =2, ipadx = 80)

btn_minus.grid(row = 5, column =0, padx=10, pady = 10)
btn_divide.grid(row = 5, column =1, padx=10, pady = 10)
btn_plus.grid(row = 5, column =2, padx=10, pady = 10)
btn_multiply.grid(row = 6, column =0, padx=10, pady = 10)
# btn_dot.grid(row = 6, column =1, padx=10, pady = 10)

btn_clearAll.grid(row = 6,  column =1, columnspan=2, ipadx = 105)
root.mainloop()