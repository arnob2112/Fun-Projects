from random import randint
import tkinter as tk
from PIL import Image, ImageTk

MOVE_INCREMENT = 20
move_per_second = 10
GAME_SPEED = 1000 // move_per_second


class Snake(tk.Canvas):
    def __init__(self):
        super().__init__(height=620, width=600, background="Black", highlightthickness=0)

        # class variables
        self.snake_positions = [(100, 100), (80, 100), (60, 100)]
        self.food_positions = self.set_food_position()
        self.score = 0
        self.direction = "Right"

        self.load_assets()
        self.create_object()
        self.after(75, self.perform_actions)

        # binding buttons
        self.bind_all('<Key>', self.on_key_press)

    # loading images from assets
    def load_assets(self):
        try:
            self.snake_body_image = Image.open("assets/snake.png")
            self.snake_body = ImageTk.PhotoImage(self.snake_body_image)

            self.food_image = Image.open("assets/food.png")
            self.food = ImageTk.PhotoImage(self.food_image)
        except IOError as e:
            print("error!")
            root.destroy()

    def create_object(self):
        try:
            self.create_text(45, 12,
                             text=f"Score: {self.score}",
                             tag="Score", fill="#fff",
                             font=("Arial", 14))
        except Exception as e:
            print(e)

        for x_position, y_position in self.snake_positions:
            self.create_image(x_position, y_position, image=self.snake_body, tag="Snake")

        self.create_image(*self.food_positions, image=self.food, tag='Food')
        self.create_rectangle(7, 27, 593, 613, outline="#525d69")

    def move_snake(self):
        head_x_position, head_y_position = self.snake_positions[0]
        if self.direction == "Right":
            new_head_positions = (head_x_position + MOVE_INCREMENT, head_y_position)
        elif self.direction == "Left":
            new_head_positions = (head_x_position - MOVE_INCREMENT, head_y_position)
        elif self.direction == "Up":
            new_head_positions = (head_x_position, head_y_position - MOVE_INCREMENT)
        elif self.direction == "Down":
            new_head_positions = (head_x_position, head_y_position + MOVE_INCREMENT)

        self.snake_positions = [new_head_positions] + self.snake_positions[:-1]

        for segment, position in zip(self.find_withtag("Snake"), self.snake_positions):
            self.coords(segment, position)

    def perform_actions(self):
        if self.check_collision():
            self.end_game()
            return

        self.check_food_collision()
        self.move_snake()
        self.after(GAME_SPEED, self.perform_actions)

    def check_collision(self):
        head_x_position, head_y_position = self.snake_positions[0]
        return (head_x_position in (0, 600)
                or head_y_position in (20, 620)
                or (head_x_position, head_y_position) in self.snake_positions[1:])

    def on_key_press(self, e):
        new_direction = e.keysym
        all_directions = ("Up", "Down", "Right", "Left")
        opposite_directions = ({"Up", "Down"}, {"Right", "Left"})
        if new_direction in all_directions and {new_direction, self.direction} not in opposite_directions:
            self.direction = new_direction

    def check_food_collision(self):
        if self.snake_positions[0] == self.food_positions:
            self.score += 1
            self.snake_positions.append(self.snake_positions[-1])

            if self.score % 5 == 0:
                global move_per_second
                move_per_second += 1

            self.create_image(*self.snake_positions[-1], image=self.snake_body, tag="Snake")
            self.food_positions = self.set_food_position()
            self.coords(self.find_withtag("Food"), self.food_positions)
            score = self.find_withtag("Score")
            self.itemconfigure(score, text=f"Score: {self.score}", tag="Score")

    def set_food_position(self):
        while True:
            x_position = randint(1,29) * MOVE_INCREMENT
            y_position = randint(3,30) * MOVE_INCREMENT
            food_positions = (x_position, y_position)
            if food_positions not in self.snake_positions:
                return food_positions

    def end_game(self):
        self.delete(tk.ALL)
        self.create_text(
            self.winfo_width() / 2,
            self.winfo_height() / 2,
            text=f"Game over! You Scored {self.score}!",
            fill="#fff",
            font=("Arial", 24)
        )
        self.create_text(
                         self.winfo_width() / 2,
                         self.winfo_height() / 1.8,
                         text="Created by Arnob.",
                         fill="#fcc603",
                         font=("Arial", 14))


root = tk.Tk()
root.title("Snake Game - Arnob")
root.resizable(False, False)

board = Snake()
board.pack()

root.mainloop()
