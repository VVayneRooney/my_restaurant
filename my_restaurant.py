from tkinter import *
import random
import datetime
from tkinter import filedialog, messagebox


operator = ''

food_prices = [1.32, 1.65, 2.31, 3.22, 1.22, 1.99, 2.05, 2.65]
drinks_prices = [0.25, 0.99, 1.21, 1.54, 1.08, 1.10, 2.00, 1.58]
desserts_prices = [1.54, 1.68, 1.32, 1.97, 2.55, 2.14, 1.94, 1.74]



def button_click(number):
    global operator
    operator = operator + number
    calculator_visor.delete(0, END)
    calculator_visor.insert(END, operator)

def delete():
    global operator
    operator = ''
    calculator_visor.delete(0, END)

def get_result():
    global operator
    result = str(eval(operator))
    calculator_visor.delete(0, END)
    calculator_visor.insert(0, result)
    operator = ''

def verify_check():
    i = 0
    for f in food_square:
        if food_variables[i].get() == 1:
            food_square[i].config(state=NORMAL)
            if food_square[i].get() == '0':
                food_square[i].delete(0, END)
            food_square[i].focus()
        else:
            food_square[i].config(state=DISABLED)
            food_text[i].set('0')
        i += 1

    i = 0
    for f in drinks_square:
        if drinks_variables[i].get() == 1:
            drinks_square[i].config(state=NORMAL)
            if drinks_square[i].get() == '0':
                drinks_square[i].delete(0, END)
            drinks_square[i].focus()
        else:
            drinks_square[i].config(state=DISABLED)
            drinks_text[i].set('0')
        i += 1

    i = 0
    for f in desserts_square:
        if desserts_variables[i].get() == 1:
            desserts_square[i].config(state=NORMAL)
            if desserts_square[i].get() == '0':
                desserts_square[i].delete(0, END)
            desserts_square[i].focus()
        else:
            desserts_square[i].config(state=DISABLED)
            desserts_text[i].set('0')
        i += 1

def total():
    food_subtotal = 0
    p = 0
    for cantidad in food_text:
        food_subtotal = food_subtotal + (float(cantidad.get()) * food_prices[p])
        p += 1
    drinks_subtotal = 0
    p = 0
    for cantidad in drinks_text:
        drinks_subtotal = drinks_subtotal + (float(cantidad.get()) * drinks_prices[p])
        p += 1

    desserts_subtotal = 0
    p = 0
    for cantidad in desserts_text:
        desserts_subtotal = desserts_subtotal + (float(cantidad.get()) * desserts_prices[p])
        p += 1
    subtotal = food_subtotal + drinks_subtotal + desserts_subtotal
    taxes = subtotal * 0.07
    total = subtotal + taxes

    food_cost.set(f'${round(food_subtotal, 2)}')
    drinks_cost.set(f'${round(drinks_subtotal, 2)}')
    desserts_cost.set(f'${round(desserts_subtotal, 2)}')
    subtotal_var.set(f'${round(subtotal, 2)}')
    taxes_var.set(f'${round(taxes, 2)}')
    total_var.set(f'${round(total, 2)}')

