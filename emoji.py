import os

from exceptions import EmojiNotFound, InvalidEmojisDir


def emoji_input_to_codepoint(emoji_input: str) -> str:
    '''Process the user's emoji input into unicode codepoint'''
    codepoints = map(lambda c: hex(ord(c))[2:], emoji_input)
    return '_'.join(codepoints)


def find_emoji_filename(emoji_codepoint: str, emojis_dir: str) -> str:
    """Find emoji filename from the directory

    Args:
        emoji_codepoint (str): Emoji codepoint

    Raises:
        InvalidEmojisDir: Emojis directory is invalid
        EmojiNotFound: Emoji png is not found

    Returns:
        str: Emoji png filename
    """

    if not os.path.isdir(emojis_dir):
        raise InvalidEmojisDir(emojis_dir)

    for filename in os.listdir(emojis_dir):
        if emoji_codepoint in filename:
            return filename
    raise EmojiNotFound(emoji_codepoint)
