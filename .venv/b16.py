# import FreeSimpleGUI as sg
#
# label1 = sg.Text("Select files to compress: ")
# input1 = sg.Input()
# choose_button1 = sg.FilesBrowse("Choose")
#
# label2 = sg.Text("Select destination folder: ")
# input2 = sg.Input()
# choose_button2 = sg.FolderBrowse("Choose")
#
# compress_button = sg.Button("Compress")
# window = sg.Window("File Compressor", layout=[[label1,input1,choose_button1],
#                                               [label2,input2,choose_button2],[compress_button]])
#
# window.read()
# window.close()

# import FreeSimpleGUI as ff
#
# nadpis1 = ff.Text('Enter feet: ')
# nadpis2 = ff.Text("Enter inches: ")
#
# input1 = ff.Input()
# input2 = ff.Input()
#
# baton = ff.Button("Convert")
#
# window = ff.Window("Convertor", layout=[[nadpis1,input1], [nadpis2,input2], [baton]])
#
# window.read()
# window.close()

import FreeSimpleGUI as sg

label = sg.Text("What are dolphins?")
option1 = sg.Radio("Amphibians", group_id="question1")
option2 = sg.Radio("Fish", group_id="question1")
option3 = sg.Radio("Mammals", group_id="question1")
option4 = sg.Radio("Birds", group_id="question1")

window = sg.Window("File Compressor",
                   layout=[[label],
                           [option1],
                            [option2],
                            [option3],
                            [option4],
                           ])

window.read()
window.close()