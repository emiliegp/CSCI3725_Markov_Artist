"""
    Emilie Grand'Pierre 
    Computational Creativity 

    In this model, music notes in my three favorties songs are used to create a patchworked masterpiece using the Turtle package. 
    The transition matrix is defined by my top songs of 2022: "Show Me" by James Blake, "Phoenix" by 
    ASAP Rocky, and "Comfortably Numb" by Pink Floyd. I simplified the notes to exclude the sharps and flats; if the
    song includes a particular note, then it is considered in the transition matrix.
    Notes are then mapped to specific colors: 
        F --> green
        C --> red
        E --> orange
        B --> pink
        D --> brown
        A --> purple
        G --> blue 
"""


import turtle
import numpy as np

TURTLE_SIZE =20
SQUARE_SIZE = 75

class MarkovArtist:
    def __init__(self, transition_matrix):
        """

        """
        self.transitionMatrix = transition_matrix
        self.strokes = list(transition_matrix.keys())
        self.patiningColors = []

    def get_next_stroke(self, current_stroke):
        """
        """
        return np.random.choice(
            self.strokes,
            p=[self.transitionMatrix[current_stroke][next_stroke] for next_stroke in self.strokes]
        )
        

    def create_painting_scheme(self, num_strokes, current_note="A"):
        """
            Generate a sequence of notes.
            :param current_note: (str) note of song we are currently looking at
            :param num_strokes: (int) number of notes per song
        """
        painting = []
        while len(painting) < num_strokes:
            next_stroke = self.get_next_stroke(current_note)
            painting.append(next_stroke)
            current_note = next_stroke

        self.note_to_color(painting)


    def note_to_color(self, matrix):
        for note in matrix:
            if note == "F":
                self.patiningColors.append("Green")
            elif note == "C":
                self.patiningColors.append("Red")
            elif note == "E":
                self.patiningColors.append("Green")
            elif note == "B":
                self.patiningColors.append("Pink")
            elif note == "D":
                self.patiningColors.append("Brown")
            elif note == "A":
                self.patiningColors.append("Purple")
            elif note == "G":
                self.patiningColors.append("Blue")

def square(turtle):
        for x in range(4):
            turtle.forward(SQUARE_SIZE)
            turtle.right(90)

def paint(screen, turtle, matrix):
    grid_size = (int) (screen.window_height()/SQUARE_SIZE)
    square_counter = 0
    for x in range(grid_size):
        for y in range(grid_size):
            turtle.begin_fill()
            square(turtle)
            #TODO Initiate choose color method 
            turtle.color(matrix[square_counter])
            square_counter = square_counter + 1
            turtle.end_fill()
            turtle.color("Black")
            turtle.forward(SQUARE_SIZE)
        turtle.backward(SQUARE_SIZE * grid_size)
        turtle.right(90)
        turtle.forward(SQUARE_SIZE)
        turtle.left(90)
    
def main():
    window = turtle.Screen()
    window.screensize(canvwidth=(SQUARE_SIZE), canvheight=(SQUARE_SIZE))
    window.bgcolor("White")
    
    canvas = turtle.Turtle()
    canvas.speed(10)
    canvas.penup()
    canvas.goto(TURTLE_SIZE/2 - window.window_width()/2, window.window_height()/2 - TURTLE_SIZE/2)
    canvas.pendown()

    grid_size = (int) (window.window_height()/SQUARE_SIZE)
    
    painter = MarkovArtist({
        "F": {"F": 0, "C": 0.75, "E": 0.25, "B": 0, "D": 0, "A": 0, "G": 0},
        "C": {"F": 0.111, "C": 0, "E": 0.111, "B": 0, "D": 0.111, "A": 0, "G": 0.667},
        "E": {"F": 0, "C": 0, "E": 0, "B": 0.5, "D": 0, "A": 0, "G": 0.5},
        "B": {"F": 0, "C": 0.5, "E": 0, "B": 0, "D": 0.5, "A": 0, "G": 0},
        "D": {"F": 0.333, "C": 0.333, "E": 0, "B": 0, "D": 0, "A": 0.334, "G": 0},
        "A": {"F": 0, "C": 0, "E": 0.25, "B": 0, "D": 0.25, "A": 0.25, "G": 0.25},
        "G": {"F": 0, "C": 0.167, "E": 0.166, "B": 0, "D": 0.25, "A": 0.25, "G": 0.167}
    })
    painter.create_painting_scheme(grid_size * grid_size)

    paint(window, canvas, painter.patiningColors)

    window.exitonclick()


if __name__ == "__main__":
    main()

