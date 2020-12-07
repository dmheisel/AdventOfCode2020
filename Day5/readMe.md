# Day 5 - Maths!

So, this was a fun challenge.

The idea is that we're given a range of seats that the ticket _could_ be for, and each letter on the boarding pass narrows it down by half -- either in upper or lower half of the range depending on the ticket.

Since we know the last three letters are always going to be for the row, I decided to split the calculations into a separate function for row and column. Some time could be spent here to clean it up and make it more programmatic, since there's a lot of repeat in the parse_row and parse_column functions, but I kept it loose like this on the chance that the second half made the behaviors change somehow.

It was interesting to find out that the math for this actually created incremental tickets (eg. 502, 503, 504...), so finding the missing ticket was as simple as checking a _full_ range between the fist and last ticket and returning the seat that wasn't in the ticket list.
