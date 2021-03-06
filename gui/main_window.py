# -*- coding: utf8 -*-
import tkinter
from tkinter import ttk
from tkinter import filedialog


class Gui:
    def __init__(self, coding_provider):
        self.root = tkinter.Tk()
        self.root.geometry("405x340")
        self.waiting = True
        self.coding_provider = coding_provider
        self.coding_provider.escape_to_connection = self.connection
        self.coding_provider.to_main_window = self.main_window
        self.coding_provider.quit_gui = self.quit
        self.connect_panel = None
        self.connect_label = None
        self.connect_but = None
        self.main_panel = None
        self.connect_state = None
        self.connect = None
        self.state = False
        self.message = None
        self.general_chat = None
        self.history_messages = None
        self.previous_main = True
        self.file_entry = None
        self.history_panel = None
        self.widget_list = []

        self.connection(None)
        self.root.mainloop()

    def connection(self, event):
        try:
            self.main_panel.destroy()
        except: pass

        self.root.geometry("460x340")
        self.root.title("Main station")
        self.connect_panel =tkinter.Frame(self.root, width=450, height=350, relief=tkinter.GROOVE, bd=2)
        self.connect_panel.place(x=25, y=35)
        self.connect_label = tkinter.Label(self.root, text='Соединение')
        self.connect_label.place(x=25, y=5)
        self.connect_but = tkinter.Button(self.root, text='Соединить', width=12)
        self.connect_but.place(y=304, x=346)

        login_label = tkinter.Label(self.connect_panel, text='Логин')
        login_entry = tkinter.Entry(self.connect_panel, width=35)
        port_label = tkinter.Label(self.connect_panel, text='Параметры COM порта:')
        speed_label = tkinter.Label(self.connect_panel, text='Скорость (бит/с)')
        speed_box = ttk.Combobox(self.connect_panel, width=35)
        speed_box.config(values=[
            u"50",
            u"75",
            u"110",
            u"150",
            u"300",
            u"600",
            u"1200",
            u"2400",
            u"4800",
            u"9600",
            u"19200",
            u"38400",
            u"57600",
            u"115200"
        ])
        speed_box.set(u"9600")
        bit_data_label = tkinter.Label(self.connect_panel, text='Биты данных')
        bit_data_box = ttk.Combobox(self.connect_panel, width=35)
        bit_data_box.config(values=[
            u"5",
            u"6",
            u"7",
            u"8"
        ])
        bit_data_box.set(u"8")
        stop_bit_label = tkinter.Label(self.connect_panel, text='Стоп биты')
        stop_bit_box = ttk.Combobox(self.connect_panel, width=35)
        stop_bit_box.config(values=[
            u"1",
            u"1.5",
            u"2"
        ])
        stop_bit_box.set(u"1")
        # тут возможны варианты NONE, EVEN, ODD, MARK, SPACE
        parity_label = tkinter.Label(self.connect_panel, text='Четность')
        parity_box = ttk.Combobox(self.connect_panel, width=35)
        parity_box.config(values=[
            u"Отсутствует",
            u"Дополнение до четности",
            u"Дополнение до нечетности",
            u"Всегда 1",
            u"Всегда 0"
        ])
        parity_box.set(u"Отсутствует")

        self.widget_list.extend([login_entry, speed_box, bit_data_box, stop_bit_box, parity_box])

        login_label.grid(row=0, column=0, sticky='w', padx=10, pady=10)
        login_entry.grid(row=0, column=1, sticky='w', padx=10, pady=10)
        port_label.grid(row=1, column=0, sticky='w', padx=10, pady=10)
        speed_label.grid(row=2, column=0, sticky='w', padx=10, pady=10)
        speed_box.grid(row=2, column=1, sticky='w', padx=10, pady=10)
        bit_data_label.grid(row=3, column=0, sticky='w', padx=10, pady=10)
        bit_data_box.grid(row=3, column=1, sticky='w', padx=10, pady=10)
        stop_bit_label.grid(row=4, column=0, sticky='w', padx=10, pady=10)
        stop_bit_box.grid(row=4, column=1, sticky='w', padx=10, pady=10)
        parity_label.grid(row=5, column=0, sticky='w', padx=10, pady=10)
        parity_box.grid(row=5, column=1, sticky='w', padx=10, pady=10)

        self.connect_but.bind('<Button-1>', self.connect_to_main)

    def connect_to_main(self, event):
        if self.widget_list[0].get() != '':
            self.coding_provider.coding_connection(self.widget_list[0].get(),
                                                   self.widget_list[1].get(),
                                                   self.widget_list[2].get(),
                                                   self.widget_list[3].get(),
                                                   self.widget_list[4].get())

    def main_window(self):
        try:
            self.history_panel.destroy()
        except: pass
        try:
            self.connect_panel.destroy()
            self.connect_but.destroy()
        except: pass
        self.state = True
        self.previous_main = True

        self.connect_label.config(text='Главная')
        self.root.geometry('680x535')
        self.main_panel = tkinter.Frame(self.root, width=630, height=495)
        self.general_chat = tkinter.Text(self.main_panel, height=20, width=79, wrap=tkinter.WORD)
        message_label = tkinter.Label(self.main_panel, text='Сообщение:')
        self.message = tkinter.Entry(self.main_panel, width=75)
        file_label = tkinter.Label(self.main_panel, text='Файл:')
        self.file_entry = tkinter.Entry(self.main_panel, width=52)
        open_but = tkinter.Button(self.main_panel, text='Открыть', width=14)
        send_message = tkinter.Button(self.main_panel, text='Отправить', width=20)
        self.connect = tkinter.Button(self.main_panel, text='Разединить', width=15)
        self.connect_state = tkinter.Label(self.main_panel, text='Подключено')
        history = tkinter.Button(self.main_panel, text='История', width=15)
        quit = tkinter.Button(self.main_panel, text='Выход', width=15)

        self.main_panel.place(x=25, y=35)
        self.general_chat.place(x=0, y=0)
        message_label.place(x=0, y=330)
        self.message.place(x=0, y=355)
        file_label.place(x=0, y=385)
        self.file_entry.place(x=0, y=410)
        open_but.place(x=345, y=406)
        send_message.place(x=480, y=351)
        # x = 304, y = 420
        self.connect.place(x=0, y=460)
        self.connect_state.place(x=130, y=463)
        history.place(x=395, y=463)
        quit.place(x=515, y=463)

        self.coding_provider.encoding_thread.textbox = self.general_chat
        self.coding_provider.decoding_thread.textbox = self.general_chat

        self.connect.bind('<Button-1>', self.change_state)
        send_message.bind('<Button-1>', self.send)
        history.bind('<Button-1>', self.history_window)
        open_but.bind('<Button-1>', self.load_file)
        quit.bind('<Button-1>', self.escape_to_connection)

    def escape_to_connection(self, event):
        self.coding_provider.initiator = True
        self.coding_provider.coding_disconnection()

    def history_window(self, event):
        self.connect_label.config(text='История сообщений')
        self.main_panel.destroy()

        self.history_panel = tkinter.Frame(self.root, height=500, width=650)
        self.history_messages = tkinter.Text(self.history_panel, height=27, width=77, wrap=tkinter.WORD, state='disabled')
        save = tkinter.Button(self.history_panel, text='Сохранить', width=15)
        clean = tkinter.Button(self.history_panel, text='Очистить', width=15)
        escape = tkinter.Button(self.history_panel, text='Назад', width=15)

        self.history_panel.place(x=25, y=35)
        self.history_messages.place(x=0, y=0)
        save.place(x=275, y=460)
        clean.place(x=395, y=460)
        escape.place(x=515, y=460)

        save.bind('<Button-1>', self.save_history)
        clean.bind('<Button-1>', self.clean_history)
        escape.bind('<Button-1>', self.escape_handler)

    def save_history(self, event):
        hist = self.history_messages.get(1.0, 'end')
        # hist = u'{}'.format(hist)
        _file = filedialog.asksaveasfilename(initialdir="C:/Users/azeng/Documents/6 семестр/сети/курсач", title="Select file")
        if _file == '':
            return
        with open(_file, 'w') as file_txt:
            file_txt.write(hist)

    def clean_history(self, event):
        # сделать удаление из бд (документа, где будет храниться история)
        self.history_messages.delete(1.0, tkinter.END)

    def escape_handler(self, event):
        if self.previous_main:
            self.main_window()
        # else:
        #     # дописать возврат к личным сообщениям определенного юзера
        #     self.private_messages_window(None)

    def change_state(self, event):
        if self.state:
            self.state = False
            self.connect_state.config(text='Отключено')
            self.connect.config(text='Соединить')
        else:
            self.state = True
            self.connect_state.config(text='Подключено')
            self.connect.config(text='Разъединить')
        self.coding_provider.disconnection(self.state)

    def send(self, event):
        if self.message.get() is not None and self.message.get() != '':
            self.coding_provider.coding_message(self.message.get())
        self.message.delete(0, tkinter.END)

    def load_file(self, event):
        _file = filedialog.askopenfilename(initialdir="/", title="Select file")
        if _file == '':
            return
        self.file_entry.delete(0, 'end')
        self.file_entry.insert(0, _file)

    def quit(self):
        self.coding_provider.com_provider.quit()
        self.coding_provider.quit()
        self.root.quit()


