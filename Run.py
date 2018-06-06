#import sys
#sys.path.append('./Parts/')
import Main
import Parts.Backgrounds as Backgrounds
import Parts.CharClass as CharClass
import Parts.Race as Race
print('Enter the information about your character.')
print('Just press enter on any information you want generated.')
print(' ?  for list of options')

breaker = True
while breaker:
	race = input('Race: ')
	if race == '?':
		Race.PrintOptions()
	elif Race.CheckInput(race) or race == '':
		breaker = False
	else:
		print('Input not accepted. Type ? for help with options.')

breaker = True 
while breaker:
	clas = input('Class: ')
	if clas == '?':
		CharClass.PrintOptions()
	elif CharClass.CheckInput(clas) or clas == '':
		breaker = False
	else:
		print('Input not accepted. Type ? for help with options.')

breaker = True
while breaker:		
	back = input('Background: ')
	if back == '?':
		Backgrounds.PrintOptions()
	elif Backgrounds.CheckInput(back) or back == '':
		breaker = False
	else:
		print('Input not accepted. Type ? for help with options.')

breaker = True
while breaker:
	chaMod = input('Charisma Mod: ')
	if chaMod == '?':
		print('Your charisma modifier from your character\'s stats.')
		print('Leave blank if you don\'t have that information.')
	else:
		breaker = False
Main.CharBuild().BuildGiven(race, clas, back, chaMod)