def invoice():
    invoice_text.delete(1.0, END)
    invoice_number = f'N# - {random.randint(1000,9999)}'
    date = datetime.datetime.now()
    date_invoice = f'{date.day}/{date.month}/{date.year} - {date.hour}:{date.minute}'
    invoice_text.insert(END, f'Data:\t{invoice_number}\t\t{date_invoice}\n')
    invoice_text.insert(END, f'*' * 47 + '\n')
    invoice_text.insert(END, 'Items\t\tQuant \t Items Cost\n')
    invoice_text.insert(END, f'-' * 54 + '\n')

    x = 0
    for food in food_text:
        if food.get() != '0':
            invoice_text.insert(END, f'{food_list[x]}\t\t{food.get()}\t'
                                     f'${int(food.get()) * food_prices[x]}\n')
        x += 1
    x = 0
    for drinks in drinks_text:
        if drinks.get() != '0':
            invoice_text.insert(END, f'{drinks_list[x]}\t\t{drinks.get()}\t'
                                     f'${int(drinks.get()) * drinks_prices[x]}\n')
        x += 1

    x = 0
    for desserts in desserts_text:
        if desserts.get() != '0':
            invoice_text.insert(END, f'{desserts_list[x]}\t\t{desserts.get()}\t'
                                     f'${int(desserts.get()) * desserts_prices[x]}\n')
        x += 1

    invoice_text.insert(END, f'-' * 54 + '\n')
    invoice_text.insert(END,f' Food Cost: \t\t\t{food_cost.get()}\n')
    invoice_text.insert(END, f' Drinks Cost: \t\t\t{drinks_cost.get()}\n')
    invoice_text.insert(END, f' Desserts Cost: \t\t\t{desserts_cost.get()}\n')
    invoice_text.insert(END, '-' * 54 + '\n')
    invoice_text.insert(END, f' Subtotal: \t\t\t{subtotal_var.get()}\n')
    invoice_text.insert(END, f' Taxes: \t\t\t{taxes_var.get()}\n')
    invoice_text.insert(END, f' Total: \t\t\t{total_var.get()}\n')
    invoice_text.insert(END, f'*' * 47 + '\n')
    invoice_text.insert(END, 'See you soon!')

def save():
    invoice_info = invoice_text.get(1.0, END)
    file = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
    file.write(invoice_info)
    file.close()
    messagebox.showinfo('Information', 'Your invoice has been saved.')

def reset():
    invoice_text.delete(0.1, END)

    for text in food_text:
        text.set('0')
    for text in drinks_text:
        text.set('0')
    for text in desserts_text:
        text.set('0')

    for square in food_square:
        square.config(state=DISABLED)
    for square in drinks_square:
        square.config(state=DISABLED)
    for square in desserts_square:
        square.config(state=DISABLED)

    for variable in food_variables:
        variable.set(0)
    for variable in drinks_variables:
        variable.set(0)
    for variable in desserts_variables:
        variable.set(0)

    food_cost.set('')
    drinks_cost.set('')
    desserts_cost.set('')
    subtotal_var.set('')
    taxes_var.set('')
    total_var.set('')

# initialize tkinter
app = Tk()

# window size
app.geometry('1020x630+0+0')

# keep window size
app.resizable(True, False)

# window title
app.title('Linguini Restaurant')

# background color
app.config(bg='burlywood')

# top panel
top_panel = Frame(app, bd=1, relief=GROOVE)
top_panel.pack(side=TOP)

# title tag
title_tag = Label(top_panel, text='Billing System', fg='azure4',
                  font=('Dosis', 58), bg='burlywood', width=27)

title_tag.grid(row=0, column=0)

# left panel
left_panel = Frame(app, bd=1, relief=GROOVE)
left_panel.pack(side=LEFT)

# cost panel
costs_panel = Frame(left_panel, bd=1, relief=GROOVE, bg='azure4', padx=50)
costs_panel.pack(side=BOTTOM)

# food panel
food_panel = LabelFrame(left_panel, text='Food', font=('Dosis', 19, 'bold'),
                        bd=1, relief=GROOVE, fg='azure4')
food_panel.pack(side=LEFT)

# drinks panel
drinks_panel = LabelFrame(left_panel, text='Drinks', font=('Dosis', 19, 'bold'),
                        bd=1, relief=GROOVE, fg='azure4')
drinks_panel.pack(side=LEFT)

# desserts panel
desserts_panel = LabelFrame(left_panel, text='Desserts', font=('Dosis', 19, 'bold'),
                        bd=1, relief=GROOVE, fg='azure4')
desserts_panel.pack(side=LEFT)

# right panel
right_panel = Frame(app, bd=1, relief=GROOVE)
right_panel.pack(side=RIGHT)

# calculator panel
calculator_panel = Frame(right_panel, bd=1, relief=GROOVE, bg='burlywood', width=37)
calculator_panel.pack()

# ticket panel
ticket_panel = Frame(right_panel, bd=1, relief=GROOVE, bg='burlywood')
ticket_panel.pack()

# buttons panel
buttons_panel = Frame(right_panel, bd=1, relief=GROOVE, bg='burlywood')
buttons_panel.pack()

