#!/bin/bash

# python solution file
cat <<EOF > /app/grid_transform.py
import numpy as np

def solve(input_grid):
    """
    Transforms 2x2 grid to 6x6.
    Correct Pattern: Tiling (Repeating the sequence), NOT stretching pixels.
    """
    # Convert to numpy array
    arr = np.array(input_grid)
    
    # 1. Top Section: The original grid repeated 3 times horizontally
    # Input: [8, 6] -> Output: [8, 6, 8, 6, 8, 6]
    top_rows = np.tile(arr, (1, 3))
    
    # 2. Middle Section: The horizontally flipped grid repeated 3 times
    # Input: [8, 6] -> Flipped: [6, 8] -> Output: [6, 8, 6, 8, 6, 8]
    flipped_arr = np.fliplr(arr)
    middle_rows = np.tile(flipped_arr, (1, 3))
    
    # 3. Bottom Section: Same as top
    bottom_rows = top_rows
    
    # Stack them vertically: Top, Middle, Bottom
    final_grid = np.vstack([top_rows, middle_rows, bottom_rows])
    
    return final_grid.tolist()
EOF