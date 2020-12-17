class Op:
    def __init__(self, key, name, params, fn, write=False):
        self.key = key
        self.name = name
        self.params = params
        self.fn = fn
        self.write = write

    def __call__(self, com, *args):
        com.debug_msg(f"{self.name} called to process {args}")
        return self.fn(com, *args)