#products list
food_list = ['chicken', 'pork', 'shrimps', 'pizza', 'kebab']
drinks_list = ['water', 'coca', 'mojito', 'tequila', 'caipirinha']
desserts_list = ['ice cream', 'flan', 'lemon cake', 'lemon pie', 'chocolate cake']

# generate food items
food_variables = []
food_square = []
food_text = []
counter = 0

for food in food_list:
    food_variables.append('')
    food_variables[counter] = IntVar()
    food = Checkbutton(food_panel,
                       text=food.title(),
                       font=('Dosis', 19, 'bold'),
                       onvalue=1,
                       offvalue=0,
                       variable=food_variables[counter],
                       command=verify_check)
    food.grid(row=counter, column=0, sticky=W)

    # create input square
    food_square.append('')
    food_text.append('')
    food_text[counter] = StringVar()
    food_text[counter].set('0')
    food_square[counter] = Entry(food_panel,
                                 font=('Dosis', 18, 'bold'),
                                 bd=1,
                                 width=6,
                                 state=DISABLED,
                                 textvariable=food_text[counter])

    food_square[counter].grid(row=counter, column=1)
    counter += 1

# generate drinks items
drinks_variables = []
drinks_square = []
drinks_text = []
counter = 0

for drinks in drinks_list:
    drinks_variables.append('')
    drinks_variables[counter] = IntVar()
    drinks = Checkbutton(drinks_panel,
                         text=drinks.title(),
                         font=('Dosis', 19, 'bold'),
                         onvalue=1,
                         offvalue=0,
                         variable=drinks_variables[counter],
                         command=verify_check)

    drinks.grid(row=counter, column=0, sticky=W)

    # create input square
    drinks_square.append('')
    drinks_text.append('')
    drinks_text[counter] = StringVar()
    drinks_text[counter].set('0')
    drinks_square[counter] = Entry(drinks_panel,
                                 font=('Dosis', 18, 'bold'),
                                 bd=1,
                                 width=6,
                                 state=DISABLED,
                                 textvariable=drinks_text[counter])

    drinks_square[counter].grid(row=counter, column=1)
    counter += 1

# generate desserts items
desserts_variables = []
desserts_square = []
desserts_text = []
counter = 0

for desserts in desserts_list:
    desserts_variables.append('')
    desserts_variables[counter] = IntVar()
    desserts = Checkbutton(desserts_panel,
                           text=desserts.title(),
                           font=('Dosis', 19, 'bold'),
                           onvalue=1,
                           offvalue=0,
                           variable=desserts_variables[counter],
                           command=verify_check)

    desserts.grid(row=counter, column=0, sticky=W)
    # create input square
    desserts_square.append('')
    desserts_text.append('')
    desserts_text[counter] = StringVar()
    desserts_text[counter].set('0')
    desserts_square[counter] = Entry(desserts_panel,
                                 font=('Dosis', 18, 'bold'),
                                 bd=1,
                                 width=6,
                                 state=DISABLED,
                                 textvariable=desserts_text[counter])

    desserts_square[counter].grid(row=counter, column=1)
    counter += 1

# variables
food_cost = StringVar()
drinks_cost = StringVar()
desserts_cost = StringVar()
subtotal_var = StringVar()
taxes_var = StringVar()
total_var = StringVar()

# cost tag and inputs
food_cost_tag = Label(costs_panel,
                              text='Food Cost',
                              font=('Dosis', 12, 'bold'),
                              bg='azure4',
                              fg='white')
food_cost_tag.grid(row=0, column=0)

