# Audio input / output operations (mostly output)

import soundfile as sf
import pygame

pygame.mixer.pre_init(channels=1, allowedchanges=pygame.AUDIO_ALLOW_CHANNELS_CHANGE)
pygame.init()

def play_audio(path_to_audio_file: str):
    """
    Uses pygame to play audio in the app.

    Args:
        path_to_audio_file (str): Path to audio file to be loaded.
    """
    pygame.mixer.init()
    pygame.mixer.music.load(path_to_audio_file)
    pygame.mixer.music.play()

def pause_audio():
    pygame.mixer.music.pause()

def stop_audio_and_close_window(window_to_close):
    # cannot believe i'm actually making this function
    try:
        pygame.mixer.music.pause()
    except pygame.error:
        pass
    finally:
        window_to_close.destroy()

if __name__ == '__main__':
    pass