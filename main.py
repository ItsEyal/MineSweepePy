import pyautogui
import random
#rightClick()
#identify numbers
MINESWEEPER_PATH = r'"C:\Users\Eyal\Documents\MineSweepePy\MineSweeper_Online_v1.4.0\MineSweeper Online.exe"'
TILE_IMAGE_PATH = r"C:\Users\Eyal\Documents\MineSweepePy\Images\Tile_small.png"
MINE_IMAGE_PATH = r"C:\Users\Eyal\Documents\MineSweepePy\Images\Mine_small.png"


def main():
    while not pyautogui.locateOnScreen(MINE_IMAGE_PATH, confidence=0.5):
        positions = list(pyautogui.locateAllOnScreen(TILE_IMAGE_PATH, confidence=0.6))
        if not positions:
            print('You won')
            break
        pos = random.choice(positions)
        print(f"pressed {pos}")
        pyautogui.click(x=pos.left, y=pos.top)


if __name__ == '__main__':
    main()
