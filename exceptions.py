class ConvertionError(Exception):
    def __init__(self, cmd_str: str):
        message = ('Error while converting image to ico.\n'
                   'Make sure ImageMagick is installed by running '
                   '`magick --version` on your command line.\n\n'
                   'executed_command: {}').format(cmd_str)
        super().__init__(message)


class EmojiNotFound(Exception):
    def __init__(self, emoji_codepoint: str):
        message = ('Cannot find emoji PNG with codepoint'
                   " `{}`.\n"
                   'Your emoji folder might not have it, '
                   'or it is an invalid emoji.').format(emoji_codepoint)
        super().__init__(message)


class InvalidEmojisDir(Exception):
    def __init__(self, emojis_dir: str):
        if emojis_dir == "":
            message = ('Unconfigured `emojis_dir`.\n'
                       'The `emojis_dir` field in config.json is empty. '
                       'You need to fill it with the path to '
                       'the directory filled with emoji PNG files.\n'
                       "Read the ReadMe in the `Google's Noto Emoji` section.")
        else:
            message = ('Invalid `emojis_dir`.\n'
                       'Make sure the `emojis_dir` in config.json '
                       'points to a valid path.')
        super().__init__(message)


class FolderNotFound(Exception):
    def __init__(self, path: str):
        message = ('Folder not found.\n\n'
                   'path: {}').format(path)
        super().__init__(message)
