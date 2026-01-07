# Audio Operations including reading and writing audio files

import shared.globals

import gui.alerts
import gui.dyncontent

import func.fileio
import func.app

import soundfile as sf

def pick_ir(ir_label):
    return_value = 2 # shortened file path
    tooltip_return_value = 0 # full file path
    
    try:
        # i realize i don't actually _have_ to do it like this, but this used to be a lambda function and it works just fine as it is and blah blah blah i'm sure it's okay
        gui.dyncontent.manipulate_tk_with_func(function=func.fileio.select_audio_file, tkObject=ir_label, tkAttribute='text', return_value=return_value, tooltip_return_value=tooltip_return_value)
        shared.globals.graph_buttons_state = 'normal'
        func.app.refresh_tkobject(shared.globals.file_data_button, shared.globals.graph_buttons_state)
        func.app.refresh_tkobject(shared.globals.td_vis_button, shared.globals.graph_buttons_state)
        func.app.refresh_tkobject(shared.globals.fd_vis_button, shared.globals.graph_buttons_state)

        shared.globals.IR, shared.globals.fs = read_audio_file(shared.globals.audio_file_path)
        
    except Exception as e:
        return -1
    
    return

def read_audio_file(audio_file_path:str):
    try:
        if audio_file_path:
            [IR, fs] = sf.read(audio_file_path)
            return IR, fs
    except Exception as e:
        gui.alerts.error_window(
            shared.globals.root, 
            error_message=f"\nError: {e}\n"
            )
        return
    return