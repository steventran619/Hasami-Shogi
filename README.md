<p align="center">
  <img src="https://github.com/ChocolateTaco/Hasami-Shogi/blob/main/sample/Title.png">
</p>

Hasami Shogi is a Japanese board game, similar to checkers with rook chess pieces. This version of the game follows "Variant 1" on the [Wikipedia page](https://en.wikipedia.org/wiki/Hasami_shogi). The game is intended to be played with two players.

## Prerequisites
[Python 3.6 or later](https://www.python.org/)

## Installation##
1. Clone the repo to a local directory
2. In the local directory, open a terminal and install the requirements:
  `
  pip install -r requirements.txt
  `
3. In the terminal run the following:
  ```
  python3 Main.py
  ```
<h2>How to Play</h2>

1. Players alternate turns (Black starts first, then Red)
2. Pieces can only move vertically or horizontally (similar to a Rook in Chess).
4. Pieces are captured (either vertically or horziontally) when they are "sandwiched" by opposing pieces, only on their turn. 

<img src="https://github.com/ChocolateTaco/Hasami-Shogi/blob/main/sample/vertical_cap.gif" width="275" height="275"/>
<em>Vertical Capture of 2 Red Pieces</em>

<img src="https://github.com/ChocolateTaco/Hasami-Shogi/blob/main/sample/horizontal_cap.gif" width="275" height="275"/>
<em>Horizontal Capture of 4 Red Pieces</em>

4. A corner piece can be captured when trapped by the two adjacent squares.
<img src="https://github.com/ChocolateTaco/Hasami-Shogi/blob/main/sample/corner_cap.gif" width="275" height="275"/>
<em>Corner Capture of 1 Black Piece</em>


5. A player cannot have their own piece(s) captured during their own turn, in the event they sandwich themselves by the opposing player.
6. A player wins when the opposing player has 1 or 0 remaining pieces in play.
