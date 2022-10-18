class ConvertionError(Exception):
    def __init__(self, cmd_str: str):
        message = 'Error while converting image to ico.\n' + \
            'Make sure ImageMagick is installed by running ' + \
            '`magick --version` on your command line.\n\n' + \
            'executed_command: {}'.format(cmd_str)
        super().__init__(message)
