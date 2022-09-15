# CSCI3725_Markov_Artist
Emilie Grand'Pierre

M3: A Markov Distinction 
Project Instructions: Use a Markov chain to create a piece of visual art that is meaningful. 

As I was setting up my dorm room, I noticed how the quilt I have carried wiht me throughout my time at Bowdoin does not match well with my multi-colored rug. There is not much of a pattern to the rug, but I love my bedspread to be mainly geometric: I have striped sheets and a white comforter with quilted squares. When given this project, I thought it would be great to design a quilt that would bring more cohesion to this room while also incorperating some of the music posters in my room.

In this model, music notes from my three favorties songs--Show Me" by James Blake, "Phoenix" by ASAP Rocky, and "Comfortably Numb" by Pink Floyd--are used to define a transition matrix that determines the next note to create a patchworked masterpiece using the Turtle library. I skipped Intro to CS, so I have not coded in Python for about 3 years and have never used the Turtle library, so this project was a great way to get reacquainted with Python and use a nifty drawing library. Using the in-class MarkovMusician as a guide, this project pushed me to express computational models through graphics: a first! Furthermore, the open-ended nature of the prompt forced me to adopt an open-minded perspective when interacting with code in an educational, academic, and creative sense. Overall, my Markov Artist reinforced MDPs by addressing a problem wildly different than GridWorld or other, more rigid instances where I have encountered fundamental AI priciples. In sum, it connected Computer Science to my broader experience at Bowdoin and knowledge-base. 



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

The result is a 2D model of a mutli-colored quilt that if created would bring such vibrance to my dorm room during the Maine winter! Going forward, it would be interesting to make the transiton matrix a dynamic model that takes input from the user so that the color scheme of the rug can change based on the songs entered. By considering more complex musical componenets, the model could also incorperate patterns and shades to the quilt design. Additionally, it would be interesting to experiment with other drawing libraries to add things like texture to the 2D model.



**How to use & is it Creative?**

To use, simple download the repositiory and run the Artist.py file. If you would like to create smaller or larger pathes in your quilt simply update the Global variable SQUARE_SIZE: inputting a SQUARE_SIZE of 300 leads to only 4 squares being created. 

WHen considering if this mdoel is creative, I turned to Maragret Boden's definitions of creaitivty. This model is certainly not H-creative, but could be argued to be P-creative and combinational. Each quilt model produced by the MarkovArtist is unique, yet it depends on familiar ideas stored in the Turtle library, definined in the 'square' method, and Markov chains. For both the AI system, and for myself, something new was created. 
