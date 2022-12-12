# Python program to read ignition tags json export
# JDW 12/8/2022

#imports
import json, re, os, xmltodict
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from os.path import exists


#select file
def select_file():
    filetypes = (       
        ('JSON files', '*.json'),
        ('XML files', '*.xml')
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
    if lbl_file_selected.cget('text').endswith('.xml'):
        f = open(lbl_file_selected.cget('text'),'rb')
        data = xmltodict.parse(f)
    else:
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
    

    #write your headers then loop through the rest of the respective function
    if checked.get() == 1:
        file.write('sep=|\n')
    
    #XML
    if lbl_file_selected.cget('text').endswith('.xml'):        
        file.write('TAG NAME|TARGET_DATA_TYPE|OPCITEMPATH|TARGET_NAME|TARGET_TYPE\n')

        parse_tags_xml(data)        
        
    #JSON
    else:
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
                
                #JSON conditionals
                if json_object[key] == 'Folder':                    
                    folder_path += name + '/'
                    print(folder_path)                  
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
        #print('hello2')
        for item in json_object:
            parse_tags(item,folder_path)


def parse_tags_xml(data):
    for i in data['Project']['Groups']['GroupConfig']:
            if i =='@name':
                file.write('Transaction Group Name: ' + data['Project']['Groups']['GroupConfig'][i] + '\n') 
                print('Transaction Group Name: ' + data['Project']['Groups']['GroupConfig'][i] + '\n')


            if i =='Property':
                x = data['Project']['Groups']['GroupConfig']['Property']
                for j in range(0,len(x)):

                    if x[j]['@name'] == 'TABLE_NAME':
                        file.write('Table Name: ' + x[j]['#text'] + '\n')
                        print('Table Name: ' + x[j]['#text'] + '\n')

                    elif x[j]['@name'] == 'DATA_SOURCE':
                        file.write('Data Source: ' + x[j]['#text'] + '\n')
                        print('Data Source: ' + x[j]['#text'] + '\n')

                    elif x[j]['@name'] == 'CONFIGURED_ITEMS':
                        y = x[j]['ItemConfig']

                        for k in range(len(y)):
                            file.write(y[k]['@name'] + '|')
                            print(y[k]['@name'] + '|')
                            z = y[k]['Property']

                            for l in z:
                                if l['@name'] == 'TARGET_DATA_TYPE':
                                    if l.get('#text'):
                                        if l['#text'] in ['0','1','2','3']:
                                            file.write('int|')
                                            print('int|')
                                        elif l['#text'] in ['4','5']:
                                            file.write('float|')
                                            print('float|')
                                        elif l['#text'] == '6':
                                            file.write('boolean|')
                                            print('boolean|')
                                        elif l['#text'] == '7':
                                            file.write('string|')
                                            print('string')
                                        elif l['#text'] == '8':
                                            file.write('datetime|')
                                            print('datetime|')
                                        elif l['#text'] == '9':
                                            file.write('text|')
                                            print('text|')
                                        elif l['#text'] in ['10','11','12','13']:
                                            file.write('int array|')
                                            print('int array|')
                                        elif l['#text'] in ['14','15']:
                                            file.write('float array|')
                                            print('float array|')
                                        elif l['#text'] == '16':
                                            file.write('boolean array|')
                                            print('boolean array|')
                                        elif l['#text'] == '17':
                                            file.write('string array|')
                                            print('string array|')
                                        elif l['#text'] == '18':
                                            file.write('datetime array|')
                                            print('datetime array|')
                                        elif l['#text'] == '19':
                                            file.write('byte array|')
                                            print('byte array|')
                                        elif l['#text'] == '20':
                                            file.write('dataset|')
                                            print('dataset|')
                                        elif l['#text'] == '21':
                                            file.write('document|')
                                            print('document|')
                                        else:
                                            file.write(l['#text'] + '|')
                                            print(l['#text'] + '|')
                                    else:
                                        file.write('|')

                                if l['@name'] == 'OPCITEMPATH':
                                    if l.get('#text'):
                                        file.write(l['#text'] + '|')
                                        print(l['#text'] + '|')
                                    else:
                                        file.write('|')

                                if l['@name'] == 'TARGET_NAME':
                                    if l.get('#text'):
                                        file.write(l['#text'] + '|')
                                        print(l['#text'] + '|')
                                    else:
                                        file.write('|')

                                if l['@name'] == 'TARGET_TYPE':
                                    if l.get('#text'):
                                        if l['#text'] == '0':
                                            file.write('read-only\n')
                                            print('read-only\n')
                                        elif l['#text'] == '1':
                                            file.write('SQL column\n')
                                            print('SQL column\n')
                                        else:
                                            file.write(l['#text'] + '\n')
                                            print(l['#text'] + '\n')
                                    else:
                                        file.write('\n')

           
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


lbl = Label(window, text = '1. Choose JSON/XML Tags File', font = ("Arial Bold", 12))
lbl.place(relx = 0.5, rely = 0.1, anchor = CENTER)


btn = Button(window, text = 'Select File', command = select_file, relief = RAISED)
btn.place(relx = 0.5, rely = 0.2, anchor = CENTER)


lbl2 = Label(window, text = 'JSON/XML Tag File Selected:', font = ("Arial Bold", 12))
lbl2.place(relx = 0.5, rely = 0.3, anchor = CENTER)


lbl_file_selected = Label(window, text = '~', font = ("Arial", 12))
lbl_file_selected.place(relx = 0.5, rely = 0.4, anchor = CENTER)


lbl_parse_when_ready = Label(window, text = '2. Parse JSON/XML And Convert To CSV', font = ("Arial Bold", 12))
lbl_parse_when_ready.place(relx = 0.5, rely = 0.6, anchor = CENTER)


chk_using_excel = Checkbutton(window, text = 'Open In Excel (Default)', variable = checked, onvalue = 1, offvalue = 0)
chk_using_excel.place(relx = 0.5, rely = 0.7, anchor = CENTER)


btn_parse = Button(window, text = 'Begin Conversion To CSV', command = parse_tags_start, relief = RAISED)
btn_parse.place(relx = 0.5, rely = 0.8, anchor = CENTER)


window.config(menu = menu)
#run
window.mainloop()