# portfolio-project

This is a portfolio project of the Japanese game named HasamiShogiGame, an abstract board game similar to checkers. The game works by using the rules for "**Variant 1**" on [the Wikipedia page](https://en.wikipedia.org/wiki/Hasami_shogi), including the diagram of the starting position. Custodian captures may be made on multiple sides (up to 3 sides) of the moved piece. For example if the black piece on square h6 in the diagram below moves to square c6, then the red pieces at c4, c5, and b6 would be captured. If instead, the black piece at h6 moves to h1, then the red pieces at e1, f1, g1, and i1 would be captured.

```
  1 2 3 4 5 6 7 8 9
a . . . . . B . . .
b . . . . . R . . .
c . . B R R . . . .
d B . . . . . . . .
e R . . . . . . . .
f R . . . . . . . .
g R . . . . . . . .
h . . . . . B . . .
i R B . . . . . . .
```

Locations on the board will be specified using "algebraic notation", with rows labeled a-i and rows labeled 1-9, as shown in the diagram of the starting position shown on the Wikipedia page.
