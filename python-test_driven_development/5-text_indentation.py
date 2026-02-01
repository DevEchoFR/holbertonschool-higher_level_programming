#!/usr/bin/python3
"""
Module that contains text_indentation function.

This module provides a function that prints text with proper indentation
after specific punctuation marks.
"""


def text_indentation(text):
    """Print text with 2 new lines after each '.', '?', and ':'.

    This function prints the provided text, adding two new lines after
    each occurrence of '.', '?', or ':'. Spaces at the beginning and end
    of each printed line are removed.

    Args:
        text (str): The text to be printed with indentation.

    Raises:
        TypeError: If text is not a string.

    Example:
        >>> text_indentation("Hello          .           How are you?")
        Hello.
        <BLANKLINE>
        How are you?
        <BLANKLINE>
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    res = ''
    i = 0
    while i < len(text):
        if text[i] in '?.:' and i < len(text):
            while len(res) >= 1 and res[-1] == ' ':
                res = res[:-1]
            res += text[i] + '\n\n'
            while i + 1 < len(text) and text[i + 1] == ' ':
                i += 1
        else:
            res += text[i]
        i += 1
    print(res, end='')
