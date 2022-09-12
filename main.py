import os
import re
from itertools import filterfalse

EMOJIS_DIR = 'D:\\resources\\icons\\noto emoji\\noto-png\\'


def process_path_input(path: str) -> str:
    '''Process the path string from user input'''
    output = path
    if '"' in path:
        output = path[1:-1]
    return output


def emoji_input_to_codepoint(emoji_input: str) -> str:
    '''Process the user's emoji input into unicode codepoint'''
    return hex(ord(emoji_input))[2:]


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
        if emoji_codepoint in filename:
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


def delete_old_emojifier_icons(folder_path: str):
    """Delete old emojifier icons within the directory

    Args:
        folder_path (str): Path to directory
    """
    p = re.compile('emojifier.+\.ico')
    filenames = os.listdir(folder_path)
    for filename in filenames:
        if p.match(filename):
            os.remove(os.path.join(folder_path, filename))


def set_folder_icon(folder_path: str, ico_path: str):
    """Modify or create the 'desktop.ini' of the folder

    Args:
        folder_path (str): Path to folder
        ico_path (str): Path to ico file
    """
    desktop_ini_path = os.path.join(folder_path, 'desktop.ini')

    if os.path.isfile(desktop_ini_path):
        icon_entry_pattern = re.compile('Icon.+=.+')

        def is_icon_entry(line: str) -> bool:
            return icon_entry_pattern.match(line)

        with open(desktop_ini_path, 'r+') as f:
            lines = f.readlines()

            # Removes lines that are icon entries,
            # such as 'IconIndex', or 'IconFile'
            filtered_lines = list(filterfalse(is_icon_entry, lines))

            shell_info_index = -1

            for i, line in enumerate(filtered_lines):
                if '[.ShellClassInfo]' in line:
                    shell_info_index = i
                    break
            if shell_info_index == -1:
                filtered_lines.insert(0, '[.ShellClassInfo]\n')
                shell_info_index = 0

            # Inserts 'IconResource' entry under '[.ShellClassInfo]'
            filtered_lines.insert(shell_info_index + 1,
                                  'IconResource="{}",0\n'.format(ico_path))

            f.seek(0)
            f.truncate(0)
            f.writelines(filtered_lines)
        return

    content = '[.ShellClassInfo]' + \
        '\nIconResource="{}",0\n'.format(ico_path)
    with open(desktop_ini_path, 'w') as f:
        f.write(content)
    hide_file(desktop_ini_path)


def main():
    print('\nFolder path to be given emoji icon (drag & drop supported)')
    folder_path = input(' > ')
    folder_path = process_path_input(folder_path)

    print('\nEmoji character')

    emoji_codepoint = emoji_input_to_codepoint(input(' > '))
    emoji_png_filename = find_emoji_filename(emoji_codepoint)

    print('codepoint: {}'.format(emoji_codepoint))
    print('filename: {}'.format(emoji_png_filename))

    emoji_png_path = os.path.join(EMOJIS_DIR, emoji_png_filename)
    emoji_ico_path = os.path.join(
        folder_path, 'emojifier {}.ico'.format(emoji_png_filename[:-4]))

    delete_old_emojifier_icons(folder_path)
    png_to_ico(emoji_png_path, emoji_ico_path)
    hide_file(emoji_ico_path)

    set_folder_icon(folder_path, emoji_ico_path)
    # Without this command, windows won't refresh the icon immediately
    os.system('attrib +r "{}"'.format(folder_path))


if __name__ == '__main__':
    while True:
        main()
