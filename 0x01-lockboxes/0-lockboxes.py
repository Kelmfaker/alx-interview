#!/usr/bin/python3

"""
function determine if all boxs can be opened
"""


from typing import List


def canUnlockAll(boxes: List[List[int]]) -> bool:
    """
    return
    true: if all boxes can be opend
    false: if not
    """
    n = len(boxes)
    opened = set([0])  # Start with the first box
    keys = list(boxes[0])  # Start with keys from the first box

    while keys:
        key = keys.pop()  # Remove and return the last key
        if key < n and key not in opened:
            opened.add(key)
            keys.extend(boxes[key])  # Add new keys found in the box

    return len(opened) == n  # Return True if all boxes are opened, else False
