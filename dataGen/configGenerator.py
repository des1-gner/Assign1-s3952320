import json
import random

def generate_maze(data_structure, row_num, col_num):

    maze_data = {

        "dataStructure": data_structure,
        "rowNum": row_num,
        "colNum": col_num,
        "entrances": [[0, -1], [-1, 1]],
        "exits": [[3, 5], [5, 4]],
        "generator": "recur",
        "visualise": True

    }

    filename = f"maze_{data_structure}.json"

    with open(filename, "w") as file:

        json.dump(maze_data, file, indent=4)
    
    print(f"Generated {filename} successfully.")

# Get user input for rowNum and colNum

row_num = int(input("Enter the number of rows: "))
col_num = int(input("Enter the number of columns: "))

# Generate maze files with different dataStructure values

generate_maze("adjlist", row_num, col_num)
generate_maze("adjmat", row_num, col_num)
generate_maze("array", row_num, col_num)
