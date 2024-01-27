import pyte

class terminal:
    def __init__(self,width=80,height=25):
        self.screen = pyte.Screen(width,height)
        self.stream = pyte.Stream(screen)
    def feed(self):
        self.stream.feed(bin_str)
    def display(self):
        return self.screen.display
