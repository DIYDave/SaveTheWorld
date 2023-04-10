from ctypes import alignment
import PySimpleGUI as sg

# VERSION 1.03

def make_window(language="en"):
    sg.theme("DarkBlue14")  #"DarkBlue13" "DarkGrey"

    if language == "en":
        txtWFOLDER = "Select World"; txtWSHOW = "Show"; txtJFOLDER = "Select Map"; txtJMAP = "Journey Map"; txtLANG = 'Sprache'
        txtApp = "Application"; txtHelp = 'Help'; txtSaveSett = 'Save Settings'
    if language == "de":
        txtWFOLDER = "Wähle Welt"; txtWSHOW = "Zeigen"; txtJFOLDER = "Wähle Karte"; txtJMAP = "Journey Karte"; txtLANG = 'Language'
        txtApp = "Anwendung"; txtHelp = 'Hilfe'; txtSaveSett = 'Einst. Speichern'

    menu_def = [[txtApp, [txtLANG,['de','en'],'E&xit']],
                [txtHelp, [txtHelp,'&About']] ]

    col_layout = [[sg.Button('Save the World', k="-START-",size = (16,1))]]

    layout =  [[sg.Menu(menu_def, key='-MENU-')],
              [sg.Button(txtWFOLDER, k='-WFOLDER-',size=(12,1)), sg.Input(k='-sWFOLDER-', size=(52,1), justification='right', disabled_readonly_background_color='grey'),  #[[sg.Text('File Settings')],, 
              sg.Button(txtWSHOW, k="-WSHOW-",size = (8,1))],
              [sg.Checkbox(txtJMAP, default=False, k='-JMAP-')],
              [sg.Button(txtJFOLDER, k='-JFOLDER-',size=(12,1)), sg.Input(k='-sJFOLDER-', size=(52,1), justification='right',disabled_readonly_background_color='grey'),
              sg.Button(txtWSHOW, k="-JSHOW-",size = (8,1))],
              [sg.Column(col_layout, element_justification='center', expand_x=True)]]

    return sg.Window('Save the World', layout,  finalize=True, grab_anywhere=1,enable_close_attempted_event=True)  #no_titlebar=True


def show_help(language="en"):
    if language == 'en':
        help_text= ''' - works only with the Java edition of Minecraft! -

This tool can backup your worlds in Minecraft.

Show the worlds with the "World Folder" button. Select the desired world. 
If you have the "Journey Map" mod installed, you can also save the associated map. (same name as Minecraft World) 
To create the ZIP archives of it, just click the "Save the World" button.

In order to restore the saved world and map, the ZIP archive must be unpacked manually. 
Windows Explorer opens the corresponding folders with the "Show" button. 
Please be careful when restoring. I cannot guarantee lost or overwritten data.
                
Have fun
DaveForesthill '''
                    
    if language == 'de':
        help_text= '''- Funktioniert nur mit der Java edition von Minecraft! -
                    
Dieses Tool kann deine Welten in Minecraft sichern. 
                
Zeige die vorhandenen Welten mit der Taste "World Folder". Wähle die gwünschte Welt. 
Falls du den Mod "Journey Map" installiert hast, kannst du auch die dazugehörige Karte sichern. (gleicher Name wie die Minecraft Welt) 
Um die ZIP-Archive davon zu erstellen, einfach Taste "Save the World" anklicken.
                
Um die gesicherte Welt und Karte wiederherzustellen muss das ZIP-Archiv manuell entpackt werden. 
Mit den Tasten "Show" öffnet der Windows Explorer die netsprechenden Ordner. 
Bitte sei vorsichtig beim wiederherstellen. 
Ich kann keine Garantie für verlorene oder überschriebene Daten übernehmen.
            
Viel Spass
DaveForesthill '''
                    
    sg.popup(help_text)