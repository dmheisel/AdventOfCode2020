class Pass:
    def __init__(self, limits, letter, pword):
        self.lower = int(limits[0])
        self.upper = int(limits[1])
        self.letter = letter
        self.password = pword
    
    def validate_count(self, password = False):
        password = password if password else self.password
        count = password.count(self.letter)
        return count >= self.lower and count <= self.upper

    def validate_position(self, password = False):
        password = password if password else self.password
        return (password[self.lower-1] == self.letter) ^ (password[self.upper-1] == self.letter)