import PySimpleGUI as sg
import func as fn

label=sg.Text("Type in a todo")
input_box=sg.InputText(tooltip="Enter todo",key="todo")
add_button=sg.Button("Add")
list_box=sg.Listbox(values=fn.gettodo(),key="todo1",enable_events=True,size=[45,10])
edit_button=sg.Button("Edit")

window=sg.Window("My todo App",layout=[[label],[input_box,add_button],
                                       [list_box,edit_button]])

while True:
    event,values=window.read()
    print(event)
    print(values)
    if event=="Add":
        todos=fn.gettodo()#dummy
        new_todo=values["todo"]+'\n'
        todos.append(new_todo)
        fn.writetodo(todos)#dummy
    elif event==sg.WIN_CLOSED:
        break
    elif event=="Edit":
        pass




window.close()