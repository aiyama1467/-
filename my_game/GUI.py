import tkinter
from tkinter import font
from my_game import app


class GUI(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.configure(width=600, height=500, bg='black')
        self.play = None
        self.application = None
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        _font = font.Font(family='MS Serif', size=70, weight='bold')
        breakout = tkinter.Label(self, text='Breakout', foreground='white', background='black', font=_font)
        breakout.pack(side='top')

        _font_for_button = font.Font(family='MS Serif', size=40, weight='bold')
        self.play = tkinter.Button(self, font=_font_for_button)
        self.play['text'] = 'Play!'
        self.play['borderwidth'] = 1
        self.play['relief'] = 'ridge'
        self.play['command'] = self.play_game
        self.play.pack(side='top')

        try:
            with open('readme.txt', encoding='utf-8', mode='r') as rm:
                _readme = rm.read()
            _font_for_readme = font.Font(family='MS Serif', size=20, weight='bold')
            readme = tkinter.Text(self, font=_font_for_readme, foreground='white', background='black')
            readme.insert('1.0', _readme)
            readme.pack()
        except FileNotFoundError as e:
            pass


    def play_game(self):
        self.application = app.App()
        self.application.on_execute()
