# Hasami Shogi

This is a portfolio project of the Japanese game named HasamiShogiGame, an abstract board game similar to checkers. The game follows  "**Variant 1**" on the [Wikipedia page](https://en.wikipedia.org/wiki/Hasami_shogi), with the starting position as follows. 

```
  1 2 3 4 5 6 7 8 9
a R R R R R R R R R
b _ _ _ _ _ _ _ _ _
c _ _ _ _ _ _ _ _ _
d _ _ _ _ _ _ _ _ _
e _ _ _ _ _ _ _ _ _
f _ _ _ _ _ _ _ _ _
g _ _ _ _ _ _ _ _ _
h _ _ _ _ _ _ _ _ _
i B B B B B B B B B
```
<h2>Requirements</h2>

* Python 2.6+
* Pygame Module 
* Simply run "Main.py"

<h2>How to Play</h2>

1. Players alternate turns (Black starts first, then Red)
2. Pieces can only move vertically or horizontally (similar to a Rook in Chess).
4. Pieces are captured (either vertically or horziontally) when they are "sandwiched" by opposing pieces, only on their turn. 

<img src="https://github.com/ChocolateTaco/Hasami-Shogi/blob/main/sample/vertical_cap.gif" width="250" height="250"/>
<em>Vertical Capture of 2 Red Pieces</em>

<img src="https://github.com/ChocolateTaco/Hasami-Shogi/blob/main/sample/horizontal_cap.gif" width="250" height="250"/>
<em>Horizontal Capture of 4 Red Pieces</em>

4. A corner piece can be captured when trapped by the two adjacent squares.
<img src="https://github.com/ChocolateTaco/Hasami-Shogi/blob/main/sample/corner_cap.gif" width="250" height="250"/>
<em>Corner Capture of 1 Black Piece</em>


5. A player cannot have their own piece(s) captured during their own turn, in the event they sandwich themselves by the opposing player.
6. A player wins when the opposing player has 1 or 0 remaining pieces in play.
