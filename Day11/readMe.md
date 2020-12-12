## Day 11:

This day was a bit of a doozy!

I had to stop and re-do everything halfway through when I realized my first attempt was horribly inefficient and took upwards of 10 seconds to complete just part one.

I initially had thought to use `numpy` and it's easy ability to manipulate matrixes. But I don't know it well enough to use its built-in functionalities and apparently if you don't use it right you're liable to have a very resource intensive program.

This was also my first use of `functools` -> `cache`. Since there was no guarantee of how many times this was going to have to repeat the iteration until it completed, and we always had the same neighbors for each seat, I cached the results of the call to get the neighbors or the first visible seats. That way it only took the most resources the first time around and each cycle tick it should be able to use the cached results for each board position, saving some resources.

In the end it was a fun challenge to use for figuring out the best way to iterate over a matrix and manipulate/determine new data for each point.

Also, I'm happy with my understanding of list comprehension now -- the `directions` variable in the `get_visible` function is:

```py
directions = [(i, j) for j in range(-1, 2) for i in range(-1, 2) if (i, j) != (0, 0)]
```

Which should come out to something along the lines of:

```py
# [(-1, 0), (1, 0), (-1, -1),(-1, 1), (1, -1) (1, 1), (0, -1), (0, 1)]
```

This should get me all of the cardinal directions from the center point `(0,0)`. And when I use it by adding to the center point of (row, col), it should allow me to increment out in all the cardinal directions from whatever point and find the first visible seat.
