# Folder Iconifier 🎨

Folder Iconifier helps you customize your folder icons with just a couple of drags and presses. You can use emojis, pngs, and icons from the internet for your folders.

![Before and after of the folders' icons](docs/assets/images/before-after.png)

- [Folder Iconifier 🎨](#folder-iconifier-)
- [Usage](#usage)
- [Google's Noto Emoji](#googles-noto-emoji)
  - [Downloading](#downloading)
  - [Using It](#using-it)
- [Requirements](#requirements)

# Usage

1. Open `main.py`
2. Input the folder path. You can paste it, or drag and drop the folder.

```console
Folder path to be given emoji icon (drag & drop supported)
 >
```

3. Input the icon URL that you want.

```console
Emoji character or an icon URL (.png .ico)
 >
```

These are some examples of valid inputs:

- `https://github.com/googlefonts/noto-emoji/raw/main/png/512/emoji_u1f60a.png`
- `https://upload.wikimedia.org/wikipedia/commons/thumb/0/0c/Blender_logo_no_text.svg/939px-Blender_logo_no_text.svg.png`

# Google's Noto Emoji

## Downloading

In order to use Google's Noto Emoji, you need to have a folder containing all the emoji PNGs with their codepoints as names. It can be whatever size (512, 128, 72, etc.) you want.

A good source of the complete emoji PNGs is from [Google's Noto Emoji GitHub](https://github.com/googlefonts/noto-emoji).

1. Download the directory you want by using the [download-directory](https://download-directory.github.io/) tool.
2. Input `https://github.com/googlefonts/noto-emoji/tree/main/png/512` into the text field.
3. Export the downloaded file into a folder.

Then go to `config.json` and fill the `emojis_dir` with the path to the emojis folder. Don't forget to escape the backslashes.

## Using It

When you're prompted for an emoji character, simply press `WINDOWS + .` to open the emoji popup, and input one emoji. Or you can copy-paste it from the internet.

Then press `Enter`.

# Requirements

- [ImageMagick](https://imagemagick.org/script/download.php)
- Python Modules
  - [requests](https://pypi.org/project/requests/) — `python -m pip install requests`
