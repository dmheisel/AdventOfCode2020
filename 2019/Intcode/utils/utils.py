def parse_input(path):
    with open(path, 'r') as f:
        op_code = [int(x) for x in f.read().split(",")]
        f.close()
    return op_code
