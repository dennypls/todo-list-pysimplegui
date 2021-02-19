import PySimpleGUI as sg

list = ["try to learn python", "get frustrated and cry", "listen to sad boy music", "look out the window and contemplate life"]

layout = [ [sg.Button ('Add to list'), sg.Button ('Delete task'), sg.Button('Clear all tasks')],
           [sg.In(key='input')],
           [sg.Text('Current task(s):')],
           [sg.Listbox(values=list, size=(50,10), key="output"), sg.Button('Miracle Button')]]

window = sg.Window('To-do List', layout)

while True:             # Event Loop
    event, values = window.read()
    if event == 'Add to list':
        list.append(values['input'])
        window.FindElement('output').Update(values=list)
        window['input'].update('')
    if event == 'Delete task':
        list.remove(values['output'][0])
        window.FindElement('output').Update(values=list)
    if event == 'Miracle Button':
        if len(list)>1:
            sg.popup("Miracles don't exist, do your work")
        if len(list)<1:
            sg.popup("Your list look pretty empty go find shit to do")        
    if event == 'Clear all tasks':
            window['output'].update('')        
            list.clear()
    if event in (sg.WIN_CLOSED, 'Exit'):
        break    
       
window.close()