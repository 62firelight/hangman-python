#  Hangman Program (NO GUI AS OF YET)
from tkinter import *
from tkinter import ttk
import random

meme_words_list = ["its", "treason", "then", "this", "is", "getting", "out", "hand", "now", "there", "are", "two", "of", "them", "another", "happy", "landing", "not", "to", "worry", "we", "are", "still",
					"flying", "half", "a", "ship", "hello", "there"] # Temporary words list

'''

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
		self.master = master # Variable defining
		self.master.title("Hangman Program") # Set the title of the program

		# Define fonts
		heading_font = "Helvetica 30 bold" 
		hidden_font = "Helvetica 30 bold"
		regular_text = "Helvetica 14"

		guess_count = 5
		self.guess = StringVar()
		self.guess.set("")

		self.message = StringVar()
		self.message.set("")

		# Creating widgets for the program
		self.main_frame = ttk.LabelFrame(self.master, text="Main Window")
		self.main_frame.grid(row=1, column=1, padx=10, pady=10, sticky="NSEW")

		# Labels are named differently just so I can keep track of them more easily
		self.title_label = ttk.Label(self.main_frame, text="Hangman", font=heading_font)
		self.title_label.grid(row=1, column=1, padx=10, pady=10, sticky="WE")

		self.status_label = ttk.Label(self.main_frame, textvariable=self.message)
		self.status_label.grid(row=2, column=1, padx=10, pady=10, sticky="WE")

		# Placeholder for now
		self.letter_label = ttk.Label(self.main_frame, text="_ _ _ _ _ _ _ _ _ _ _ _ _", font=hidden_font)
		self.letter_label.grid(row=3, column=1, padx=10, pady=10, sticky="WE")

		self.guess_label = ttk.Label(self.main_frame, text="You have {} guesses left.".format(guess_count))
		self.guess_label.grid(row=4, column=1, padx=10, pady=10, sticky="WE")
		
		self.guess_entry = ttk.Entry(self.main_frame, textvariable=self.guess)
		self.guess_entry.grid(row=5, column=1, padx=10, pady=10, sticky="WE")

		self.guess_button = ttk.Button(self.main_frame, text="Guess")
		self.guess_button.grid(row=5, column=2, padx=10, pady=10, sticky="WE")

		self.guess_frame = ttk.LabelFrame(self.master, text="Previous Guesses")
		self.guess_frame.grid(row=6, column=1, padx=10, pady=10, sticky="NSEW")



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