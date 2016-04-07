import graphics as g
pattern = "PBQpbqNRKnrk"
fen = "rnbqkbnr/pp1ppppp/8/2p5/4P3/5N2/PPPP1PPP/RNBQKB1R b KQkq - 1 2"

p = g.assignPieces(g.getPieces("p.png",50,50),pattern)
b = g.drawBoard()
f = g.readFEN(fen)

g.setBoard(b,p,f)

