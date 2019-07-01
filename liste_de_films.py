continuer = 'o'
liste_de_films = []


while continuer == 'o':
	film_a_ajouter = raw_input('Entrer le titre du film :')
	
	liste_minuscule = [film[0].lower() for film in liste_de_films]
	film_minuscule = film_a_ajouter.lower()

	if film_minuscule  in liste_minuscule:
		print('{0} est deja present dans la base'.format(film_a_ajouter))
	else:
		note = raw_input('Entrer une note sur 5 pour ce film :')
		liste_de_films.append((film_a_ajouter,note))
	
	continuer = raw_input('Voulez-vous ajouter un autre film ? o/n :')
	print('-----------------------------------------------')


liste_de_films.sort()
print(liste_de_films)



class Maclasse(object):
	"""docstring for Maclasse"""
	def __init__(self, arg):
		super(Maclasse, self).__init__()
		self.arg = arg
		
