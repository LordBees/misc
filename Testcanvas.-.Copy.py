from tkinter import *
window_main = Tk()
cvs = Canvas(window_main,height = '300',width = '300')
ovalk = cvs.create_oval(7,7,5,5,outline = 'red')
top = cvs.create_line(0, 0, 640, 0, fill='green', tags=('top'))

#image = cvs.create_image(50, 50, anchor=NE, image=PhotoImage(file = "testhuan.png"))

cvs.pack()
def onKeyPress(event):
    key = ord(event.char)
    print(event.char)
    #if key == 'a':
    #elif key == 'a':
    if key == ('dsl2'):
        pass
##    if key == '!':
##    elif key == '"':
##    elif key == '#':
##    elif key == '$':
##    elif key == '%':
##    elif key == '&':
##    elif key == "'":
##    elif key == '(':
##    elif key == ')':
##    elif key == '*':
##    elif key == '+':
##    elif key == ',':
##    elif key == '-':
##    elif key == '.':
##    elif key == '/':
##    elif key == '0':
##    elif key == '1':
##    elif key == '2':
##    elif key == '3':
##    elif key == '4':
##    elif key == '5':
##    elif key == '6':
##    elif key == '7':
##    elif key == '8':
##    elif key == '9':
##    elif key == ':':
##    elif key == ';':
##    elif key == '<':
##    elif key == '=':
##    elif key == '>':
##    elif key == '?':
##    elif key == '@':
##    elif key == 'A':
##    elif key == 'B':
##    elif key == 'C':
##    elif key == 'D':
##    elif key == 'E':
##    elif key == 'F':
##    elif key == 'G':
##    elif key == 'H':
##    elif key == 'I':
##    elif key == 'J':
##    elif key == 'K':
##    elif key == 'L':
##    elif key == 'M':
##    elif key == 'N':
##    elif key == 'O':
##    elif key == 'P':
##    elif key == 'Q':
##    elif key == 'R':
##    elif key == 'S':
##    elif key == 'T':
##    elif key == 'U':
##    elif key == 'V':
    elif key == 'W':
        ovalk.move(1,1)
##    elif key == 'X':
##    elif key == 'Y':
##    elif key == 'Z':
##    elif key == '[':
##    elif key == '\':
##    elif key == ']':
##    elif key == '^':
##    elif key == '_':
##    elif key == '`':
##    elif key == 'a':
##    elif key == 'b':
##    elif key == 'c':
##    elif key == 'd':
##    elif key == 'e':
##    elif key == 'f':
##    elif key == 'g':
##    elif key == 'h':
##    elif key == 'i':
##    elif key == 'j':
##    elif key == 'k':
##    elif key == 'l':
##    elif key == 'm':
##    elif key == 'n':
##    elif key == 'o':
##    elif key == 'p':
##    elif key == 'q':
##    elif key == 'r':
##    elif key == 's':
##    elif key == 't':
##    elif key == 'u':
##    elif key == 'v':
##    elif key == 'w':
##    elif key == 'x':
##    elif key == 'y':
##    elif key == 'z':
##    elif key == '{':
##    elif key == '|':
##    elif key == '}':
##    elif key == '~':
    
def asciidump_ext():
    for x in range(0,255):
        print("elif key == '"+chr(x)+"':")
        
window_main.bind('<KeyPress>', onKeyPress)
window_main.mainloop()


	
