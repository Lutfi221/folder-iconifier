import os
from random import randint
import re

import requests

from set_icon import set_icon

EMOJIS_DIR = 'D:\\resources\\icons\\noto emoji\\noto-png\\'


def process_path_input(path: str) -> str:
    '''Process the path string from user input'''
    output = path
    if '"' in path:
        output = path[1:-1]
    return output


def emoji_input_to_codepoint(emoji_input: str) -> str:
    '''Process the user's emoji input into unicode codepoint'''
    codepoints = map(lambda c: hex(ord(c))[2:], emoji_input)
    return '_'.join(codepoints)


def find_emoji_filename(emoji_codepoint: str) -> str:
    """Find emoji filename from the directory

    Args:
        emoji_codepoint (str): Emoji codepoint

    Raises:
        Exception: Emoji png is not found

    Returns:
        str: Emoji png filename
    """
    for filename in os.listdir(EMOJIS_DIR):
        if filename.startswith(emoji_codepoint):
            return filename
    raise Exception(
        'Cannot find emoji png for codepoint \'{}\''.format(emoji_codepoint))


def png_to_ico(png_path: str, ico_path: str):
    """Convert png to ico

    Args:
        png_path (str): Path to png file
        ico_path (str): Path to ico file
    """
    os.system('magick convert "{}" -define icon:auto-resize=256,128,96,64,48,32,24,16 "{}"'.format(
        png_path, ico_path))


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

    png_to_ico(temp_filepath, destination_ico_path)
    os.remove(temp_filepath)


def main():
    print('\nFolder path to be given emoji icon (drag & drop supported)')
    folder_path = input(' > ')
    folder_path = process_path_input(folder_path)

    print('\nEmoji character or an icon URL (.png .ico)')

    user_input = input(' > ')

    if (is_url(user_input)):
        ico_path = os.path.join(folder_path, 'iconifier download.ico')
        download_to_ico(user_input, ico_path)
    else:
        emoji_codepoint = emoji_input_to_codepoint()
        emoji_png_filename = find_emoji_filename(emoji_codepoint)

        print('codepoint: {}'.format(emoji_codepoint))
        print('filename: {}'.format(emoji_png_filename))

        emoji_png_path = os.path.join(EMOJIS_DIR, emoji_png_filename)
        ico_path = os.path.join(
            folder_path, 'iconifier {}.ico'.format(emoji_png_filename[:-4]))

        png_to_ico(emoji_png_path, ico_path)

    hide_file(ico_path)

    delete_old_iconifier_icons(folder_path)
    set_icon(folder_path, ico_path)
    # Without this command, windows won't refresh the icon immediately
    os.system('attrib +r "{}"'.format(folder_path))


if __name__ == '__main__':
    while True:
        main()
