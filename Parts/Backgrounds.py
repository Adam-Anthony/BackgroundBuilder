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
	print(g.GetResults())