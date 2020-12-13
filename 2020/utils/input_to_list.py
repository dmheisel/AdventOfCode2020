def input_to_list(path, num_convert = True):
    with open(path, "r") as f:
        data = f.read()
        f.close()
    ret = [int(num) for num in data.split("\n")] if num_convert else data.split("\n")
    return ret
    