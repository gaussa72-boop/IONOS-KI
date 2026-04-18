class World:
    def __init__(self):
        self.state = "Genesis"

    def evolve(self, action):
        if "light" in action:
            self.state = "Lichtwelt entsteht"
        elif "shadow" in action:
            self.state = "Schatten-Dimension aktiviert"
        else:
            self.state = "Neutralraum stabil"

        return self.state