import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import Layers
from kmk.modules.encoder import EncoderHandler


keyboard = KMKKeyboard()
keyboard.modules.append(Layers())
encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)

keyboard.col_pins = (board.GP13,board.GP19,board.GP20,board.GP26,board.GP27,board.GP28,board.GP4)
keyboard.row_pins = (board.GP12,board.GP11,board.GP10,board.GP9)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

FN_MOMENTARY = KC.MO(1)

keyboard.keymap = [
    [KC.C, KC.P, KC.K, KC.N7, KC.N8, KC.N9, KC.U,
    KC.M, KC.O, KC.S, KC.N4, KC.N5, KC.N6, KC.BSPACE,
    KC.T, KC.R, KC.V, KC.N1, KC.N2, KC.N3, KC.ENTER,
    KC.A, FN_MOMENTARY, KC.NO, KC.N0, KC.DOT, KC.MINUS, KC.NO],

    [KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, 
     KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, 
     KC.NO, KC.NO, KC.NO, KC.I, KC.D, KC.NO, KC.NO, 
     KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, ]
]

encoder_handler.pins = (
    (board.GP6, board.GP7, None)
)

encoder_handler.map = [((KC.B,KC.N,KC.NO))]

if __name__ == '__main__':
    keyboard.go()