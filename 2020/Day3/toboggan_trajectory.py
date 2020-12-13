from utils.input_to_list import input_to_list

def move_on_x(amt, start, length):
    new_position = start + amt
    return new_position if length - 1 >= new_position else new_position - length

def move_on_y(amt, start, length):
    new_position = start + amt
    return new_position if length - 1 >= new_position else length - 1

def count_trees(map, x_slope, y_slope):
    x_pos = 0
    y_pos = 0
    tree_count = 0
    while(y_pos < len(map)-1) :
        if (map[y_pos][x_pos] == "#"):
            tree_count += 1
        x_pos = move_on_x(x_slope, x_pos, len(map[y_pos]))
        y_pos = move_on_y(y_slope, y_pos, len(map))
    return tree_count


def calculate_trajectory(path, slopes):

    print('parsing map...')
    map = input_to_list(path, False)

    product = 1
    for (x, y) in slopes:
        print(f"counting trees on map with trajectory {x} right and {y} down")
        tree_count = count_trees(map, x, y)
        print(f"{tree_count} trees found!")
        product *= tree_count
        print(f"Product updated to {product}")
    
    print(f"Final product of all trees is: {product}")
    return product
