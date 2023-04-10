from ctypes import alignment
from re import MULTILINE
import PySimpleGUI as sg    # testet with PySimpleGUI-4.55.1 and PySimpleGUI-4.57.0

" version: 1.11"

def make_window():
  sg.theme("DarkBlue14")  #"DarkBlue13" "DarkGrey"
  menu_def = [['&Application', ['E&xit']],
                ['&Help', ['&Help (pdf)', '&About']] ]
  
  common_layout = [[sg.Checkbox('Automatic Reading (Trigger)', k='AUTOMATIC')],
                  [sg.Text('Chart Name:',size=(10,1)), sg.Input('',k='-CHARTNAME-', size=(32,1), tooltip=tt_chartName, enable_events=True)],
                  [sg.Text('Record No.:',size=(10,1)), sg.Input('',k='-RECNO-', size=(6,1), tooltip=tt_chartNo, justification='right', enable_events=True)]]

  plc_layout = [[sg.Text("")],[sg.Text("IP-Adress:",size=(10,1)),sg.Input('', size=(14,1),k="IP",tooltip=tt_ip,justification='center',disabled_readonly_background_color='grey', focus=False),    #[[sg.Text('PLC Settings (SLMP or MC Protocol)')],
                sg.Text(""), sg.Text("Start Device:"), sg.Input('',k='STARTDEV', size=(6,1), tooltip=tt_stDev, justification='right',disabled_readonly_background_color='grey'),
                sg.Text(""),sg.Text("Number of Devices:"), sg.Input('',k='DEVSIZE', size=(5,1), tooltip=tt_noDev, justification='right',disabled_readonly_background_color='grey')],
                [sg.Text("Port:",size=(10,1)), sg.Input('',k='PORT', size=(5,1), tooltip=tt_port, justification='right',disabled_readonly_background_color='grey'),
                sg.Text("",size=(8,1)),sg.Text("Trigger Device:"), sg.Input('',k='TRIGDEV', size=(6,1), tooltip=tt_triDev, justification='right',disabled_readonly_background_color='grey'),
                sg.Text("Done Devices:"), sg.Input('',k='DONEDEV', size=(6,1), tooltip=tt_donDev, justification='right',disabled_readonly_background_color='grey')]]

  file_layout = [[sg.Text("")],[sg.Button("Template", k='-FILE-',size=(12,1)), sg.Input(k='-sFILE-', size=(64,1), justification='right', disabled_readonly_background_color='grey')],  #[[sg.Text('File Settings')],
                [sg.Button("Output Folder", k='-FOLDER-',size=(12,1)), sg.Input(k='-sFOLDER-', size=(64,1), justification='right',disabled_readonly_background_color='grey')]]

  layout =  [[sg.Menu(menu_def, key='-MENU-')]]

  layout += [[sg.TabGroup([[  sg.Tab('Common Settings', common_layout),
                              sg.Tab('PLC Settings', plc_layout),
                              sg.Tab('File Settings', file_layout),]], key='-TAB GROUP-')]]
              
  layout +=  [[sg.Text('Commands')],
              [sg.Button('Connect', k='-START-',size=(10,1)), sg.Button('Disconnect', k='-STOP-',size=(10,1)),sg.Button('Manu Read', k='-MANUREAD-', size=(10,1)),sg.Button('Save Settings', k='-SET-',size=(10,1)),
              sg.Button('Open Folder', k='-OPENFOLDER-', size=(10,1)),sg.Button('Clear Log', k='-CLEAR-', size=(10,1))],
              [[sg.Text("Log")], [sg.Multiline(size=(70,15),font='Courier 10',disabled = True, focus=True, key='LOG' +sg.WRITE_ONLY_KEY, background_color='lightgrey')]]]  #+sg.WRITE_ONLY_KEY = Inhalt erscheint nicht in "values" beib readen
  
  return sg.Window('MC Sheet', finalize=True, grab_anywhere=0).Layout(layout)  #no_titlebar=True             


# Tool tip text
tt_ip = " IP-Adress of PLC "
tt_port = " Select Port for SLMP communication as in PLC parameter settings "
tt_stDev = " First device to read data from (D or R)"
tt_noDev = " Number of data register to read from (1..9800) "
tt_triDev = " \"Trigger device\" PLC -> MC-Sheet (M0..M7679)"
tt_donDev = " \"Done device\" MC-Sheet -> PLC (M0..M7679)"
tt_chartName = " Name to display on chart"
tt_chartNo = " Number to display on chart. Automatically increments after each data save "