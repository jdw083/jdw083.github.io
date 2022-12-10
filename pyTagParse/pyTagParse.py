# Python program to read ignition tags json export
# JDW 12/8/2022

#imports
import json, re, os
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from os.path import exists


#select file
def select_file():
    filetypes = (       
        ('JSON files', '*.json'),
        ('text files', '*.txt'),
        ('All files', '*.*')
    )

    filename = filedialog.askopenfilename(
        title = 'Open A File',
        initialdir = '/',
        filetypes = filetypes
    )

    if filename != '':
        messagebox.showinfo(
            title = 'Selected File',
            message = 'File Selected Successfully'
        )
    else:
        messagebox.showerror(
            title = 'Selected File',
            message = 'No File Selected'
        )

    lbl_file_selected.configure(text = str(filename))

    
#set up parse info
def parse_tags_start():


    #vars
    f = open(lbl_file_selected.cget('text'))
    data = json.load(f)


    #choose save file path
    filetypes = [       
        ('CSV files', '*.csv'),
    ]
    export_file = filedialog.asksaveasfile(filetypes = filetypes, defaultextension = filetypes, mode = 'a')


    #check for a selected file
    if export_file.name == '':
        messagebox.showerror(
            title = 'Message',
            message = 'No File Selected'
        )
    
        return

    else:

        messagebox.showinfo(
            title = 'Message',
            message = 'File Will Be Saved As:\n\n' + export_file.name
        )

    #set global files
    global file
    global folder_path
    file = open(export_file.name,'w')
    

    #write your headers then loop through the rest of the 
    if checked.get() == 1:
        file.write('sep=|\n')

    file.write('Source|Query/Expression|Tag Path|Data Type|Tag Name|Type|Folder Path\n')

    for i in range(0,len(data['tags'])):    
        parse_tags(data['tags'][i],'')         

           
    #close JSON file after working with it
    f.close()
    file.close()


    if exists(export_file.name):
        messagebox.showinfo(
            title = 'Message',
            message = 'CSV Created Successfully'
        )

        if checked.get() == 1:
            os.system('start EXCEL.EXE ' + export_file.name)

        return
    else:
        messagebox.showerror(
            title = 'Message',
            message = 'There Was A Problem Saving The File'
        )
        return


#function used to parse entire JSON file for the following keys
#listed in "headers" variable below
def parse_tags(json_object,folder_path):

    #vars
    headers = ['valueSource','expression','opcItemPath','dataType','name','tagType','query']
    source = ''
    tag_type = ''
    query = ''
    name = ''
    path = ''
    expr = ''
    data_type = ''


    #loops through JSON tag structure
    if type(json_object) is dict and json_object:
        for key in json_object:
            if headers.__contains__(key):
                if json_object[key] == 'Folder':                    
                    folder_path += name + '/'
                    print(folder_path)
                #conditionals
                if key == 'tagType' and json_object[key] != '':
                    print(json_object[key] + '|')
                    tag_type = json_object[key]

                elif key == 'expression':
                    print(re.sub(r'\s', ' ', json_object[key]) + '|')
                    expr = re.sub(r'\s', ' ', json_object[key])

                elif key == 'query':
                    print(re.sub(r'\s', ' ', json_object[key]) + '|')
                    query = re.sub(r'\s', ' ', json_object[key])

                elif key == 'name':
                    print(json_object[key] + '|')
                    name = json_object[key]

                elif key == 'valueSource':
                    print(json_object[key] + '|')
                    source = json_object[key]

                elif key == 'opcItemPath':
                    print(json_object[key] + '|')
                    path = json_object[key]

                elif key == 'dataType':
                    print(json_object[key] + '|')
                    data_type = json_object[key]

                else:
                    print(json_object[key] + '|')  
                        
        #keep going to the next loop
        parse_tags(json_object[key],folder_path)

        
        #file write conditionals for each row
        if source == 'db':
            file.write(
                source + '|' +
                query + '|' +
                '|' +
                data_type + '|' +
                name + '|' +
                tag_type + '|' +
                folder_path + '\n'
            )
        elif source == 'opc':
            file.write(
                source + '|' +
                '|' +
                path + '|' +
                data_type + '|' +
                name + '|' +
                tag_type + '|' +
                folder_path + '\n'
            )
        elif source == 'expr':
            file.write(
                source + '|' +
                expr + '|' +
                '|' +
                data_type + '|' +
                name + '|' +
                tag_type + '|' +
                folder_path + '\n'
            )
        elif source == 'memory':
            return
        elif tag_type == 'Folder':  
            return


    #elseif statement if object is a list
    elif type(json_object) is list and json_object:
        for item in json_object:
            parse_tags(item,folder_path)

           
#Tkinter GUI
window = Tk()
window.title('Ignition Tag Parser Program')
window.geometry('600x300')


#vars
checked = IntVar(value = 1)


#labels and buttons
menu = Menu(window)
filemenu = Menu(menu, tearoff = 0)
filemenu.add_command(label = 'Exit Program', command = window.destroy)
menu.add_cascade(label = 'File', menu = filemenu)


lbl = Label(window, text = '1. Choose JSON Tags File', font = ("Arial Bold", 12))
lbl.place(relx = 0.5, rely = 0.1, anchor = CENTER)


btn = Button(window, text = 'Select File', command = select_file, relief = RAISED)
btn.place(relx = 0.5, rely = 0.2, anchor = CENTER)


lbl2 = Label(window, text = 'JSON Tag File Selected:', font = ("Arial Bold", 12))
lbl2.place(relx = 0.5, rely = 0.3, anchor = CENTER)


lbl_file_selected = Label(window, text = '~', font = ("Arial", 12))
lbl_file_selected.place(relx = 0.5, rely = 0.4, anchor = CENTER)


lbl_parse_when_ready = Label(window, text = '2. Parse JSON And Convert To CSV', font = ("Arial Bold", 12))
lbl_parse_when_ready.place(relx = 0.5, rely = 0.6, anchor = CENTER)


chk_using_excel = Checkbutton(window, text = 'Open In Excel (Default)', variable = checked, onvalue = 1, offvalue = 0)
chk_using_excel.place(relx = 0.5, rely = 0.7, anchor = CENTER)


btn_parse = Button(window, text = 'Begin Conversion To CSV', command = parse_tags_start, relief = RAISED)
btn_parse.place(relx = 0.5, rely = 0.8, anchor = CENTER)


window.config(menu = menu)
#run
window.mainloop()
