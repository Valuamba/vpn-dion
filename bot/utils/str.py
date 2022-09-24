import os
import re
import uuid

# from emoji import UNICODE_EMOJI_ENGLISH
#
#
# def is_emoji(s):
#     return s in UNICODE_EMOJI_ENGLISH


# def first_letter_to_lower(str: str):
#     if str:
#         new_str = list(str)
#         for idx, s in enumerate(new_str):
#             if not is_emoji(s) and not s.isspace() and s != "\u200d":
#                 new_str[idx] = s.lower()
#                 str = ''.join(new_str)
#     return str


def get_str_uniq():
    return str(uuid.uuid4()).upper()[:8]


def check_int(str):
    if str[0] in ('-', '+'):
        return str[1:].isdigit()
    return str.isdigit()


def absolute_file_paths(directory, re_ext='\d+(?<!.jpg)'):
    for dirpath,_,filenames in os.walk(directory):
        sorted_files = sorted(filenames, key=lambda f: int(re.match(re_ext, f).group(0)), reverse=False)
        for file_name in sorted_files:
            yield os.path.abspath(os.path.join(dirpath, file_name))