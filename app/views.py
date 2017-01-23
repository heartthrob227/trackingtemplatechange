from app import app
from app import tkinter

master = Tk()
e = entry(master)
e.pack()

e.focus_set()


@app.route('/')
@app.route('/index')


def index():
    return "Hello, World!"
	
