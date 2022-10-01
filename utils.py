import os
from random import randint
import re

import requests


def process_path_input(path: str) -> str:
    '''Process the path string from user input'''
    output = path
    if '"' in path:
        output = path[1:-1]
    return output


def convert_to_ico(png_path: str, ico_path: str):
    """Convert file to ico

    Args:
        source_path (str): Path to image file
        ico_path (str): Path to ico file
    """
    os.system('magick convert "{}" -define '.format(png_path) +
              'icon:auto-resize=' +
              '256,128,96,64,48,32,24,16 "{}"'.format(ico_path))


def hide_file(file_path: str):
    """Hides a file and make it a system file

    Args:
        file_path (str): Path to file
    """
    os.system('attrib +s +h "{}"'.format(file_path))


def delete_old_iconifier_icons(folder_path: str):
    """Delete old iconifier icons within the directory

    Args:
        folder_path (str): Path to directory
    """
    p = re.compile(r'(iconifier|emojifier).+\.ico')
    filenames = os.listdir(folder_path)
    for filename in filenames:
        if p.match(filename):
            os.remove(os.path.join(folder_path, filename))


def is_url(s: str) -> bool:
    """Checks if a string is a valid url"""
    # https://regexr.com/39nr7
    p = re.compile(
        r'[(http(s)?):\/\/(www\.)?a-zA-Z0-9@:%._\+~#=]{2,256}' +
        r'\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)')
    return bool(p.match(s))


def download_to_ico(url: str, destination_ico_path: str):
    r = requests.get(url, allow_redirects=True)
    destination_dirpath = os.path.split(destination_ico_path)[0]
    temp_filepath = os.path.join(
        destination_dirpath, 'temp iconifier {}'.format(randint(0, 9999)))

    open(temp_filepath, 'wb').write(r.content)

    convert_to_ico(temp_filepath, destination_ico_path)
    os.remove(temp_filepath)
