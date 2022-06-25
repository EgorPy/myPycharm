import tkinter
from tkinter import filedialog
from io import StringIO
from contextlib import redirect_stdout
import traceback


def show_menu_buttons():
    global menuOpened
    if not menuOpened:
        buttonOpenFile.grid()
        buttonSaveFile.grid()
        buttonInfo.grid()
        buttonExit.grid()
        menuOpened = True
        return None
    if menuOpened:
        buttonOpenFile.grid_remove()
        buttonSaveFile.grid_remove()
        buttonInfo.grid_remove()
        buttonExit.grid_remove()
        menuOpened = False
        return None


def exit_program():
    exit(0)


def change_buttonMenu_color_1(event):
    buttonMenu.config(foreground='cyan')


def change_buttonOpenFile_color_1(event):
    buttonOpenFile.config(foreground='cyan')


def change_buttonSaveFile_color_1(event):
    buttonSaveFile.config(foreground='cyan')


def change_buttonExit_color_1(event):
    buttonExit.config(foreground='cyan')


def change_buttonInfo_color_1(event):
    buttonInfo.config(foreground='cyan')


def change_buttonMenu_color_2(event):
    buttonMenu.config(foreground='black')


def change_buttonOpenFile_color_2(event):
    buttonOpenFile.config(foreground='black')


def change_buttonSaveFile_color_2(event):
    buttonSaveFile.config(foreground='black')


def change_buttonExit_color_2(event):
    buttonExit.config(foreground='black')


def change_buttonInfo_color_2(event):
    buttonInfo.config(foreground='black')


def openFile():
    files = [("TXT files", "*.txt"),
             ("PY files", "*.py"),
             ('HTML files', '*.html;*.htm'),
             ('All files', '*.*')]
    file = filedialog.askopenfile(filetype=files, defaultextension=files)
    f = open(file.name, 'r', encoding='UTF-8')
    mainText.insert(1.0, f.read())


def saveFile():
    files = [("TXT files", "*.txt"),
             ("PY files", "*.py"),
             ('HTML files', '*.html;*.htm'),
             ('All files', '*.*')]
    file = filedialog.asksaveasfilename(filetype=files, defaultextension=files, confirmoverwrite=True)
    f = open(file, 'w')
    s = mainText.get(1.0, 'end')
    f.write(s)


def info():
    global infoOpened
    if not infoOpened:
        mainText.delete(1.0, 'end')
        mainText.insert(1.0, 'Hello, this is a program for programming programs lol.\n\n'
                             'Press the "Menu" button to open menu.\n\n'
                             'In the menu press button "Open file" to open file.\n\n'
                             'If you want to create new file, just start typing your program here and then save your program '
                             'by clicking "Menu" button and clicking "Save file" button.\n\n'
                             'Open menu and click on "Info" button to open this info.\n\n'
                             'Open menu and click "Exit" to exit program.\n\n\n\n\n\n\n\n'
                             'Created by Egor.')
        infoOpened = True
        return None
    if menuOpened:
        mainText.delete(1.0, 'end')
        infoOpened = False
        return None


def compileProgram(event):
    output('process started')
    output('compiling...')
    try:
        code = compile(mainText.get(1.0, 'end'), 'file', 'exec')
        f = StringIO()
        with redirect_stdout(f):
            exec(code)
        output('')
        output('output:')
        output(f.getvalue())
        output('compiling completed successfully')
    except Exception:
        output(f'Error: {traceback.format_exc()}')
    output('process finished')


def output(text):
    outputText.insert('end', f'{str(text)}\n')


root = tkinter.Tk()
root.title('MyPycharm')
root.attributes('-fullscreen', True)
root.config(bg='#555555')

menuOpened = False
infoOpened = False

mainText = tkinter.Text(root, bg='#131e21', insertbackground='white', foreground='#00ff00', font=('Arial', 20),
                        wrap='word', height=20)
outputText = tkinter.Text(root, bg='#000000', insertbackground='white', foreground='#00ff00', font=('Arial', 20),
                          wrap='word', width=100)
frame = tkinter.Frame(root)
buttonMenu = tkinter.Button(frame, text='Menu', command=show_menu_buttons, width=10, bg='#555555', relief='solid',
                            activebackground='#555555', bd=1)
buttonOpenFile = tkinter.Button(frame, text='Open file', command=openFile, width=10, bg='#555555', relief='solid',
                                activebackground='#555555', bd=1)
buttonSaveFile = tkinter.Button(frame, text='Save file', command=saveFile, width=10, bg='#555555', relief='solid',
                                activebackground='#555555', bd=1)
buttonInfo = tkinter.Button(frame, text='Info', command=info, width=10, bg='#555555', relief='solid',
                            activebackground='#555555', bd=1)
buttonExit = tkinter.Button(frame, text='Exit', command=exit_program, width=10, bg='#555555', relief='solid',
                            activebackground='#555555', bd=1)

frame.pack(side='left', anchor='nw')
mainText.pack(fill='both', expand=1)
outputText.pack(anchor='s')
buttonMenu.grid(row=0, column=0, ipady=10)
buttonOpenFile.grid(row=2, column=0, sticky='n', ipady=10)
buttonSaveFile.grid(row=3, column=0, sticky='n', ipady=10)
buttonInfo.grid(row=4, column=0, sticky='n', ipady=10)
buttonExit.grid(row=5, column=0, sticky='n', ipady=10)

mainText.bind('<F5>', compileProgram)

buttonMenu.bind('<Enter>', change_buttonMenu_color_1)
buttonOpenFile.bind('<Enter>', change_buttonOpenFile_color_1)
buttonSaveFile.bind('<Enter>', change_buttonSaveFile_color_1)
buttonInfo.bind('<Enter>', change_buttonInfo_color_1)
buttonExit.bind('<Enter>', change_buttonExit_color_1)

buttonMenu.bind('<Leave>', change_buttonMenu_color_2)
buttonOpenFile.bind('<Leave>', change_buttonOpenFile_color_2)
buttonSaveFile.bind('<Leave>', change_buttonSaveFile_color_2)
buttonInfo.bind('<Leave>', change_buttonInfo_color_2)
buttonExit.bind('<Leave>', change_buttonExit_color_2)

buttonOpenFile.grid_remove()
buttonSaveFile.grid_remove()
buttonInfo.grid_remove()
buttonExit.grid_remove()

root.mainloop()
