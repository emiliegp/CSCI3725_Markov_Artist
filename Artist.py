"""
    Emilie Grand'Pierre 
    Computational Creativity (CSCI 3725)
    M3: A Markov Destinction 
    9/15/2022

    In this model, music notes in my three favorties songs are used to create a patchworked masterpiece using the Turtle package. 
    The transition matrix is defined by my top songs of 2022: "Show Me" by James Blake, "Phoenix" by 
    ASAP Rocky, and "Comfortably Numb" by Pink Floyd. I simplified the notes to exclude the sharps and flats; if the
    song includes a particular note, then it is considered in the transition matrix.
    Notes are then mapped to specific colors: 
        F --> green
        C --> red
        E --> orange
        B --> pink
        D --> grey
        A --> purple
        G --> blue 
"""

import turtle
import numpy as np

TURTLE_SIZE =20
SQUARE_SIZE = 20

class MarkovArtist:
    def __init__(self, transition_matrix):
        """
            Simulates an artist that relies on a simple Markov chain to form the color scheme of 
            a patchwork quilt.

            :param transitionMatrix: (list) transition prob. 
        """
        self.transition_matrix = transition_matrix
        self.strokes = list(transition_matrix.keys())
        self.patining_colors = []

    def get_next_stroke(self, current_stroke):
        """
            Decide which note, and therefore color, comes next in the color scheme of the quilt
            
            :param current_stroke: (str) the current note (i.e. color) in the scheme
            :return: (str) next stroke based on the MarkovArtist transitionMatrix
        """
        return np.random.choice(
            self.strokes,
            p=[self.transition_matrix[current_stroke][next_stroke] for next_stroke in self.strokes]
        )
        

    def create_painting_scheme(self, num_strokes, current_note="A"):
        """
            Generate a sequence of notes (i.e. colors) of the quilt's color scheme & updates paintingColors

            :param current_note: (str) note of song we are currently looking at
            :param num_strokes: (int) number of squares within the quilt (i.e. the # of notes/colors
                                        needed in the color scheme)
            
        """
        painting = []
        while len(painting) < num_strokes:
            next_stroke = self.get_next_stroke(current_note)
            painting.append(next_stroke)
            current_note = next_stroke

        #Call helper method to map notes to color and define quilt's color scheme
        self.note_to_color(painting)


    def note_to_color(self, matrix):
        """
            A helper method that maps notes to specific colors and updates painting_colors

            :param matrix: the list of notes determined by the transition matrix
        """
        for note in matrix:
            if note == "F":
                self.patining_colors.append("Green")
            elif note == "C":
                self.patining_colors.append("Red")
            elif note == "E":
                self.patining_colors.append("Green")
            elif note == "B":
                self.patining_colors.append("Pink")
            elif note == "D":
                self.patining_colors.append("Grey")
            elif note == "A":
                self.patining_colors.append("Purple")
            elif note == "G":
                self.patining_colors.append("Blue")

def paint(screen, turtle, matrix):
    """
        Generates a 2D quilt (i.e. grid) using the Turtle library and the color scheme
        developed by the MarkovArtist. 

        :param screen, turtle: objects defined by the Turtle library
        :param colorScheme: (list) order of colors for the pathces (squares) in the quilt (grid)
    """
    #Determine how many patches (squares) are needed in the quilt (grid)
    grid_size = (int) (screen.window_height()/SQUARE_SIZE)
    square_counter = 0

    #Creating each row of the quilt
    for x in range(grid_size):
        #Building out each column of the quilt
        for y in range(grid_size):
            turtle.begin_fill()
            square(turtle)
            turtle.color(matrix[square_counter])
            turtle.end_fill()
            turtle.color("Black")
            #move to the next patch 
            square_counter = square_counter + 1
            turtle.forward(SQUARE_SIZE)
        turtle.backward(SQUARE_SIZE * grid_size)
        turtle.right(90)
        turtle.forward(SQUARE_SIZE)
        turtle.left(90)

def square(turtle):
    """
        A helper method to paint which generates a squares, or patches
        within the quilt (i.e. grid)
    """
    for x in range(4):
        turtle.forward(SQUARE_SIZE)
        turtle.right(90)

def main():
    """
        Main method that uses a MarkovArtist object and the Turtle library to 
        create a 2D quilt whith a color scheme based on a transition matrix 
        defined by the order of notes found in the following songs: "Show Me" by James 
        Blake, "Pheonix" by ASAP Rocky, and "Comfortably Numb" by Pink Floyd. 
    """
    #Build a background for the 2D quilt and a turtle object
    window = turtle.Screen()
    window.screensize(canvwidth=(SQUARE_SIZE), canvheight=(SQUARE_SIZE))
    window.bgcolor("White")
    
    #Move turtle to top left corner of the screen
    canvas = turtle.Turtle()
    canvas.speed(10)
    canvas.penup()
    canvas.goto(TURTLE_SIZE/2 - window.window_width()/2, window.window_height()/2 - TURTLE_SIZE/2)
    canvas.pendown()

    #Determine how many patches (squares) are needed in the quilt (grid)
    quilt_size = (int) (window.window_height()/SQUARE_SIZE)
    
    #Create a MarkovArtist object whose transition matrix is defined by the occurance of notes
    painter = MarkovArtist({
        "F": {"F": 0, "C": 0.75, "E": 0.25, "B": 0, "D": 0, "A": 0, "G": 0},
        "C": {"F": 0.111, "C": 0, "E": 0.111, "B": 0, "D": 0.111, "A": 0, "G": 0.667},
        "E": {"F": 0, "C": 0, "E": 0, "B": 0.5, "D": 0, "A": 0, "G": 0.5},
        "B": {"F": 0, "C": 0.5, "E": 0, "B": 0, "D": 0.5, "A": 0, "G": 0},
        "D": {"F": 0.333, "C": 0.333, "E": 0, "B": 0, "D": 0, "A": 0.334, "G": 0},
        "A": {"F": 0, "C": 0, "E": 0.25, "B": 0, "D": 0.25, "A": 0.25, "G": 0.25},
        "G": {"F": 0, "C": 0.167, "E": 0.166, "B": 0, "D": 0.25, "A": 0.25, "G": 0.167}
    })
    #Create a color scheme for the quilt
    painter.create_painting_scheme(quilt_size * quilt_size)

    #Create the 2D quilt
    paint(window, canvas, painter.patining_colors)

    window.exitonclick()


if __name__ == "__main__":
    main()

