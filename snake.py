class Snake:
    def __init__(self):
        self.body = [(0, 0)]  # Starting position of the snake
        self.direction = (1, 0)  # Initial movement direction (to the right)

    def move(self):
        head_x, head_y = self.body[0]
        new_head = (head_x + self.direction[0], head_y + self.direction[1])
        self.body.insert(0, new_head)  # Add new head position to the snake's body
        self.body.pop()  # Remove last segment of the snake

    def grow(self):
        tail_x, tail_y = self.body[-1]
        self.body.append((tail_x, tail_y))  # Add a new segment at the tail of the snake

    def set_direction(self, new_direction):
        # Prevent the snake from going in the opposite direction
        if (new_direction[0] * -1, new_direction[1] * -1) != self.direction:
            self.direction = new_direction

    def check_collision(self):
        head = self.body[0]
        # Check if the snake collides with itself
        if head in self.body[1:]:
            return True
        return False
