# Day 6!

Time for some list comprehension madness, y'all.

At first, I had:

```
letter for form in group for letter in form if all(letter in form for form in group
```

_whew_

So, that's to create a set for each `letter` from each `form` in the `group` if that `letter` is in **all** of the `form`s in the `group`

And since sets don't repeat entries, it gets us a nice list of all of the answers that _everyone_ in the group answered yes to.

Then I realized I could have it loop over the total_yeses set -- that has all of the unique answers from the group anyways, and would have less loops to run through.

And _then_ I realized instead of doing a long list comprehension with an if statement in it I could use the filter() method and save a bit of space there, too.

so we end up with

```
set(filter(lambda x: all(x in form for form in group), total_yeses))
```

And that doesn't look _nearly_ as bad!
