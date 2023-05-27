from tkinter import*
from tkinter import messagebox
from tkinter.filedialog import askopenfile
from tkinter.filedialog import asksaveasfile


root = Tk()
root.geometry('900x610')
root.minsize(900,610)
# root.maxsize(900,610)
root.title("Kiril to Lotin")
root.configure(bg='light grey')


def view_lime():
    myButton.configure(background='PaleTurquoise', fg='black')
    bbutton.configure(background='PaleTurquoise', fg='black')
    return root.configure(bg='PaleTurquoise')

def view_grey():
    myButton.configure(background='grey', fg='black')
    bbutton.configure(background='grey', fg='black')
    return root.configure(bg='grey')

def view_white():
    myButton.configure(background='#D9DDDC', fg='black')
    bbutton.configure(background='#D9DDDC', fg='black')
    return root.configure(bg='white')

def view_dsg():
    myButton.configure(background='DarkSlateGray', fg='white')
    bbutton.configure(background='DarkSlateGray', fg='white')
    return root.configure(bg='DarkSlateGray')

def view_default():
    myButton.configure(background='light grey', fg='black')
    bbutton.configure(background='light grey', fg='black')
    return root.configure(bg='light grey')                                

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)

content=str(encoding="utf-8")

def open_file():
    file = askopenfile(mode="rb", initialdir = "/",title = "Select file",filetypes = (("text file","*.txt"),("pdf file","*.pdf"),("docx file","*.docx"), ("doc file","*.doc"),("all files","*.*")))
                                                
    
    if file is not None:
        content= file.read()
        inputtxt.insert('end',content)

def print_file():
    
   
    file_to_print = filedialog.askopenfilename(
      initialdir="/", title="Select file", 
      filetypes=(("Text files", "*.txt"), ("all files", "*.*")))
      
    if file_to_print:
        
        # Print Hard Copy of File
        win32api.ShellExecute(0, "print", file_to_print, None, ".", 0)   	

def box():
    messagebox.showinfo(title="Dasturchi haqida:",message="Ishlab chiquvchi: Mamaraimov Mirjalol.  bog'lanish uchun num:  _+998976112128_")


def boxes():
   messagebox.showwarning("Bu dasturning vazifasi.", " < Kiril > alifbosida yozilgan matnni < Lotin > alifbosidagi matnga o'girib beradi.")


def ClearAll():
    inputtxt.delete(1.0, END)
    output.delete(1.0, END)

def file_save():
    if len(inputtxt.get("1.0","end-1c"))!=0 and len(output.get("1.0","end-1c"))!=0:
        f = asksaveasfile(mode='w', defaultextension=".txt" , filetypes=[
                                                                                ('Text file',".txt"),
                                                                                ('Word files',".doc"),
                                                                                ('All file',".*")], initialdir = "dir", title = "Save as")
        if f is None: 
            return
        text2save = str(output.get(1.0, END)) 
        f.write(text2save)
        f.close()
        

