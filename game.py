from msilib.schema import SelfReg
from grid import Grid
from blocks import *
import random

class Game:
    def __init__(self):
        self.grid = Grid()
        self.blocks = [LBlock(),JBlock(),IBlock(),OBlock(),SBlock(),TBlock(),ZBlock()]
        self.cur_block = self.get_random_block()
        self.next_block = self.get_random_block()
        self.game_over = False
        self.score = 0

    def get_random_block(self):
        if len(self.blocks) == 0:
            self.blocks = [LBlock(),JBlock(),IBlock(),OBlock(),SBlock(),TBlock(),ZBlock()]
        block = random.choice(self.blocks)
        self.blocks.remove(block)
        return block
    
    def move_left(self):
        self.cur_block.move(0,-1)
        if self.block_inside() == False or self.block_fits() == False:
            self.cur_block.move(0,1)
    
    def move_right(self):
        self.cur_block.move(0,1)
        if self.block_inside() == False or self.block_fits() == False:
            self.cur_block.move(0,-1)

    def move_down(self):
        self.cur_block.move(1,0)
        if self.block_inside() == False or self.block_fits() == False:
            self.cur_block.move(-1,0)
            self.lock_block()

    def lock_block(self):
        tiles = self.cur_block.get_cell_position()
        for pos in tiles:
            self.grid.grid[pos.row][pos.column] = self.cur_block.id
        self.cur_block = self.next_block
        self.next_block = self.get_random_block()
        lines_cleared=self.grid.clear_full_rows()
        self.update_score(lines_cleared)
        if self.block_fits() == False:
            self.game_over = True
 
    def block_fits(self):
        tiles = self.cur_block.get_cell_position()
        for tile in tiles:
            if self.grid.is_empty(tile.row, tile.column) == False:
                return False
        return True 

    def rotate(self):
        self.cur_block.rotate()
        if self.block_inside() == False or self.block_fits() == False:
            self.cur_block.undo_rotate()

    def block_inside(self):
        tiles = self.cur_block.get_cell_position()
        for tile in tiles:
            if self.grid.is_inside(tile.row,tile.column) == False:
                return False
        return True
    
    def reset(self):
        self.grid.reset()
        self.cur_block = self.get_random_block()
        self.next_block = self.get_random_block()
        self.score = 0

    def update_score(self, lines_cleared):
        if lines_cleared == 1:
            self.score += 100
        elif lines_cleared == 2:
            self.score += 300
        elif lines_cleared == 3:
            self.score += 500
        elif lines_cleared >= 4:
            self.score += 1000
    
    def draw(self,screen):
        self.grid.draw(screen)
        self.cur_block.draw(screen, 11, 11)
        if self.next_block.id == 4:
            self.next_block.draw(screen,255,270)
        elif self.next_block.id == 3:
            self.next_block.draw(screen,255,290)
        else:
            self.next_block.draw(screen,270,270)