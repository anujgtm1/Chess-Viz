import graphics as g
pattern = "KkQqBbNnRrPp"
fen = "rnbqkbnr/pp1ppppp/8/2p5/4P3/5N2/PPPP1PPP/RNBQKB1R b KQkq - 1 2"

p = g.assignPieces(g.getPieces("Graphics/Pieces.png", 50, 50), pattern)
b = g.drawBoard()
f = g.readFEN(fen)
fb = b.copy()
fb = g.setBoard(fb, p, f)
