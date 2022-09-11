import os

EMOJIS_DIR = 'D:\\resources\\icons\\noto emoji\\noto-png'


def process_path_input(path: str) -> str:
    '''Process the path string from user input'''
    output = path
    if '"' in path:
        output = path[1:-1]
    return output


def emoji_input_to_codepoint(emoji_input: str) -> str:
    '''Process the user's emoji input into unicode codepoint'''
    return hex(ord(emoji_input))


def main():
    print('Folder path to be given emoji icon (drag & drop supported)')
    folder_path = input(' > ')
    folder_path = process_path_input(folder_path)
    print('\nEmoji character')
    emoji_codepoint = emoji_input_to_codepoint(input(' > '))
    print('codepoint: {}\n'.format(emoji_codepoint))


if __name__ == '__main__':
    main()
