from utils.input_to_list import input_to_list
import re 

mandatory_fields = {
    'byr': {
        'description': 'Birth Year',
        'mandatory': True,
        'validate': lambda x: 1920 <= int(x) <= 2002
    },
    'iyr': {
        'description': 'Issuance Year',
        'mandatory': True,
        'validate': lambda x: 2010 <= int(x) <= 2020
    },
    'eyr': {
        'description': 'Expiration Year',
        'mandatory': True,
        'validate': lambda x: 2020 <= int(x) <= 2030
    },
    'hgt': {
        'description': 'Height',
        'mandatory': True,
        'validate': lambda x: 150 <= int(x[:-2]) <= 193 if x[-2:] == 'cm' else 59 <= int(x[:-2]) <= 76
    },
    'hcl': {
        'description': 'Hair Color',
        'mandatory': True,
        'validate': lambda x: bool(re.match('^#(\w|\d){6}$', x))
    },
    'ecl': {
        'description': 'Eye Color',
        'mandatory': True,
        'validate': lambda x: x in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    },
    'pid': {
        'description': 'Passport ID',
        'mandatory': True,
        'validate': lambda x: bool(re.match('^\d{9}$', x))
    },
    'cid': {
        'description': 'Country ID',
        'mandatory': False,
        'validate': lambda x: True
    }
}

def parse_input(path):
    with open(path, "r") as f:
        data = [parse_passport(y.split(":") for y in x.replace("\n", " ").split(" ")) for x in f.read().split("\n\n")]
        f.close()
    return data

def parse_passport(data):
    passport = {}
    for [key, value] in data:
        passport[key] = value        
    return passport

def validate_passport(passport):
    for name, props in mandatory_fields.items(): 
        try:
            if props['mandatory']:
                if not props['validate'](passport[name]):
                    print(f"Passport invalid: failed validation check for {name}.")
                    return False
        except:
            print(f"Passport invalid: missing field {name}.")
            return False
    print(f"Passport valid!")
    return True

    
def validate_all(path):
    input = parse_input(path)
    return [validate_passport(passport) for passport in input].count(True)
