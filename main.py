import pyautogui
import random
import PIL
import sys
import time
MINESWEEPER_PATH = r'"C:\Users\Eyal\Documents\MineSweepePy\MineSweeper_Online_v1.4.0\MineSweeper Online.exe"'
TILE_IMAGE_PATH = r"C:\Users\Eyal\Documents\MineSweepePy\Images\Tile_small.png"
MINE_IMAGE_PATH = r"C:\Users\Eyal\Documents\MineSweepePy\Images\Mine_small.png"
ONE_IMAGE_PATH = r"C:\Users\Eyal\Documents\MineSweepePy\Images\1.png"
TWO_IMAGE_PATH = r"C:\Users\Eyal\Documents\MineSweepePy\Images\2.png"
THREE_IMAGE_PATH = r"C:\Users\Eyal\Documents\MineSweepePy\Images\3.png"
FOUR_IMAGE_PATH = r"C:\Users\Eyal\Documents\MineSweepePy\Images\4.png"
EMPTY_IMAGE_PATH = r"C:\Users\Eyal\Documents\MineSweepePy\Images\empty.png"
UNOPENED = 0
EMPTY = -1
MINE = 'm'
MINE_RGB = (119, 119, 119)
EMPTY_RGB = (205, 205, 255)
NUMBERS_RGB = [(0, 0, 255), (0, 128, 0), (228, 109, 136)]
UNOPENED_RGB = (0, 176, 166)

# PIL.ImageColor.getcolor('red', 'L')
# PIL.ImageColor.getcolor('blue')
#values: unopened, empty, mine, number
#PIL.ImageColor.getrgb(color)

class Strategy:
    def __init__(self, board):
        self.board = board

    def single_number_tile(self):
        pass

    def click_corners(self):
        board.get_corners()
        self.board.board[0].click()


    def random_click(self):
        random.choice(self.board.board).click()

class Tile:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.value = UNOPENED

    def click(self):
        pyautogui.click(x=self.x, y=self.y)

    def flag(self):
        pyautogui.rightClick(x=self.x, y=self.y)

    def multi_click(self):
        pyautogui.mouseDown(button='right', x=self.x, y=self.y)
        pyautogui.mouseDown(button='left', x=self.x, y=self.y)
        pyautogui.mouseUp(button='left')
        pyautogui.mouseUp(button='right')


class Board:
    def __init__(self):
        self.board = []
        positions = pyautogui.locateAllOnScreen(TILE_IMAGE_PATH, confidence=0.6)
        for pos in positions:
            center = pyautogui.center(pos)
            self.board.append(Tile(center.x, center.y))

    def update_board(self):
        im1 = pyautogui.screenshot().convert("RGB")
        colors = []
        for tile in self.board:
           color = im1.getpixel((int(tile.x), int(tile.y)))
           if color not in colors:
               colors.append(color)
           if color == MINE_RGB:
               print('You lose')
               sys.exit()
           elif color == EMPTY_RGB:
               print('empty found')
               tile.value = EMPTY
           elif color in NUMBERS_RGB:
               print('number found')
               tile.value = NUMBERS_RGB.index(color) + 1

        #     if pyautogui.locateOnScreen(MINE_IMAGE_PATH, confidence=0.6, region=(tile.x, tile.y, 500, 500)):
        #         tile.value = MINE
        #     elif pyautogui.locateOnScreen(ONE_IMAGE_PATH, confidence=0.6, region=(tile.x, tile.y, 500, 500)):
        #         tile.value = 1
        #     elif pyautogui.locateOnScreen(TWO_IMAGE_PATH, confidence=0.6, region=(tile.x, tile.y, 500, 500)):
        #         tile.value = 2
        #     elif pyautogui.locateOnScreen(THREE_IMAGE_PATH, confidence=0.6, region=(tile.x, tile.y, 500, 500)):
        #         tile.value = 3
        #     elif pyautogui.locateOnScreen(FOUR_IMAGE_PATH, confidence=0.6, region=(tile.x, tile.y, 500, 500)):
        #         tile.value = 4
        #     elif pyautogui.locateOnScreen(EMPTY_IMAGE_PATH, confidence=0.6, region=(tile.x, tile.y, 500, 500)):
        #         tile.value = EMPTY
    def get_corners(self):
        pass

def main():
    board = Board()
    strategy = Strategy(board)
    while True:
        strategy.click_corners()
        strategy.random_click()
        time.sleep(1)
        board.update_board()

    # while not pyautogui.locateOnScreen(MINE_IMAGE_PATH, confidence=0.5):
    #     positions = list(pyautogui.locateAllOnScreen(TILE_IMAGE_PATH, confidence=0.6))
    #     if not positions:
    #         print('You won')
    #         break
    #     pos = random.choice(positions)
    #     print(f"pressed {pos}")
    #     pyautogui.click(x=pos.left, y=pos.top)


if __name__ == '__main__':
    main()
