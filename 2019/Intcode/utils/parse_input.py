def parse_input(path):
    with open(path, 'r') as f:
        op_code = f.read().split(",")
        f.close()
    return op_code
