import Parts.Background.Acolyte as Acolyte
import Parts.Background.Charlatan as Charlatan
import Parts.Background.Criminal as Criminal

import Parts.Background.Entertainer as Entertainer
import Parts.Background.FolkHero as FolkHero
import Parts.Background.GuildArtisan as GuildArtisan

import Parts.Background.Hermit as Hermit
import Parts.Background.Noble as Noble
import Parts.Background.Outlander as Outlander

import Parts.Background.Sage as Sage
import Parts.Background.Sailor as Sailor
import Parts.Background.Soldier as Soldier

import Parts.Background.Urchin as Urchin
import random as rng
### Background is in first person
### ### Should we change it to third person to match classes
### ### Should we change classes to first person

def RunBackgrounds(back):
	g = None
	if back == 'acolyte':
		g = Acolyte
	elif back == 'charlatan':
		g = Charlatan
	elif back == 'criminal':
		g = Criminal
	elif back == 'entertainer':
		g = Entertainer
	elif back == 'folk hero':
		g = FolkHero
	elif back == 'guild artisan':
		g = GuildArtisan
	elif back == 'hermit':
		g = Hermit
	elif back == 'noble':
		g = Noble
	elif back == 'outlander':
		g = Outlander
	elif back == 'sage':
		g = Sage
	elif back == 'sailor':
		g = Sailor
	elif back == 'soldier':
		g = Soldier
	elif back == 'urchin':
		g = Urchin
	return g.GetResults()

def ChooseRandom():
	roll = rng.randint(1,13)
	result = ''
	if roll == 1:
		result = 'acolyte'
	elif roll == 2:
		result = 'charlatan'
	elif roll == 3:
		result = 'criminal'
	elif roll == 4:
		result = 'entertainer'
	elif roll == 5:
		result = 'folk hero'
	elif roll == 6:
		result = 'guild artisan'
	elif roll == 7:
		result = 'hermit'
	elif roll == 8:
		result = 'noble'
	elif roll == 9:
		result = 'outlander'
	elif roll == 10:
		result = 'sage'
	elif roll == 11:
		result = 'sailor'
	elif roll == 12:
		result = 'soldier'
	elif roll == 13:
		result = 'urchin'
	#
	return result