from random import randint
import tkinter as tk
from PIL import Image, ImageTk
import os
import sys

MOVE_INCREMENT = 20
move_per_second = 10
GAME_SPEED = 1000 // move_per_second


class Snake(tk.Canvas):
    def __init__(self):
        super().__init__(height=620, width=600, background="black", highlightthickness=0)

        self.running = True  # control loop safely

        # game state
        self.snake_positions = [(100, 100), (80, 100), (60, 100)]
        self.food_positions = self.set_food_position()
        self.score = 0
        self.direction = "Right"

        if not self.load_assets():
            return

        self.create_object()
        self.after(GAME_SPEED, self.perform_actions)

        self.bind_all('<Key>', self.on_key_press)

    # ------------------ ASSETS ------------------
    def load_assets(self):
        try:
            base_path = os.path.dirname(__file__)

            snake_path = os.path.join(base_path, "assets", "snake.png")
            food_path = os.path.join(base_path, "assets", "food.png")

            self.snake_body_image = Image.open(snake_path)
            self.snake_body = ImageTk.PhotoImage(self.snake_body_image)

            self.food_image = Image.open(food_path)
            self.food = ImageTk.PhotoImage(self.food_image)

            return True

        except Exception as e:
            print("Asset loading failed:", e)
            sys.exit(1)  # safe exit

    # ------------------ CREATE OBJECTS ------------------
    def create_object(self):
        self.create_text(
            45, 12,
            text=f"Score: {self.score}",
            tag="Score",
            fill="#fff",
            font=("Arial", 14)
        )

        for x, y in self.snake_positions:
            self.create_image(x, y, image=self.snake_body, tag="Snake")

        self.create_image(*self.food_positions, image=self.food, tag="Food")
        self.create_rectangle(7, 27, 593, 613, outline="#525d69")

    # ------------------ GAME LOOP ------------------
    def perform_actions(self):
        if not self.running:
            return

        if self.check_collision():
            self.end_game()
            return

        self.check_food_collision()
        self.move_snake()

        self.after(GAME_SPEED, self.perform_actions)

    # ------------------ MOVEMENT ------------------
    def move_snake(self):
        head_x, head_y = self.snake_positions[0]

        if self.direction == "Right":
            new_head = (head_x + MOVE_INCREMENT, head_y)
        elif self.direction == "Left":
            new_head = (head_x - MOVE_INCREMENT, head_y)
        elif self.direction == "Up":
            new_head = (head_x, head_y - MOVE_INCREMENT)
        else:
            new_head = (head_x, head_y + MOVE_INCREMENT)

        self.snake_positions = [new_head] + self.snake_positions[:-1]

        for segment, position in zip(self.find_withtag("Snake"), self.snake_positions):
            self.coords(segment, position)

    # ------------------ INPUT ------------------
    def on_key_press(self, e):
        new_direction = e.keysym
        all_directions = ("Up", "Down", "Right", "Left")
        opposite = ({"Up", "Down"}, {"Left", "Right"})

        if new_direction in all_directions and {new_direction, self.direction} not in opposite:
            self.direction = new_direction

    # ------------------ COLLISIONS ------------------
    def check_collision(self):
        x, y = self.snake_positions[0]

        return (
            x < 10 or x > 590 or
            y < 30 or y > 610 or
            (x, y) in self.snake_positions[1:]
        )

    def check_food_collision(self):
        if self.snake_positions[0] == self.food_positions:
            self.score += 1
            self.snake_positions.append(self.snake_positions[-1])

            global move_per_second
            if self.score % 5 == 0:
                move_per_second += 1

            self.create_image(*self.snake_positions[-1], image=self.snake_body, tag="Snake")

            self.food_positions = self.set_food_position()
            self.coords(self.find_withtag("Food"), self.food_positions)

            self.itemconfigure("Score", text=f"Score: {self.score}")

    # ------------------ FOOD ------------------
    def set_food_position(self):
        while True:
            x = randint(1, 29) * MOVE_INCREMENT
            y = randint(3, 30) * MOVE_INCREMENT

            if (x, y) not in self.snake_positions:
                return (x, y)

    # ------------------ END GAME ------------------
    def end_game(self):
        self.running = False
        self.delete(tk.ALL)

        self.create_text(
            self.winfo_width() / 2,
            self.winfo_height() / 2,
            text=f"Game Over! Score: {self.score}",
            fill="#fff",
            font=("Arial", 24)
        )

        self.restart_button = tk.Button(
            self,
            text="Restart",
            font=("Arial", 14),
            command=self.restart_game,
            bg="black",
            fg="white",
            bd=0
        )

        self.create_window(
            self.winfo_width() / 2,
            self.winfo_height() / 1.6,
            window=self.restart_button
        )

    # ------------------ RESTART ------------------
    def restart_game(self):
        self.running = True

        self.snake_positions = [(100, 100), (80, 100), (60, 100)]
        self.food_positions = self.set_food_position()
        self.score = 0
        self.direction = "Right"

        global move_per_second
        move_per_second = 10

        self.delete(tk.ALL)
        self.create_object()

        self.after(GAME_SPEED, self.perform_actions)


# ------------------ MAIN ------------------
root = tk.Tk()
root.title("Snake Game")
root.resizable(False, False)

board = Snake()
board.pack()

root.mainloop()