def share():
    text= list(inputtxt.get("1.0","end-1c"))
    text.append(' ')

    new_text= str()
    if len(text)== 0 and len(output.get("1.0" , "end-1c")) !=0:
        messagebox.showerror("Error" , "Enter the text in the box provided!!!")
    output.delete("1.0" , END)
    
    for idx , i in enumerate(text):

        if i=='а':
            new_text+='а'
        elif i=='А':
            new_text+='A'
        elif i=='б':
             new_text+='b'
        elif i=='Б':
            new_text+='B'
        elif i=='с':
                new_text+='s'
        elif i=='С':
                new_text+='S'
        elif i=='д':
            new_text+='d'
        elif i=='Д':
            new_text+='D'
        elif i=='Е':
            new_text+='E'
        elif i=='е':
            new_text+='e'
        elif i=='л':
            new_text+='l'
        elif i=='Л':
            new_text+='L'
        elif i=='ч':
            new_text+='ch'
        elif i=='Ч':
            new_text+='CH'
        elif i=='Ф':
            new_text+='F'
        elif i=='ф':
            new_text+='f'
        elif i=='я':
            new_text+='ya'
        elif i=='Я':
            new_text+='YA'
        elif i=='м':
            new_text+='m'
        elif i=='М':
            new_text+='M'
        elif i=='О':
            new_text+='O'
        elif i=='о':
            new_text+='o'
        elif i=='И':
            new_text+='I'
        elif i=='и':
            new_text+='i'
        elif i=='З':
            new_text+='Z'
        elif i=='з':
            new_text+='z'
        elif i=='В':
            new_text+='V'
        elif i=='в':
            new_text+='v'
        elif i=='Ё':
            new_text+='YO'
        elif i=='ё':
            new_text+='yo'
        elif i=='Г':
            new_text+='G'
        elif i=='г':
            new_text+='g'
        elif i=='Ж':
            new_text+='J'
        elif i=='ж':
            new_text+='j'
        elif i=='Й':
            new_text+='Y'
        elif i=='й':
            new_text+='y'
        elif i=='К':
            new_text+='K'
        elif i=='к':
            new_text+='k'
        elif i=='Н':
            new_text+='N'
        elif i=='н':
            new_text+='n'
        elif i=='П':
            new_text+='P'
        elif i=='п':
            new_text+='p'
        elif i=='Р':
            new_text+='R'
        elif i=='р':
            new_text+='r'
        elif i=='Т':
            new_text+='T'
        elif i=='т':
            new_text+='t'
        elif i=='У':
            new_text+='U'
        elif i=='у':
            new_text+='u'
        elif i=='х':
            new_text+='x'
        elif i=='Х':
            new_text+='X'
        elif i=='Ю':
            new_text+='YU'
        elif i=='ю':
            new_text+='yu'
        elif i=='Ҳ':
            new_text+='H'
        elif i=='ҳ':
            new_text+='h'
        elif (i=="Ъ" or i=='ъ'):
            new_text+="'"
        elif (i=='Щ'):
            new_text+='SH'
        elif i=='щ':
            new_text+='sh'
        elif (i=='Ш'):
            new_text+='SH'
        elif i=='ш':
            new_text+='sh'
        elif i=='Ц':
            new_text+='TS'
        elif i=='ц':
            new_text+='ts'
        elif (i=='Ы'  or i=='ы'):
            new_text+=""
        elif (i=='ь' or i=='Ь'):
            new_text+=""
        elif i=='Э':
            new_text+='E'
        elif i=='э':
            new_text+='e'
        elif i=='ў':
            new_text+="o'"
        elif i=='Ў':
            new_text+="O'"
        elif i=='Қ':
            new_text+='Q'
        elif i=='қ':
            new_text+='q'



        elif i=='c':
            if text[idx + 1] == 'h':
                new_text += 'ч'
                del text[idx + 1]
            else:
                new_text+=''
        elif i=='C':
                if text[idx + 1] == 'h' or text[idx + 1] == 'H':
                       new_text += 'Ч'
                       del text[idx + 1]
                else:
                    new_text+=''
                    
        elif i=='а':
            new_text+='а'
        elif i=='A':
            new_text+='А'
        elif i=='b':
             new_text+='б'
        elif i=='B':
            new_text+='Б'
        elif i=='s':
            if text[idx + 1] == 'h':
                new_text += 'ш'
                del text[idx + 1]
            else:
                new_text+='с'

        elif i=='S':
                if (text[idx + 1] == 'h' or text[idx + 1] == 'H'):
                       new_text += 'Ш'
                       del text[idx + 1]
                else:
                    new_text+='С'
        elif i=='d':
            new_text+='д'
        elif i=='D':
            new_text+='Д'
        elif i=='E':
            new_text+='Е'
        elif i=='e':
            new_text+='е'
        elif i=='l':
            new_text+='л'
        elif i=='L':
            new_text+='Л'
        elif i=='F':
            new_text+='Ф'
        elif i=='f':
            new_text+='ф'
        elif i=='y':
            if text[idx + 1] == 'a':
                new_text += 'я'
                del text[idx+1]
            elif text[idx+1]=='o':
                new_text += 'ё'
                del text[idx + 1]
            elif text[idx+1]=='u':
                new_text += 'ю'
                del text[idx + 1]
            else:
                new_text+='й'

        elif i=='Y':
            if text[idx + 1] == 'A' or text[idx + 1] == 'a':
                new_text += 'Я'
                del text[idx+1]
            elif text[idx + 1] == 'O' or text[idx + 1] == 'o':
                new_text += 'Ё'
                del text[idx + 1]
            elif text[idx + 1] == 'U' or text[idx + 1] == 'u':
                new_text += 'Ю'
                del text[idx + 1]
            else:
                new_text+='Й'
        elif i=='m':
            new_text+='м'
        elif i=='M':
            new_text+='М'
        elif i=='I':
            new_text+='И'
        elif i=='i':
            new_text+='и'
        elif i=='Z':
            new_text+='З'
        elif i=='z':
            new_text+='з'
        elif i=='V':
            new_text+='В'
        elif i=='v':
            new_text+='в'
        elif i=='J':
            new_text+='Ж'
        elif i=='j':
            new_text+='ж'

        elif i=='K':
            new_text+='К'
        elif i=='k':
            new_text+='к'
        elif i=='N':
            new_text+='Н'
        elif i=='n':
            new_text+='н'
        elif i=='P':
            new_text+='П'
        elif i=='p':
            new_text+='п'
        elif i=='R':
            new_text+='Р'
        elif i=='r':
            new_text+='р'

        elif i=='U':
            new_text+='У'
        elif i=='u':
            new_text+='у'
        elif i=='x':
            new_text+='х'
        elif i=='X':
            new_text+='Х'
        elif i=='H':
            new_text+='Ҳ'
        elif i=='h':
            new_text+='ҳ'
        elif (i=='\''):
            new_text+="ъ"
        elif i=='T':
            if text[idx + 1] == 'S' or text[idx + 1] == 's':
                new_text += 'Ц'
                del text[idx+1]
            else:
                new_text+='Т'
        elif i=='t':
            if text[idx + 1] == 's':
                new_text += 'ц'
                del text[idx+1]
            else:
                new_text+='т'
        elif i=='E':
            new_text+='Э'
        elif i=='e':
            new_text+='э'
        elif i=='o':
            if text[idx + 1] == '\'':
                new_text += 'ў'
                del text[idx+1]
            else:
                new_text+="о"
        elif i=='O':
            if text[idx + 1] == '\'':
                new_text += 'Ў'
                del text[idx+1]
            else:

                new_text+="О"


        elif i=='g':
            if str(text[idx + 1]) == "'":
                new_text += 'ғ'
                del text[idx + 1]
            else:
                new_text+="g"
        elif i=='G':
            if str(text[idx + 1]) == "'":
                new_text += 'Ғ'
                del text[idx+1]
            else:
                new_text+="G"
        elif i=='Q':
            new_text+='Қ'
        elif i=='q':
            new_text+='қ'
        else:
            new_text+=i

    output.insert("1.0", new_text)

