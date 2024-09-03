from tkinter import *
from tkinter import ttk


def i_print(i, j):
    label = ttk.Label(i, text="И", style="My.TLabel")
    label.pack(side=LEFT)
    j.config(state=LEFT)


def m_print(i):
    label = ttk.Label(i, text="М", style="My.TLabel")
    label.pack(side=LEFT)


def p_print(i):
    label = ttk.Label(i, text="П", style="My.TLabel")
    label.pack(side=LEFT)


def r_print(i):
    label = ttk.Label(i, text="Р", style="My.TLabel")
    label.pack(side=LEFT)


def o_print(i):
    label = ttk.Label(i, text="О", style="My.TLabel")
    label.pack(side=LEFT)


def v_print(i):
    label = ttk.Label(i, text="В", style="My.TLabel")
    label.pack(side=LEFT)


def z_print(i):
    label = ttk.Label(i, text="З", style="My.TLabel")
    label.pack(side=LEFT)


def a_print(i):
    label = ttk.Label(i, text="А", style="My.TLabel")
    label.pack(side=LEFT)


def c_print(i):
    label = ttk.Label(i, text="Ц", style="My.TLabel")
    label.pack(side=LEFT)


def ya_print(i):
    label = ttk.Label(i, text="Я", style="My.TLabel")
    label.pack(side=LEFT)


def exit():
    def yes():
        window.destroy()
        window_exit.destroy()
    window_exit = Toplevel()
    window_exit.config(cursor="heart")
    window_exit.title("Выход")
    window_exit.geometry("400x200")
    x = int(window.winfo_screenwidth()/2 - 400/2)
    y = int(window.winfo_screenheight()/2 - 200/2)
    window_exit.geometry("+{}+{}".format(x, y))
    window_exit.grab_set()
    window_exit.resizable(False, False)
    window_exit.attributes("-toolwindow", True)

    lbl_question = ttk.Label(window_exit, text="ВЫ УВЕРЕНЫ?", font=("Comic Sans MS", 20))
    lbl_question.pack(pady=(35, 0))

    btn_yes = Button(window_exit, text="ДА", font=("Comic Sans MS", 15), width=8, command=yes)
    btn_yes.pack(side=LEFT,  padx=(60, 20))
    btn_no = Button(window_exit, text="НЕТ", font=("Comic Sans MS", 15), width=8, command=window_exit.destroy)
    btn_no.pack(side=RIGHT, padx=(20, 60))
    window_exit.mainloop()


def settings():
    for widget in window.winfo_children():
        widget.destroy()

    btn_menu = ttk.Button(window, text="МЕНЮ", style="My.TButton", width=8, command=menu)
    btn_menu.pack(anchor="nw", pady=20, padx=20)

    lbl_title = ttk.Label(window, text="НАСТРОЙКИ", font=("Comic Sans MS", 70))
    lbl_title.pack(pady=(10, 20))

    lbl_title = ttk.Label(window, text="ЗВУКИ", font=("Comic Sans MS", 35))
    lbl_title.pack(pady=(10, 50))
    sounds_frame = ttk.Frame(window)
    sounds_frame.pack(pady=(10, 50))
    btn_on = ttk.Button(sounds_frame, text="ВКЛ.", style="My.TButton", width=7)
    btn_on.pack(side=LEFT, padx=20)
    btn_off = ttk.Button(sounds_frame, text="ВЫКЛ.", style="My.TButton", width=7)
    btn_off.pack(side=LEFT, padx=20)

    lbl_title = ttk.Label(window, text="МУЗЫКА", font=("Comic Sans MS", 35))
    lbl_title.pack( pady=(10, 50))
    music_frame = ttk.Frame(window)
    music_frame.pack()
    btn_on = ttk.Button(music_frame, text="ВКЛ.", style="My.TButton", width=7)
    btn_on.pack(side=LEFT, padx=20)
    btn_off = ttk.Button(music_frame, text="ВЫКЛ.", style="My.TButton", width=7)
    btn_off.pack(side=LEFT, padx=20)


def menu():
    for widget in window.winfo_children():
        widget.destroy()

    style_btn = ttk.Style()
    style_btn.configure("My.TButton", font=("Comic Sans MS", 20))

    lbl_title = ttk.Label(window, text="CЛОВА ИЗ СЛОВ", font=("Comic Sans MS", 70))
    lbl_title.pack(fill=Y, pady=(120, 85))

    btn_start = ttk.Button(window, text="ИГРАТЬ", style="My.TButton", command=levels_menu)
    btn_start.pack(fill=Y, pady=(10, 10), ipady=5, ipadx=15)
    btn_lvls = ttk.Button(window, text="ПРАВИЛА", style="My.TButton")
    btn_lvls.pack(fill=Y, pady=(10, 10), ipady=5, ipadx=15)
    btn_settings = ttk.Button(window, text="НАСТРОЙКИ", style="My.TButton", command=settings)
    btn_settings.pack(fill=Y, pady=(10, 10), ipady=5, ipadx=15)
    btn_exit = ttk.Button(window, text="ВЫЙТИ", style="My.TButton", command=exit)
    btn_exit.pack(fill=Y, pady=(10, 10), ipady=5, ipadx=15)


