# Audio Operations including reading and writing audio files

import soundfile as sf
import gui.alerts
import ggamir

def readAudioFile(audio_file_path:str):
    try:
        if audio_file_path:
            [IR, fs] = sf.read(audio_file_path)
    except Exception as e:
        gui.alerts.errorWindow(
            ggamir.root, 
            error_message=f"\nError: {e}\n"
            )
        return
    # else:
    #     if audio_file_path:
            