import pygame
import random
import time
import os

WIDTH, HEIGHT = 640, 480
CELL_SIZE = 40
COLS, ROWS = WIDTH // CELL_SIZE, HEIGHT // CELL_SIZE
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BACKGROUND_MUSIC_PATH = 'background.mp3'

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Game")

if not os.path.exists(BACKGROUND_MUSIC_PATH):
    print(f"Error: {BACKGROUND_MUSIC_PATH} not found.")
    exit()

try:
    pygame.mixer.music.load(BACKGROUND_MUSIC_PATH)
    pygame.mixer.music.play(-1)
except pygame.error as e:
    print(f"Error loading background music: {e}")
    exit()


class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.walls = [True, True, True, True]
        self.visited = False

    def draw(self, surface):
        x, y = self.x * CELL_SIZE, self.y * CELL_SIZE
        if self.walls[0]:
            pygame.draw.line(surface, WHITE, (x, y), (x + CELL_SIZE, y), 2)
        if self.walls[1]:
            pygame.draw.line(surface, WHITE, (x + CELL_SIZE, y), (x + CELL_SIZE, y + CELL_SIZE), 2)
        if self.walls[2]:
            pygame.draw.line(surface, WHITE, (x + CELL_SIZE, y + CELL_SIZE), (x, y + CELL_SIZE), 2)
        if self.walls[3]:
            pygame.draw.line(surface, WHITE, (x, y + CELL_SIZE), (x, y), 2)

    def highlight(self, surface, color):
        x, y = self.x * CELL_SIZE, self.y * CELL_SIZE
        pygame.draw.rect(surface, color, (x, y, CELL_SIZE, CELL_SIZE))


class Maze:
    def __init__(self):
        self.grid = [[Cell(x, y) for x in range(COLS)] for y in range(ROWS)]
        self.generate_maze()

    def generate_maze(self):
        stack = []
        current = self.grid[0][0]
        current.visited = True

        while True:
            next_cell = self.get_next_cell(current)
            if next_cell:
                next_cell.visited = True
                stack.append(current)
                self.remove_walls(current, next_cell)
                current = next_cell
            elif stack:
                current = stack.pop()
            else:
                break

    def remove_walls(self, current, next):
        dx = current.x - next.x
        dy = current.y - next.y
        if dx == 1:
            current.walls[3] = False
            next.walls[1] = False
        elif dx == -1:
            current.walls[1] = False
            next.walls[3] = False
        if dy == 1:
            current.walls[0] = False
            next.walls[2] = False
        elif dy == -1:
            current.walls[2] = False
            next.walls[0] = False

    def get_next_cell(self, cell):
        neighbors = []
        directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
        for direction in directions:
            nx, ny = cell.x + direction[0], cell.y + direction[1]
            if 0 <= nx < COLS and 0 <= ny < ROWS:
                neighbor = self.grid[ny][nx]
                if not neighbor.visited:
                    neighbors.append(neighbor)
        if neighbors:
            return random.choice(neighbors)
        return None

    def draw(self, surface):
        for row in self.grid:
            for cell in row:
                cell.draw(surface)


class Player:
    def __init__(self, start_cell, goal_cell):
        self.cell = start_cell
        self.goal = goal_cell
        self.start_time = time.time()

    def move(self, direction, grid):
        if direction == 'UP' and not self.cell.walls[0]:
            self.cell = grid[self.cell.y - 1][self.cell.x]
        elif direction == 'DOWN' and not self.cell.walls[2]:
            self.cell = grid[self.cell.y + 1][self.cell.x]
        elif direction == 'LEFT' and not self.cell.walls[3]:
            self.cell = grid[self.cell.y][self.cell.x - 1]
        elif direction == 'RIGHT' and not self.cell.walls[1]:
            self.cell = grid[self.cell.y][self.cell.x + 1]

    def highlight(self, surface, color):
        self.cell.highlight(surface, color)

    def reached_goal(self):
        return self.cell == self.goal

    def get_elapsed_time(self):
        return time.time() - self.start_time


class Game:
    def __init__(self, players_count):
        self.players_count = players_count
        self.players_times = [0] * players_count

    def play(self):
        for i in range(self.players_count):
            maze = Maze()
            player = Player(maze.grid[0][0], maze.grid[ROWS - 1][COLS - 1])

            clock = pygame.time.Clock()
            running = True

            while running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()

                keys = pygame.key.get_pressed()
                if keys[pygame.K_UP]:
                    player.move('UP', maze.grid)
                if keys[pygame.K_DOWN]:
                    player.move('DOWN', maze.grid)
                if keys[pygame.K_LEFT]:
                    player.move('LEFT', maze.grid)
                if keys[pygame.K_RIGHT]:
                    player.move('RIGHT', maze.grid)

                screen.fill(BLACK)
                maze.draw(screen)
                player.highlight(screen, GREEN)
                player.goal.highlight(screen, RED)
                pygame.display.flip()

                if player.reached_goal():
                    elapsed_time = player.get_elapsed_time()
                    self.players_times[i] = elapsed_time
                    print(f"Player {i + 1} finished the maze in {elapsed_time:.2f} seconds.")
                    running = False

                clock.tick(30)

        winner_index = self.players_times.index(min(self.players_times))
        print(f"Player {winner_index + 1} wins the game with a time of {self.players_times[winner_index]:.2f} seconds.")


if __name__ == "__main__":
    players_count = int(input("Enter the number of players: "))
    game = Game(players_count)
    game.play()
    pygame.quit()
