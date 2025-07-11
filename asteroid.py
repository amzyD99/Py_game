class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(self, x, y, radius)
    
    def draw(self):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)

    def update(self):
        self.position += self.velocity * dt