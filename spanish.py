# Spanish Program 

# Functions:

# Check if input already exists 
	# if it does then deny new entry
	# if it doesn't then allow new entry





# Dictionary = SpainishDictionary.txt
import sys
import pickle

MyDictionary = {}
pkl_file = open('MyDictionary.pkl', 'r+b') 
MyDictionary = pickle.load(pkl_file)
pkl_file.close()

temp = {}

# The main menu is where the user starts and returns. 
def main_menu():
	print 'Type:\n "1" to input a new definition, \n "2" to end program, or \n "3" to save dictionary.'
	selection = raw_input(':')
	if selection == '1':
		q = get_definition_dictionary()
		MyDictionary.update(temp)
		print 'You have successfully entered a new dictionary defintion.'
		z = raw_input('Type "1" to input a new definition or "2" to return to the main menu:')
		if z == '1':
			get_definition_dictionary()
		if z == '2':
			main_menu()
		else: 
			print 'You entered something weird. We are sending you back to the main menu.'
			main_menu()
	elif selection == '2':
		return
	elif selection == '3':
		save()
	else: 
		print 'Invdalid Entry. Goodbye.'

# Save dictionary to file 
def save():
	output = open('MyDictionary.pkl', 'w+b')
	pickle.dump(MyDictionary, output)
	output.close()
	print 'Your dictionary has been saved.'
	return


# User enters new definition
def get_definition_dictionary():

	a = raw_input('Enter the American word:')
	b = raw_input('Enter the South American word:')
	temp = {a:b}
	MyDictionary.update(temp)
	return MyDictionary

main_menu()

print MyDictionary

