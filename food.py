class Food:
    def __init__(self, width, height):
        import random
        self.width = width
        self.height = height
        self.position = self.generate_food_position()

    def generate_food_position(self):
        x = random.randint(0, self.width - 1)
        y = random.randint(0, self.height - 1)
        return (x, y)

    def check_collision(self, snake_position):
        return self.position == snake_position

    def refresh_food(self):
        self.position = self.generate_food_position()