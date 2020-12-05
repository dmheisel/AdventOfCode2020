from utils.input_to_list import input_to_list


def parse_row(code):
    row_range = list(range(128))
    for char in code:
        if (char == "F"):
            row_range = row_range[:int(len(row_range) / 2)]
        else:
            row_range = row_range[int(len(row_range) / 2):]
    return row_range[0]


def parse_column(code):
    column_range = list(range(8))
    for char in code:
        if(char == 'L'):
            column_range = column_range[:int(len(column_range)/2)]
        else:
            column_range = column_range[int(len(column_range)/2):]
    return column_range[0]


def get_seat_ID(seatcode):
    return parse_row(seatcode[:-3]) * 8 + parse_column(seatcode[0-3:])


def get_all_seats(data):
    seats_by_id = [get_seat_ID(seat) for seat in data]
    seats_by_id.sort()
    return seats_by_id


def get_missing_seat(seats):
    possible_seats = list(range(seats[0], seats[-1]))
    return [seat for seat in possible_seats if seat not in seats]
