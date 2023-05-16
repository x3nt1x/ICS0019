"""Homework 1"""
import tkinter as tkinter
from tkinter import ttk
from square_x3nt1x.app import quadratic_formula


def cli() -> None:
    """CLI for the calculator."""
    ok = '\033[92m'
    fail = '\033[91m'

    try:
        first = float(input('First number: '))
        second = float(input('Second number: '))

        print(f'({first} + {second})² = {ok}{quadratic_formula(first, second)}')
    except ValueError:
        print(f'{fail}Only numeric values are allowed!')


def gui() -> tkinter.Tk:
    """GUI for the calculator."""
    # create main window
    window = tkinter.Tk()

    # customize main window
    window.title('Homework 1')
    window.geometry('450x250')
    window.resizable(False, False)
    window.configure(background='#303030')

    # title
    tkinter.Label(window, text='Quadratic formula calculator', font=('Arial Bold', 15),
                  background='#303030', foreground='#2589FF', height=2).pack()

    # separator line
    ttk.Separator(window, orient='horizontal').pack(fill='x')

    # first number label
    tkinter.Label(window, text='First number', font=('Arial Bold', 12), bg='#303030', fg='#FFF').pack(pady=5)

    # first number textbox
    a = tkinter.Entry(window, font=('Arial Bold', 10), bg='#505050', insertbackground='#FFF', fg='#FFF', width=35)
    a.pack()

    # second number label
    tkinter.Label(window, text='Second number', font=('Arial Bold', 12), bg='#303030', fg='#FFF').pack(pady=5)

    # second number textbox
    b = tkinter.Entry(window, font=('Arial Bold', 10), bg='#505050', insertbackground='#FFF', fg='#FFF', width=35)
    b.pack()

    # calculation result label
    label = tkinter.Label(window, text='(a + b)²', font=('Arial Bold', 15), bg='#303030', fg='#FFF')
    label.pack(pady=10)

    def on_enter(e: tkinter.Event) -> None:
        """Button hover."""
        button['background'] = '#555555'

    def on_leave(e: tkinter.Event) -> None:
        """Button regular."""
        button['background'] = '#454545'

    def calculate() -> None:
        """Button click."""
        try:
            first = float(a.get())
            second = float(b.get())

            label.config(text=f'({first} + {second})² = {quadratic_formula(first, second)}', foreground='#FFF')
        except ValueError:
            label.config(text='Only numeric values are allowed!', foreground='#FF0000')

    # button
    button = tkinter.Button(window, text='Calculate', font=('Arial Bold', 10), bg='#454545', activebackground='#454545',
                            foreground='#FFF', activeforeground='#FFF', command=calculate)
    button.pack()

    button.bind("<Enter>", on_enter)
    button.bind("<Leave>", on_leave)

    return window


if __name__ == '__main__':
    gui().mainloop()
    # cli()
