"""
This file contains examples of the grid transformation pattern.
The AI agent reads this file to understand how to solve the task.
"""

examples = [
    {
        "input": [
            [8, 6],
            [6, 4]
        ],
        "output": [
            # Top Section: Original Input repeated 3x
            [8, 6, 8, 6, 8, 6],
            [6, 4, 6, 4, 6, 4],
            
            # Middle Section: Flipped (Mirrored) Input repeated 3x
            [6, 8, 6, 8, 6, 8],
            [4, 6, 4, 6, 4, 6],
            
            # Bottom Section: Original Input repeated 3x
            [8, 6, 8, 6, 8, 6],
            [6, 4, 6, 4, 6, 4]
        ],
        "explanation": "The 2x2 grid is tiled 3x3. The middle row of tiles is horizontally mirrored."
    },
    {
        "input": [
            [1, 2],
            [3, 4]
        ],
        "output": [
            # Top
            [1, 2, 1, 2, 1, 2],
            [3, 4, 3, 4, 3, 4],
            
            # Middle (Flipped: 1,2 becomes 2,1)
            [2, 1, 2, 1, 2, 1],
            [4, 3, 4, 3, 4, 3],
            
            # Bottom
            [1, 2, 1, 2, 1, 2],
            [3, 4, 3, 4, 3, 4]
        ]
    }
]