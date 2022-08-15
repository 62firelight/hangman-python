#  Hangman Program (NO GUI AS OF YET)
from tkinter import *
from tkinter import ttk
import random

meme_words_list = ["its", "treason", "then", "this", "is", "getting", "out", "hand", "now", "there", "are", "two", "of", "them", "another", "happy", "landing", "not", "to", "worry", "we", "are", "still",
					"flying", "half", "a", "ship", "hello", "there"] # Temporary words list, a text file will be used to generate a random word

'''

		##############################################################
		##################### 				    ######################
		##############################################################

def check_guess(guess, word):
	if len(guess) == 1:
		for letter in word:
			if letter == guess:
				print("Correct letter.")
				return letter
				break
		if letter != guess:
			print("Wrong, try again.")
			return False
	elif len(guess) == len(word):
		if guess == word:
			print("Correct. Well done.")
			return guess
		else:
			print("Wrong, try again.")
			return False
	else:
		print("Wrong, try again.")
		return False
'''

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

		# Define fonts
		self.heading_font = "Helvetica 30 bold" 
		self.hidden_font = "Helvetica 30 bold"
		self.regular_text = "Helvetica 14"
		# Font choice is temporary

		# Define graphic settings
		self.colour = "black"
		self.width = 2

		# Coordinates used to draw the hangman picture, this will appear whenever the player guesses wrongly
		self.coordinates = [(3, 99, 89, 99), (3, 98, 3, 2), (4, 81, 16, 98), (4, 2, 98, 2), (51, 3, 51, 16),
					  		(42, 17, 60, 35), (51, 36, 51, 61), (52, 62, 61, 71), (50, 62, 41, 71), (39, 48, 63, 48)]
		# Total of ten coordinates, so ten guesses will be used
		
		self.guess_multiplier = 1 # Used in conjunction with guess_count to calculate how many guesses the player will have - Default: 1
		self.guess_count = int(round(len(self.coordinates) * self.guess_multiplier, 0)) # How many guesses the player has

		self.guess = StringVar()
		self.guess.set("")

		self.declare_message = StringVar() # String variable that updates whenever the player wins or loses
		self.declare_message.set("")

		self.guess_letters = StringVar() 
		self.guess_letters.set("") # Placeholder text

		self.hidden_word = StringVar()

		self.generate_word()

		self.draw_gui() # Call method to draw the GUI

	def generate_word(self):
		random_word = random.choice(meme_words_list)

		self.hidden_word_l = []

		for i in range(len(random_word)):
			self.hidden_word_l.append("_")


		self.hidden_word.set(self.hidden_word_l)

	def draw_gui(self):

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
		self.reset_button = ttk.Button(self.main_frame, text="Reset", command=self.generate_word)
		self.reset_button.grid(row=1, column=3, padx=10, pady=10, sticky="WE")

		self.title_label = ttk.Label(self.main_frame, text="Hangman", font=self.heading_font)
		self.title_label.grid(row=1, column=1, padx=10, pady=10, columnspan=2)

		self.status_label = ttk.Label(self.main_frame, textvariable=self.declare_message)
		self.status_label.grid(row=2, column=1, padx=10, pady=10, columnspan=2)

		self.letter_label = ttk.Label(self.main_frame, textvariable=self.hidden_word, font=self.hidden_font) # Placeholder text
		self.letter_label.grid(row=3, column=1, padx=30, pady=10, columnspan=2)

		self.guess_label = ttk.Label(self.main_frame, text="You have {} guesses left.".format(self.guess_count), font=self.regular_text)
		self.guess_label.grid(row=4, column=1, padx=10, pady=10, columnspan=2)
		
		self.guess_entry = ttk.Entry(self.main_frame, textvariable=self.guess)
		self.guess_entry.grid(row=5, column=1, padx=10, pady=10, sticky="WE")

		self.guess_button = ttk.Button(self.main_frame, text="Guess")
		self.guess_button.grid(row=5, column=2, padx=10, pady=10, columnspan=2, sticky="WE")

		# Guesses frame
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