class Star:
    def __init__(self, intensity: int, size: int, colour: str, x: int, y: int) -> None:
        self.intensity = intensity
        self.size = size
        self.colour = colour
        self.x = x
        self.y = y
    
    def __str__(self) -> str:
        return f"Star: intensity={self.intensity}, size={self.size}, colour={self.colour}"