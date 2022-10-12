import os
from configurations import load_config

from emoji import emoji_input_to_codepoint, find_emoji_filename

from set_icon import set_icon
from utils import (convert_to_ico, delete_old_iconifier_icons,
                   download_to_ico, hide_file, is_url, process_path_input)

CONFIG_PATH = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), 'config.json')


def main():
    config = load_config(CONFIG_PATH)

    print('\nFolder path to be given emoji icon (drag & drop supported)')
    folder_path = input(' > ')
    folder_path = process_path_input(folder_path)

    print('\nEmoji character or an icon URL (.png .ico)')

    user_input = input(' > ')

    if (is_url(user_input)):
        ico_path = os.path.join(folder_path, 'iconifier download.ico')
        delete_old_iconifier_icons(folder_path)
        download_to_ico(user_input, ico_path)
    else:
        emoji_codepoint = emoji_input_to_codepoint(user_input)
        emoji_png_filename = find_emoji_filename(
            emoji_codepoint, config['emojis_dir'])

        print('codepoint: {}'.format(emoji_codepoint))
        print('filename: {}'.format(emoji_png_filename))

        emoji_png_path = os.path.join(config['emojis_dir'], emoji_png_filename)
        ico_path = os.path.join(
            folder_path, 'iconifier {}.ico'.format(emoji_png_filename[:-4]))

        delete_old_iconifier_icons(folder_path)
        convert_to_ico(emoji_png_path, ico_path)

    hide_file(ico_path)
    set_icon(folder_path, ico_path)

    # This command might help update the icon to display on explorer
    os.system('attrib +r "{}"'.format(folder_path))


if __name__ == '__main__':
    while True:
        main()
