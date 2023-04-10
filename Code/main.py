import os, sys
from datetime import datetime
import subprocess
import zipfile

import gui, tools

VERSION = "1.03"
FILEBROWSER_PATH = os.path.join(os.getenv('WINDIR'), 'explorer.exe')
JOURNEY_FOLDER = os.path.expandvars(r'%APPDATA%\.minecraft\journeymap\data\sp')
WORLD_FOLDER = os.path.expandvars(r'%APPDATA%\.minecraft\saves')

tools.settings = tools.handle_settings()
window = gui.make_window(tools.settings["language"])

def make_zipfile(output_filename, source_dir):
    try:
        relroot = os.path.abspath(os.path.join(source_dir, os.pardir))
        with zipfile.ZipFile(output_filename, "w", zipfile.ZIP_DEFLATED) as zip:
            for root, dirs, files in os.walk(source_dir):
                # add directory (needed for empty dirs)
                zip.write(root, os.path.relpath(root, relroot))
                for file in files:
                    filename = os.path.join(root, file)
                    if os.path.isfile(filename): # regular files only
                        arcname = os.path.join(os.path.relpath(root, relroot), file)
                        zip.write(filename, arcname)
    except Exception as e:
        gui.sg.popup(e) 


def explore(path):
    try:
        path = os.path.normpath(path)
        if os.path.isdir(path):
            subprocess.run([FILEBROWSER_PATH, path])
        elif os.path.isfile(path):
            subprocess.run([FILEBROWSER_PATH, '/select,', os.path.normpath(path)])
    except Exception as e:
        gui.sg.popup(e) 


def main():
    firststart = True
    global window
    while True: 
        event, values = window.read(timeout=100)  
        if event == gui.sg.WINDOW_CLOSE_ATTEMPTED_EVENT or event == 'Exit':
            tools.save_settings(values)
            break
        elif event == '-START-':
            make_zipfile(WORLD_FOLDER + "/" + "World_" + str(datetime.now().strftime("%Y_%m_%d_%H%M%S"".zip")), tools.settings["world_folder"])
            if values['-JMAP-'] == True:
                make_zipfile(JOURNEY_FOLDER + "/" + "Journey_" + str(datetime.now().strftime("%Y_%m_%d_%H%M%S"".zip")), tools.settings['journey_folder'])
        elif event == '-WFOLDER-':
            folder = gui.sg.popup_get_folder('Choose your World', initial_folder= WORLD_FOLDER)
            if folder != None:  
                tools.settings.update({'world_folder':folder})
                window['-sWFOLDER-'].update(str(tools.settings["world_folder"]))
        elif event == '-JFOLDER-':
            folder = gui.sg.popup_get_folder('Choose your Map', initial_folder= JOURNEY_FOLDER)
            if folder != None:   
                tools.settings.update({'journey_folder':folder}) 
                window['-sJFOLDER-'].update(str(tools.settings['journey_folder']))
        elif event == '-WSHOW-': 
            explore(WORLD_FOLDER)
        elif event == '-JSHOW-':
            explore(JOURNEY_FOLDER)
        elif event == 'en':
            tools.settings.update({'language':'en'}) 
            gui.sg.popup("Setting take effect after restart the Application")
        elif event == 'de':
            tools.settings.update({'language':'de'})      
            gui.sg.popup(" Einstellung wird erst nach einem Neustart übernommen")
        elif event == 'Help' or event == 'Hilfe':
            gui.show_help(tools.settings["language"])
        elif event == 'About':
            gui.sg.popup(f'Version: {VERSION} \n - works only with the JAVA version of Minecraft! -')
        if values['-JMAP-'] == True: 
            window['-JFOLDER-'].update(disabled=False)  
            window["-JSHOW-"].update(disabled=False) 
            window['-sJFOLDER-'].update(disabled=False) 
        else: 
            window['-JFOLDER-'].update(disabled=True)
            window['-JSHOW-'].update(disabled=True) 
            window['-sJFOLDER-'].update(disabled=True) 

        if firststart == True:       
            firststart = False
            if tools.update_window(window) == "Error":
                gui.sg.popup("Error reading settings.txt")
    sys.exit()

if __name__ == '__main__':
    main()