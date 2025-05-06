#!/usr/bin/env python3
import random

class Minesweeper:
    def __init__(self, width=10, height=10, mines=10):
        self.width = width
        self.height = height
        self.mines = set(random.sample(range(width * height), mines))
        self.revealed = [[False for _ in range(width)] for _ in range(height)]

    def count_mines_nearby(self, x, y):
        count = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    if (ny * self.width + nx) in self.mines:
                        count += 1
        return count

    def reveal_all(self):
        for y in range(self.height):
            for x in range(self.width):
                if (y * self.width + x) not in self.mines:
                    self.revealed[y][x] = True

    def print_empty_board(self):
        print('0 1 2 3 4 5 6 7 8 9')
        for i in range(1, self.height):
            print(i)

    def print_revealed_board(self):
        print('0 1 2 3 4 5 6 7 8 9')
        for y in range(self.height):
            print(y, end=' ')
            for x in range(self.width):
                index = y * self.width + x
                if index in self.mines:
                    print('.', end=' ')
                elif self.revealed[y][x]:
                    count = self.count_mines_nearby(x, y)
                    print(count if count > 0 else ' ', end=' ')
                else:
                    print('.', end=' ')
            print()

    def run_script(self):
        self.print_empty_board()
        print('...\n...\n0 1 2 3 4 5 6 7 8 9')
        self.reveal_all()
        self.print_revealed_board()
        print("Congratulations! You've won the game.")

if __name__ == "__main__":
    game = Minesweeper()
    game.run_script()
