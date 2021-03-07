MESSAGE = "Hello Grandpy ! How was your evening with Grandma yesterday? \
			By the way, as i am here, can you tell where is the museum of Art and History of Fribourg please? \
			My deer salutations."

GOOGLE_API_RETURN = "Route de Morat 12, 1700 Fribourg, Suisse", 46.8077191, 7.159642

WIKI_API_RETURN = "The Musée d'art et d'histoire is a museum of art and history in the town of Fribourg in Switzerland, founded in 1774 by Tobie Gerfer.", \
					"https://en.wikipedia.org/wiki/Mus%C3%A9e_d%27art_et_d%27histoire_(Fribourg)"	

RESPONSE_RETURN_OK = {
	'status' : 'ok',
	'address' : "Route de Morat 12, 1700 Fribourg, Suisse",
	'latitude' : 46.8077191,
	'longitude' : 7.159642,
	'anecdote' : "The Musée d'art et d'histoire is a museum of art and history in the town of Fribourg in Switzerland, founded in 1774 by Tobie Gerfer.", 
	'url': "https://en.wikipedia.org/wiki/Mus%C3%A9e_d%27art_et_d%27histoire_(Fribourg)"}


RESPONSE_RETURN_NOK = {'status' : 'nok'}