#!/usr/bin/python3

def canUnlockAll(boxes):
    """
    Determine if all the boxes can be opened.

    Args:
        boxes: A list of lists representing the boxes and their keys.

    Returns:
        True if all boxes can be opened, False otherwise.
    """

    # Initialize a set to keep track of opened boxes
    opened_boxes = {0}

    # Initialize a list to keep track of unopened boxes
    unopened_boxes = [box_index for box_index in range(1, len(boxes))]

    # Start with the first box and explore the keys
    stack = boxes[0]

    # Use DFS to explore the boxes and their keys
    while stack:
        key = stack.pop()

        # Check if the key opens a new box
        if key < len(boxes) and key not in opened_boxes:
            opened_boxes.add(key)
            stack.extend(boxes[key])
            unopened_boxes.remove(key)

            # Check if all boxes have been opened
            if not unopened_boxes:
                return True

    return False

# Example test cases
boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))  # False

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))  # True

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))  # True

