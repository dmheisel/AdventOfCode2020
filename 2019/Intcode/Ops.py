from Op.Op import *
from Constants import *

ops = {
    ADD: Op(ADD, 'Add', 3,
            lambda self, x, y, z: self.mod(z, x + y),
            True),
    MLT: Op(MLT, 'Mult', 3,
            lambda self, x, y, z: self.mod(z, x * y),
            True),
    INP: Op(INP, 'Input', 1,
            lambda self, x: self.mod(x, self.request_input()),
            True),
    OUT: Op(OUT, 'Output', 1,
            lambda self, x: self.O.append(x),
            ),
    JIT: Op(JIT, 'Jump-if-True', 2,
            lambda self, x, y: self.update_pointer(
                y, True) if x != 0 else True
            ),
    JIF: Op(JIF, 'Jump-if-False', 2,
            lambda self, x, y: self.update_pointer(
                y, True) if x == 0 else True
            ),
    LTN: Op(LTN, "Less Than", 3,
            lambda self, x, y, z: self.mod(z, 1 if x < y else 0),
            True),
    EQL: Op(EQL, "Equal To", 3,
            lambda self, x, y, z: self.mod(z, 1 if x == y else 0),
            True),
    RBO: Op(RBO, "Relative Base Offset", 1,
            lambda self, x: self.update_base(x),
            False),
    STP: Op(STP, 'Stop', 0,
            lambda self: self.halt()),
}
