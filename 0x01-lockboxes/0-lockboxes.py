#!/usr/bin/python3
def canUnlockAll(boxes):
    num_boxes = len(boxes)
    visited = [False] * num_boxes

    def dfs(box):
        if visited[box]:
            return
        visited[box] = True
        for key in boxes[box]:
            dfs(key)

    dfs(0)
    return all(visited)

# Test cases
boxes1 = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes1))  # Output: True

boxes2 = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes2))  # Output: True

boxes3 = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes3))  # Output: False
