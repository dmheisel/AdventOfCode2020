# Day 1

This could have been a pretty simple loop through for both challenges, but I wanted to give myself a little bit of exercise with recursion.

Oh, and I've got a very basic function set up to convert the input text file into an array of numbers, saved in the utils folder so I can just call it like this

So in the find_sum function, there's some recursion. This threw me for a loop for a bit -- I'm not as familiar/used to writing recusion so it was a little bit of a headache remembering how it would need to look to work, but I got there in the end.

Now you can pass the find_sum function whatever total you want to find instead of _only_ 2020, and you can tell it how many numbers you want to use to sum them up as the _depth_ parameter.

Likely could have written it with some sort of list comprehension but...I'm bad at those, and I think with a case like this it would have been too confusing to read.
