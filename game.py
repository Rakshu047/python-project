from grid import Grid
from blocks import *
import random

class Game:
    def __init__(self):
        self.grid = Grid()
        self.blocks = [LBlock(),JBlock(),IBlock(),OBlock(),SBlock(),TBlock(),ZBlock()]
        self.cur_block = self.get_random_block()
        self.next_block = self.get_random_block()

    def get_random_block(self):
        if len(self.blocks) == 0:
            self.blocks = [LBlock(),JBlock(),IBlock(),OBlock(),SBlock(),TBlock(),ZBlock()]
        block = random.choice(self.blocks)
        self.blocks.remove(block)
        return block
    
    def move_left(self):
        self.cur_block.move(0,-1)
        if self.block_inside() == False:
            self.cur_block.move(0,1)
    
    def move_right(self):
        self.cur_block.move(0,1)
        if self.block_inside() == False:
            self.cur_block.move(0,-1)

    def move_down(self):
        self.cur_block.move(1,0)
        if self.block_inside() == False:
            self.cur_block.move(-1,0)

    def rotate(self):
        self.cur_block.rotate()
        if self.block_inside() == False:
            self.cur_block.undo_rotate()

    def block_inside(self):
        tiles = self.cur_block.get_cell_position()
        for tile in tiles:
            if self.grid.is_inside(tile.row,tile.column) == False:
                return False
        return True
    
    def draw(self,screen):
        self.grid.draw(screen)
        self.cur_block.draw(screen)