#!/usr/bin/python3
"""
a method that determines if all the boxes can be opened
"""


def canUnlockAll(boxes):
    opened_boxes = set()
    opened_boxes.add(0)

    keys = set(boxes[0])

    while keys:
        key = keys.pop()

        if key < len(boxes) and key not in opened_boxes:
            opened_boxes.add(key)
            keys.update(boxes[key])

    return len(opened_boxes) == len(boxes)
