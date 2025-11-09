from tkinter import Tk
from ui.chat_window import ChatWindow

def main():
    root = Tk()
    app = ChatWindow(root)
    root.mainloop()

if __name__ == "__main__":
    main()
