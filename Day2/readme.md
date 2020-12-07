## Day 2!

Time for some validation, it seems!

So, this was two separate chunks for me. First one splitting up the input. There were three separate chunks here, easily identifiable portions on each line that serve as instructions for validating the password.
It was simple enough to split, though I feel my parse_input function and parse_line function could be a little bit cleaner.

More fun for me was setting up the Pass class. I like the idea of passing in the broken down instructions (limits, letter, and password) to a class that would create and validate itself.

Even better when part two included a revised validation, all I had to do was create a second type of validation on the class and could leave the first one -- you know, for if the client ever changed their mind. ;)
