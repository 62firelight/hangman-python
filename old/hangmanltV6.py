# Hangman Program
# Importing modules for use in program 
from tkinter import *
from tkinter import ttk
import random

meme_words_list = ["happy"] # Temporary words list, a text file will be used to generate a random word

'''

		##############################################################
		##################### 				    ######################
		############################################################## '''

class HangmanGUI: # Defining class
	def __init__(self, master): # Constructor class, always uses root as argument
								# Used mainly for variable defining
								# This always runs when an instance of this class is created
		self.master = master # Variable defining
		self.master.title("Hangman Program") # Set the title of the program

		##############################################################
		##################### VARIABLE DEFINING ######################
		##############################################################
		# Note the self. prefix, which is used so that the variables that are defined here can be used in other methods

		# Define fonts in a specific format
		self.heading_font = "Helvetica 30 bold"  # Used for the heading
		self.hidden_font = "Helvetica 30 bold" # Used for the hidden/revealed letters
		self.regular_text = "Helvetica 11" 
		# Font choice is temporary for now

		# Define graphic settings for hangman canvas
		self.colour = "black" # Colour of line
		self.width = 2 # Line width of line

		# Define game settings, some parameters are set as variables for added flexibility to the program
		self.hidden_letter = "_" 

		# Coordinates used to draw the hangman picture, this will appear whenever the player guesses wrongly
		self.coordinates = [(3, 99, 89, 99), (3, 98, 3, 2), (4, 81, 16, 98), (4, 2, 98, 2), (51, 3, 51, 16),
					  		(42, 17, 60, 35), (51, 36, 51, 61), (52, 62, 61, 71), (50, 62, 41, 71), (39, 48, 63, 48)]
		# Total of ten coordinates, so ten guesses will be used
		# Amount of guesses depends on how many coordinates for the hangman picture there are -- allows for more flexibility
		
		self.guess_multiplier = 1 # Used in conjunction with guess_count to calculate how many guesses the player will have - Default: 1
		self.guess_count = int(round(len(self.coordinates) * self.guess_multiplier, 0)) # How many guesses the player has

		self.guess = StringVar() # Define a guess variable that will be used to get the player's input
		self.guess.set("")

		self.declare_message = StringVar() # Define a string variable that updates whenever the player wins or loses
		self.declare_message.set("") # This will always be set to "" when the game is in progress

		self.guess_letters_list = [] # Empty list

		self.guess_letters = StringVar() 
		self.guess_letters.set("") # Placeholder text

		self.hidden_word = StringVar() # Define a hidden word variable that will be used throughout the entirety of the class

		# Calling methods to initialize the game
		self.generate_word() # Generate a word before the method to start the game is called -- otherwise the game breaks
		self.draw_gui() # Draw the GUI

	def generate_word(self): # Method for generating a random word
							 # Does not take any parameters
		self.random_word = random.choice(meme_words_list) # Random word is defined within the method so a parameter is not needed

		self.hidden_word_l = [] # Create an empty list so that things can be appended onto it later
								# Controls how many hidden letters should be added

		for i in range(len(self.random_word)): 
			self.hidden_word_l.append(self.hidden_letter) # Append the list with whatever the hidden letter is

		self.hidden_word.set(self.hidden_word_l) # Set this equal to the hhidden_letter 

	def check_word(self, guess): # Method to check the player's input
								 # Take the player's input as a parameter, so that I don't have to type out a self. prefix every time
								 # I want to use the player's input
		# print(self.guess.get()) # Debug message
		if self.declare_message.get() == "": # Check if the game is still in progress
			if guess.isalpha() == True: # Check if the player's input only uses letters
										# This method will return false whenever the player types nothing or a character that is not a letter

				# Correct conditon checks
				if guess == self.random_word: # If the player guesses the whole word
					self.hidden_word.set(guess)
				else:
					for letter in self.random_word:
						if guess == letter: # If the player guesses a letter
							self.hidden_word_l[self.random_word.index(letter)] = guess 
							self.hidden_word.set(self.hidden_word_l)
				# Wrong condition checks
						elif letter == self.random_word[-1]: # If the player's guess is not correct and the loop reaches the last letter
							self.guess_count -= 1
							self.guess_letters_list.append(guess.upper())
							self.guess_letters.set(self.guess_letters_list)
							
				if len(guess) > 1 and len(guess) < len(self.random_word) or len(guess) > len(self.random_word):
					self.guess_count -= 1
					print("Wrong word")
			elif guess == "": # If the player's input is nothing
				print("Enter a letter or a word.")
			else: # If the player's input has any amount of other characters
				print("Give a letter or a word. Numbers and other characters are not allowed.")
			self.guess.set("") # Reset entry field no matter what, so the player doesn't have to delete their input every time they guess
			
		else: # Otherwise the player has won or lost
			pass # Do nothing

	def draw_gui(self): # Method to generate the GUI
						# Where most of the widgets in the program are stored

		##############################################################
		##################### 	 DRAWING GUI	######################
		##############################################################

		# Coordinates used to draw the hangman's face, but this will only appear if the player loses the game

		# Creating widgets for the program
		# The ttk. prefix is used to ensure that the widget's appearance remains appropriate depending on the operating system, makes the program look more modern'

		# Main container frame
		self.main_frame = ttk.LabelFrame(self.master, text="Main Window") # Placeholder text
		self.main_frame.grid(row=1, column=1, padx=10, pady=10, columnspan=2, sticky="NSEW") # The grid function is used to organize the frames

		# Labels are named differently just so I can keep track of them more easily
		self.reset_button = ttk.Button(self.main_frame, text="Reset", command=self.generate_word) # Button to reset the game by generating a new word
		self.reset_button.grid(row=1, column=3, padx=10, pady=10, sticky="WE")

		self.title_label = ttk.Label(self.main_frame, text="Hangman", font=self.heading_font) # Heading label
		self.title_label.grid(row=1, column=1, padx=10, pady=10, columnspan=2)

		self.status_label = ttk.Label(self.main_frame, textvariable=self.declare_message) # "Declaration" message to tell the player if they have won or lost
		self.status_label.grid(row=2, column=1, padx=10, pady=10, columnspan=2)

		self.letter_label = ttk.Label(self.main_frame, textvariable=self.hidden_word, font=self.hidden_font) # Placeholder text
		self.letter_label.grid(row=3, column=1, padx=30, pady=10, columnspan=2)

		self.guess_label = ttk.Label(self.main_frame, text="You have {} guesses left.".format(self.guess_count), font=self.regular_text) # Label to tell the player how 
																																		 # many guesses they have
		self.guess_label.grid(row=4, column=1, padx=10, pady=10, columnspan=2)
		
		self.guess_entry = ttk.Entry(self.main_frame, textvariable=self.guess) # Entry that takes the player's input
		self.guess_entry.grid(row=5, column=1, padx=10, pady=10, sticky="WE")

		self.guess_button = ttk.Button(self.main_frame, text="Guess", command=lambda : self.check_word(self.guess.get()))
																	  # Button that when pushed, checks the player's input and evaluate to see if it is correct or wrong
																	  # Should clear the entry widget as well so the player doesn't have to delete their input before 
																	  # entering in another one
																	  # Lambda is just here so that the program is able to pass a parameter into the check word method
		self.guess_button.grid(row=5, column=2, padx=10, pady=10, columnspan=2, sticky="WE")

		self.master.bind('<Return>', lambda x: self.check_word(self.guess.get())) # Bind the enter key to the guess button, so that they can push Enter instead of having
																				  # to click the guess button every time they wanted to guess

		# Guesses frame
		# Wrong guesses go in here
		self.guess_frame = ttk.LabelFrame(self.master, text="Previous Guesses") 
		self.guess_frame.grid(row=6, column=1, padx=10, pady=10, sticky="NSEW")

		self.guess_letters_label = ttk.Label(self.guess_frame, textvariable=self.guess_letters) # Placeholder code
		self.guess_letters_label.grid(row=6, column=1)

		# Picture frame
		self.picture_frame = ttk.LabelFrame(self.master, text="Picture") # Placeholder text
		self.picture_frame.grid(row=6, column=2, padx=10, pady=10, sticky="NSEW")

		self.picture_canvas = Canvas(self.picture_frame, width=100, height=100) # No ttk. prefix because there is none for a Canvas widget 
		self.picture_canvas.grid(row=6, column=1)

		for line in self.coordinates:
			if self.coordinates.index(line) == 5:
				self.picture_canvas.create_oval(self.coordinates[5], fill=self.colour, width=self.width)
			else:
				self.picture_canvas.create_line(self.coordinates, fill=self.colour, width=self.width)

'''
		guess_count = 5
		word = random.choice(meme_words_list)

		

		while guess_count > 0:
			hidden_word = 
			word_display = "The word is {}. You have {} guess(es) left.".format(hidden_word, guess_count)
			guess = input("Guess a letter or a word\n")
			if check_guess(guess, word) == False:
				guess_count -= 1
			elif check_guess(guess, word) == :
'''

root = Tk()
Hangman = HangmanGUI(root)
root.mainloop()