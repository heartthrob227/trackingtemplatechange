from app import app
from app import tkinter

master = Tk()
e = entry(master)
e.pack()

e.focus_set()


@app.route('/')
@app.route('/index')
@app.route('/input')

def index():
    return "Hello, World!"
	
def input():
	print e.get()
