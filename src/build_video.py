import json
from CONST import *
from pathlib import Path
from moviepy.editor import *


def read_config(path: str):
    """
    Return the config from json file to config the process
    :param path: json file
    :return: dict
    """
    path_file_config = Path(path).absolute()
    config = None
    with open(path_file_config) as file_config:
        file_config = file_config.read()
        config = json.loads(file_config)

    return config


def sound_background(sound_path, duration, volume=0.5):
    """
    set sound loop for the time of all video
    """
    sound_bg = AudioFileClip(sound_path)
    sound_bg = afx.audio_loop(sound_bg, duration=duration)
    return sound_bg.volumex(volume)


def process_image(composition_imagen, duration, size=0):
    imagen = ImageClip(composition_imagen[PATH], transparent=True, duration=duration)
    fadein = composition_imagen.get(FADE_IN) if composition_imagen.get("FADE_IN") else 0
    fadeout = composition_imagen.get(FADE_OUT) if composition_imagen.get(FADE_OUT) else 0
    result_video = CompositeVideoClip([imagen], size=imagen.size).fadeout(composition_imagen[FADE_OUT]).fadein(
        composition_imagen[FADE_IN])

    return result_video


def process_sound(compostion_sound, duration):
    pass


def process_video(compostion_video, duration):
    pass


def process_start(composition: dict, duration, size=0):
    imagens = []
    duration_for_picture = duration / len(composition[START][IMAGEN])

    for imagen in composition[START][IMAGEN]:
        imagens.append(process_image(imagen, duration_for_picture, size))

    imagen_clip = concatenate_videoclips(imagens, method="compose")
    #return imagen_clip
    imagen_clip.write_videofile(f"test_final.mp4", fps=4, codec="libx264")


def main():
    config = read_config("video1.json")
    ## print(config)
    process_start(config, duration=20)


if __name__ == "__main__":
    main()
