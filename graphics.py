from PIL import Image
import ImageDraw
from itertools import cycle


def getPieces(path, gHeight, gWidth):
# Gets the graphics from the given path
# Divides the image into the given grid size
# returns a list of those pieces
    image = Image.open(path)
    set = []
    width, height = image.size
    for i in range(0, width, gWidth):
        for j in range(0, height, gHeight):
            box = (i, j, i + gWidth, j + gHeight)
            a = image.crop(box)
            set.append(a)
    return set


def assignPieces(set, pattern):
# Assign the piece image to their name
# using the pattern given in the string
    Dict = {}
    for i in range(len(set)):
        Dict[pattern[i]] = set[i]
    return Dict


def drawBoard(n=8, pixel_width=500):
    "Draw an n x n chessboard using PIL."

    def sq_start(i):
        "Return the x/y start coord of the square at column/row i."
        return i * pixel_width / n

    def square(i, j):
        "Return the square corners, suitable for use in PIL drawings"
        return map(sq_start, [i, j, i + 1, j + 1])

    image = Image.new("RGB", (pixel_width, pixel_width), color=(45, 145, 45))
    draw_square = ImageDraw.Draw(image).rectangle
    squares = (square(i, j)
               for i_start, j in zip(cycle((0, 1)), range(n))
               for i in range(i_start, n, 2))
    for sq in squares:
        draw_square(sq, fill='white')

    return image


def highlightSquare(board, square):
    # highlight the given square
    # board is the board image
    # square is the board coordinate in algebric form
    boxSize = board.size[0]/8.0
    if type(square) == str:
        square = (ord(square[0]) - 97, 8 - int(square[1]))
    box = [square[0], square[1], square[0]+1, square[1]+1]
    box = [boxSize * x for x in box]
    if (square[0] + square[1]) % 2 == 1:
        ImageDraw.Draw(board).rectangle(box, fill=(0, 100, 0))
    else:
        ImageDraw.Draw(board).rectangle(box, fill=(180, 180, 180))
    return board

def highlightElement(board, element):
    e1 = (ord(element[0][0]) - 97, 8 - int(elmenet[0][1]))
    e2 = (ord(element[1][0]) - 97, 8 - int(elmenet[1][1]))
    if e1[0] == e2[0]:
        for i in range(e1[1], e2[1]):
            highlightSquare(board, [e1[0], i])
    elif e1[1] == e2[1]:
        for i in range(e1[0], e2[0]):
            highlightSquare(board, [i, e1[1]])
    return

def convertPiece(x, y, board_width, piece_width):
    x = x * board_width/8 + 0.1 * board_width/8
    y = y * board_width/8 + 0.1 * board_width/8
    box = tuple(map(int, (x, y, x+piece_width, y+piece_width)))
    return box


def readFEN(fen):
    fen = fen.split()[0]
    fen = fen.split('/')
    for i in range(len(fen)):
        x = ''
        for j in range(len(fen[i])):
            if fen[i][j].isdigit():
                x += '.'*int(fen[i][j])
            else:
                x += fen[i][j]
        fen[i] = x
    return fen


def setBoard(board, pieces, fen):
    nBoard = board
    bSize = nBoard.size[0]
    pSize = pieces['Q'].size[0]
    for i in range(0, 8):
        for j in range(0, 8):
            if fen[i][j] != '.':
                piece = pieces[fen[i][j]]
                nBoard.paste(piece, convertPiece(j, i, bSize, pSize), mask=piece)
    nBoard.show()
    return nBoard
