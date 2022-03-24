# Hasami Shogi

This is a portfolio project of the Japanese game named HasamiShogiGame, an abstract board game similar to checkers. The game works by using the rules for "**Variant 1**" on [the Wikipedia page](https://en.wikipedia.org/wiki/Hasami_shogi), including the diagram of the starting position. Custodian captures may be made on multiple sides (up to 3 sides) of the moved piece. For example if the black piece on square h6 in the diagram below moves to square c6, then the red pieces at c4, c5, and b6 would be captured. If instead, the black piece at h6 moves to h1, then the red pieces at e1, f1, g1, and i1 would be captured.

```
  1 2 3 4 5 6 7 8 9
a _ _ _ _ _ B _ _ _
b _ _ _ _ _ R _ _ _
c _ _ B R R _ _ _ _
d B _ _ _ _ _ _ _ _
e R _ _ _ _ _ _ _ _
f R _ _ _ _ _ _ _ _
g R _ _ _ _ _ _ _ _
h _ _ _ _ _ B _ _ _
i R B _ _ _ _ _ _ _
```

Locations on the board will be specified using "algebraic notation", with rows labeled a-i and rows labeled 1-9, as shown in the diagram of the starting position shown on the Wikipedia page.

Vertical Capture of 2 Red Pieces
![](https://github.com/ChocolateTaco/Hasami-Shogi/blob/main/sample/vertical_cap.gif | width=200)

Horizontal Capture of 4 Red Pieces
![](https://github.com/ChocolateTaco/Hasami-Shogi/blob/main/sample/horizontal_cap.gif | width=200)

Corner Capture of 1 Black Piece
![](https://github.com/ChocolateTaco/Hasami-Shogi/blob/main/sample/corner_cap.gif | width=200)

