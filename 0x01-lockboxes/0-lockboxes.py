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