def levels_menu():
    for widget in window.winfo_children():
        widget.destroy()

    btn_menu = ttk.Button(window, text="МЕНЮ", style="My.TButton", width=8, command=menu)
    btn_menu.pack(anchor="nw", pady=20, padx=20)

    first_frame = ttk.Frame(window)
    first_frame.pack(pady=(100, 20))
    btn_lvl1 = ttk.Button(first_frame, text="1", style="My.TButton", width=5, command=level_1)
    btn_lvl1.pack(side=LEFT, ipady=20, padx=20)
    btn_lvl2 = ttk.Button(first_frame, text="2", style="My.TButton", width=5, command=level_2)
    btn_lvl2.pack(side=LEFT, ipady=20, padx=20)
    btn_lvl3 = ttk.Button(first_frame, text="3", style="My.TButton", width=5, command=level_3)
    btn_lvl3.pack(side=LEFT, ipady=20, padx=20)
    btn_lvl4 = ttk.Button(first_frame, text="4", style="My.TButton", width=5, command=level_4)
    btn_lvl4.pack(side=LEFT, ipady=20, padx=20)

    second_frame = ttk.Frame(window)
    second_frame.pack(pady=20)
    btn_lvl5 = ttk.Button(second_frame, text="5", style="My.TButton", width=5)
    btn_lvl5.pack(side=LEFT, ipady=20, padx=20)
    btn_lvl6 = ttk.Button(second_frame, text="6", style="My.TButton", width=5)
    btn_lvl6.pack(side=LEFT, ipady=20, padx=20)
    btn_lvl7 = ttk.Button(second_frame, text="7", style="My.TButton", width=5)
    btn_lvl7.pack(side=LEFT, ipady=20, padx=20)
    btn_lvl8 = ttk.Button(second_frame, text="8", style="My.TButton", width=5)
    btn_lvl8.pack(side=LEFT, ipady=20, padx=20)

    third_frame = ttk.Frame(window)
    third_frame.pack(pady=20)
    btn_lvl9 = ttk.Button(third_frame, text="9", style="My.TButton", width=5)
    btn_lvl9.pack(side=LEFT, ipady=20, padx=20)
    btn_lvl10 = ttk.Button(third_frame, text="10", style="My.TButton", width=5)
    btn_lvl10.pack(side=LEFT, ipady=20, padx=20)
    btn_lvl11 = ttk.Button(third_frame, text="11", style="My.TButton", width=5)
    btn_lvl11.pack(side=LEFT, ipady=20, padx=20)
    btn_lvl12 = ttk.Button(third_frame, text="12", style="My.TButton", width=5)
    btn_lvl12.pack(side=LEFT, ipady=20, padx=20)