food_cost_text = Entry(costs_panel,
                           font=('Dosis', 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=food_cost)
food_cost_text.grid(row=0, column=1, padx=41)

drink_cost_tag = Label(costs_panel,
                              text='Drinks Cost',
                              font=('Dosis', 12, 'bold'),
                              bg='azure4',
                              fg='white')
drink_cost_tag.grid(row=1, column=0)

drink_cost_text = Entry(costs_panel,
                           font=('Dosis', 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=drinks_cost)
drink_cost_text.grid(row=1, column=1, padx=41)

desserts_cost_tag = Label(costs_panel,
                              text='Desserts Cost',
                              font=('Dosis', 12, 'bold'),
                              bg='azure4',
                              fg='white')
desserts_cost_tag.grid(row=2, column=0)

desserts_cost_text = Entry(costs_panel,
                           font=('Dosis', 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=desserts_cost)
desserts_cost_text.grid(row=2, column=1, padx=41)

subtotal_tag = Label(costs_panel,
                              text='Subtotal',
                              font=('Dosis', 12, 'bold'),
                              bg='azure4',
                              fg='white')
subtotal_tag.grid(row=0, column=2)

subtotal_text = Entry(costs_panel,
                           font=('Dosis', 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=subtotal_var)
subtotal_text.grid(row=0, column=3, padx=41)

taxes_tag = Label(costs_panel,
                              text='Taxes',
                              font=('Dosis', 12, 'bold'),
                              bg='azure4',
                              fg='white')
taxes_tag.grid(row=1, column=2)

taxes_text = Entry(costs_panel,
                           font=('Dosis', 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=taxes_var)
taxes_text.grid(row=1, column=3, padx=41)

total_tag = Label(costs_panel,
                              text='Total',
                              font=('Dosis', 12, 'bold'),
                              bg='azure4',
                              fg='white')
total_tag.grid(row=2, column=2)

total_text = Entry(costs_panel,
                           font=('Dosis', 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=total_var)
total_text.grid(row=2, column=3, padx=41)


# buttons
buttons = ['total', 'invoice', 'save', 'reset']
created_buttons = []

columns = 0

for button in buttons:
    button = Button(buttons_panel,
                    text=button.title(),
                    font=('Dosis', 14, 'bold'),
                    fg='white',
                    bg='azure4',
                    bd=1,
                    width=9)

    created_buttons.append(button)

    button.grid(row=0, column=columns)
    columns += 1

created_buttons[0].config(command=total)
created_buttons[1].config(command=invoice)
created_buttons[2].config(command=save)
created_buttons[3].config(command=reset)

# Invoice
invoice_text = Text(ticket_panel,
                    font=('Dosis', 12, 'bold'),
                    bd=1,
                    width=52,
                    height=10)
invoice_text.grid(row=0, column=0)

# calculator
calculator_visor = Entry(calculator_panel,
                         font=('Dosis', 16, 'bold'),
                         width=37,
                         bd=1,)
calculator_visor.grid(row=0, column=0, columnspan=4)

calculator_buttons = ['7', '8', '9', '+',
                      '4', '5', '6', '-',
                      '1', '2', '3', 'x',
                      'R', 'B', '0', '/']

saved_buttons = []

row = 1
column = 0
for button in calculator_buttons:
    button = Button(calculator_panel,
                    text=button.title(),
                    font=('Dosis', 16, 'bold'),
                    fg='white',
                    bg='azure4',
                    bd=1,
                    width=8)
    saved_buttons.append(button)

    button.grid(row=row, column=column)

    if column == 3:
        row += 1

    column += 1

    if column == 4:
        column = 0
saved_buttons[0].config(command=lambda: button_click('7'))
saved_buttons[1].config(command=lambda: button_click('8'))
saved_buttons[2].config(command=lambda: button_click('9'))
saved_buttons[3].config(command=lambda: button_click('+'))
saved_buttons[4].config(command=lambda: button_click('4'))
saved_buttons[5].config(command=lambda: button_click('5'))
saved_buttons[6].config(command=lambda: button_click('6'))
saved_buttons[7].config(command=lambda: button_click('-'))
saved_buttons[8].config(command=lambda: button_click('1'))
saved_buttons[9].config(command=lambda: button_click('2'))
saved_buttons[10].config(command=lambda: button_click('3'))
saved_buttons[11].config(command=lambda: button_click('*'))
saved_buttons[12].config(command=get_result)
saved_buttons[13].config(command=delete)
saved_buttons[14].config(command=lambda: button_click('0'))
saved_buttons[15].config(command=lambda: button_click('/'))

# keep window open
app.mainloop()

