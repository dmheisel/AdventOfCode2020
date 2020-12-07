# Trajectory calculation

This one was a fun one!

If I had more free time/inclination, I'd want to start exploring how to visualize this. In fact...this would be a ripe candidate for exploring some kind of terminal animations.

The problem was that we're given a pattern that's narrower than it is long. To reach the bottom, we'll need to repeat the width as we travel over and down.

My solution was to create a move function that would calculate the new position for each point on the slope. The "X" position (horizontal) would loop back to the beginning of the row if it hit the end, and the "Y" position would stay at the end if it attempted to go past it.

From there, it was simple to check each position and see if it was a tree.

Wonder if we'll see more of this sort of calculation as the month goes on?
