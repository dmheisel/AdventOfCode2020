## Day 12! OOP Ship!

This was fun! I always enjoy object-oriented programming, and decided that today was a good exercise in making a Ship class that could track its position, heading, etc.

Because I had a good idea how to do this as soon as I read it, I also used this as an excuse to brush up on my TDD and python unit testing.

Each method was created at the same time as/right after creating the test for it -- using the standard process of

```
test -> fail test -> write code -> pass test -> new test(repeat)
```

I'm sure there could be some things cleaned up in there - it'd be a prime spot to refactor the turning, for example, but it works to spec so there's no _need_ to at this point in time.

I'm curious how the turning would handle/could be updated for smaller turns than 90 degrees, for instance. It would be fun figuring out the math/parsing the code to make that work, but at this point all turns are 90 degree turns so it's not necessary.
