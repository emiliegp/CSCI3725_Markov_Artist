# CSCI3725_Markov_Artist
Emilie Grand'Pierre
M3: A Markov Distinction 
Project Instructions: Use a Markov chain to create a piece of visual art that is meaningful. 

As I was setting up my dorm room, I noticed how the quilt I have carried wiht me throughout my time at Bowdoin does not match well with my multi-colored rug. There is not much of a pattern to the rug, but I love my bedspread to be mainly geomatric: I have striped sheets and a white comforter with quilted squares. When given this project, I thought it would be great to design a quilt that would bring more cohesion to this room while also incorperating some of the music posters in my room.

In this model, music notes from my three favorties songs--Show Me" by James Blake, "Phoenix" by ASAP Rocky, and "Comfortably Numb" by Pink Floyd--are used to define a transition matrix that determines the next note to create a patchworked masterpiece using the Turtle library. I skipped Intro to CS, so I have not coded in Python for about 2 years and have never used the Turtle library, so this project was a great way to get reacquainted with Python and use a nifty drawing library. 

**Building the Transition Matrix and Mapping Notes to Colors**
To begin, I compiled a list of piano notes for the three songs, taking note of the order in which the notes appeared. If the song includes a particular note, then it is considered in the transition matrix. For example, in "Show Me," a F is followed by a C or E, but in "Pheonix" a F is always followed by a C. It follows then that in the transition matrix, if the note is C, the following note will be F with a probablity of .75 or an E with a probability of .25. This logic was followed for all notes in the key. 

I simplified the notes to exclude the sharps and flats. 

The particular notes in the song went on to be mapped to colors
Notes are then mapped to specific colors: 
    F --> green
    C --> red
    E --> orange
    B --> pink
    D --> grey
    A --> purple
    G --> blue 

The result is a 2D model of a mutli-colored quilt that if created would bring such vibrance to my room during the Maine winter! Going forward, it would be inetresting to make the transiton matrix a dynamic model that takes input from the user so that the color scheme of the rug can change based on the songs entered. Additionally, it would be interesting to experiment with other drawing libraries to add things like texture to the 2D model