def level_1():
    for widget in window.winfo_children():
        widget.destroy()

    def destroy():
        for widget in enter_frame.winfo_children():
            widget.destroy()

    title_frame = ttk.Frame(window)
    title_frame.pack()
    btn_menu = ttk.Button(title_frame, text="МЕНЮ", style="My.TButton", width=8, command=menu)
    btn_menu.pack(side=LEFT)
    btn_lvls = ttk.Button(title_frame, text="УРОВНИ", style="My.TButton", width=8, command=levels_menu)
    btn_lvls.pack(side=LEFT, padx=(20, 100))
    lbl_lvl1 = ttk.Label(title_frame, text="УРОВЕНЬ 1", font=("Comic Sans MS", 30))
    lbl_lvl1.pack(side=LEFT)
    btn_hint = ttk.Button(title_frame, text="ПОДСКАЗКА", style="My.TButton")
    btn_hint.pack(side=LEFT, padx=100)

    style_lbl = ttk.Style()
    style_lbl.configure("My.TLabel", font=("Comic Sans MS", 20))

    yes_no_frame = ttk.Frame(window)
    yes_no_frame.pack(side=RIGHT, pady=(350, 0))
    btn_ya = ttk.Button(yes_no_frame, text="X", style="My.TButton", width=5, command=destroy)
    btn_ya.pack(side=RIGHT, ipady=20, padx=10)

    enter_frame = ttk.Frame(window)
    enter_frame.pack(pady=(int(window.winfo_screenheight()/2)+140, 0))

    btn_frame = ttk.Frame(window)
    btn_frame.pack(side=BOTTOM, pady=50)
    btn_i = ttk.Button(btn_frame, text="И", style="My.TButton", width=5, command=lambda:i_print(enter_frame, btn_i))
    btn_i.pack(side=LEFT, ipady=20, padx=10)
    btn_m = ttk.Button(btn_frame, text="М", style="My.TButton", width=5, command=lambda:m_print(enter_frame))
    btn_m.pack(side=LEFT, ipady=20, padx=10)
    btn_p = ttk.Button(btn_frame, text="П", style="My.TButton", width=5, command=lambda:p_print(enter_frame))
    btn_p.pack(side=LEFT, ipady=20, padx=10)
    btn_r = ttk.Button(btn_frame, text="Р", style="My.TButton", width=5, command=lambda:r_print(enter_frame))
    btn_r.pack(side=LEFT, ipady=20, padx=10)
    btn_o = ttk.Button(btn_frame, text="О", style="My.TButton", width=5, command=lambda:o_print(enter_frame))
    btn_o.pack(side=LEFT, ipady=20, padx=10)
    btn_v = ttk.Button(btn_frame, text="В", style="My.TButton", width=5, command=lambda:v_print(enter_frame))
    btn_v.pack(side=LEFT, ipady=20, padx=10)
    btn_i = ttk.Button(btn_frame, text="И", style="My.TButton", width=5, command=lambda:i_print(enter_frame, btn_i))
    btn_i.pack(side=LEFT, ipady=20, padx=10)
    btn_c = ttk.Button(btn_frame, text="З", style="My.TButton", width=5, command=lambda:z_print(enter_frame))
    btn_c.pack(side=LEFT, ipady=20, padx=10)
    btn_a = ttk.Button(btn_frame, text="А", style="My.TButton", width=5, command=lambda:a_print(enter_frame))
    btn_a.pack(side=LEFT, ipady=20, padx=10)
    btn_z = ttk.Button(btn_frame, text="Ц", style="My.TButton", width=5, command=lambda:c_print(enter_frame))
    btn_z.pack(side=LEFT, ipady=20, padx=10)
    btn_i = ttk.Button(btn_frame, text="И", style="My.TButton", width=5, command=lambda:i_print(enter_frame, btn_i))
    btn_i.pack(side=LEFT, ipady=20, padx=10)
    btn_ya = ttk.Button(btn_frame, text="Я", style="My.TButton", width=5, command=lambda:ya_print(enter_frame))
    btn_ya.pack(side=LEFT, ipady=20, padx=10)



def level_2():

    for widget in window.winfo_children():
        widget.destroy()

    btn_menu = ttk.Button(window, text="МЕНЮ", style="My.TButton", width=8, command=menu)
    btn_menu.pack(anchor="nw", pady=20, padx=20)
    btn_lvls = ttk.Button(window, text="УРОВНИ", style="My.TButton", width=8, command=levels_menu)
    btn_lvls.place(x=180, y=20)
    btn_hint = ttk.Button(window, text="ПОДСКАЗКА", style="My.TButton")
    btn_hint.place(x=1070, y=20)

    lbl_lvl2 = ttk.Label(window, text="УРОВЕНЬ 2", font=("Comic Sans MS", 30))
    lbl_lvl2.place(x=540, y=20)


def level_3():
    for widget in window.winfo_children():
        widget.destroy()

    btn_menu = ttk.Button(window, text="МЕНЮ", style="My.TButton", width=8, command=menu)
    btn_menu.pack(anchor="nw", pady=20, padx=20)
    btn_lvls = ttk.Button(window, text="УРОВНИ", style="My.TButton", width=8, command=levels_menu)
    btn_lvls.place(x=180, y=20)
    btn_hint = ttk.Button(window, text="ПОДСКАЗКА", style="My.TButton")
    btn_hint.place(x=1070, y=20)

    lbl_lvl3 = ttk.Label(window, text="УРОВЕНЬ 3", font=("Comic Sans MS", 30))
    lbl_lvl3.place(x=540, y=20)


def level_4():
    for widget in window.winfo_children():
        widget.destroy()

    btn_menu = ttk.Button(window, text="МЕНЮ", style="My.TButton", width=8, command=menu)
    btn_menu.pack(anchor="nw", pady=20, padx=20)
    btn_lvls = ttk.Button(window, text="УРОВНИ", style="My.TButton", width=8, command=levels_menu)
    btn_lvls.place(x=180, y=20)
    btn_hint = ttk.Button(window, text="ПОДСКАЗКА", style="My.TButton")
    btn_hint.place(x=1070, y=20)

    lbl_lvl4 = ttk.Label(window, text="УРОВЕНЬ 4", font=("Comic Sans MS", 30))
    lbl_lvl4.place(x=540, y=20)


window = Tk()
window.attributes("-fullscreen", True)
window.resizable(False, False)
window.config(cursor="heart")
menu()
window.mainloop()