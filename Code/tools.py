import json
import gui

# VERSION 1.03
settings = {}

def read(filename):
    try:
        return json.load(open(filename))
    except:
        return None 


def write(filename,dict):
    try:
        json.dump(dict, open(filename,'w'),indent=2)  # ident=2 -> New line for each variable
        return None
    except Exception as e:
        return e 


def handle_settings():
    settings = read(".\settings.ini")           # Read settings from file
    if settings == None:                        # File not found
        settings = {                            # Default settings to make new file
                  "language": "en",
                  "use_journey": False, 
                  "world_folder": "Please select world", 
                  "journey_folder": "Please select journey map", 
                  }  
        write(".\settings.ini", settings)         # Make new file
        gui.sg.popup("No settings file found!\nA new one was created with default values.\nPlease change/add the settings and save them",keep_on_top=True)
    return settings


def update_window(window): 
    try:  
        window['-sWFOLDER-'].update(settings["world_folder"])
        window['-sJFOLDER-'].update(settings["journey_folder"])
        window['-JMAP-'].update(settings["use_journey"])
    except:
        return "Error"
 

def save_settings(values):
    settings.update({"use_journey":values['-JMAP-']})
    write(".\settings.ini", settings)         # Make new file