inputtxt=Text(root, bg='#F5FFFA', width =100, height=15)
inputtxt.pack(expand=True, fill=BOTH, padx=10, pady = 10)


myButton=Button(root,text='Convert' ,fg="Black", command = share, background='light grey')
myButton.pack(fill=BOTH,pady=5,padx=10)

output= Text(root, bg="#F5FFFA", width =100, height=15)
output.pack(expand=True, fill=BOTH, padx=10, pady = 10)


bbutton=Button(root,text="Clear",fg="Black",command=ClearAll, background='light grey')
bbutton.pack(fill=BOTH,pady=10,padx=10)

filemenu.add_command(label="New", command=None)
filemenu.add_command(label="Open", command=open_file)
filemenu.add_command(label="Save", command=file_save)
filemenu.add_command(label="Print", command=print_file)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.destroy)

menubar.add_cascade(label="File", menu=filemenu)

viewmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="View", menu=viewmenu)
viewmenu.add_command(label="Lime", command=view_lime)
viewmenu.add_command(label="DarkSlateGray", command=view_dsg)
viewmenu.add_command(label="White", command=view_white)
viewmenu.add_command(label="Gray", command=view_grey)
viewmenu.add_command(label="Default", command=view_default)

helpmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=box)
helpmenu.add_command(label="Help Index", command=boxes)


root.call('encoding', 'system', 'utf-8')
root.config(menu=menubar)
mainloop()

