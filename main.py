from my_game import GUI
import tkinter


if __name__ == '__main__':
    root = tkinter.Tk()
    root.title('Breakout!')

    app = GUI.GUI(root)
    root.mainloop()
