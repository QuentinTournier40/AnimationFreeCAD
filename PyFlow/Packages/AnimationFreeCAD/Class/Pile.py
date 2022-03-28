class Pile:

	def __init__(self):
		self.valeurs = []

	def empiler(self, valeur):
		self.valeurs.append(valeur)

	def depiler(self):
		if self.valeurs:
			return self.valeurs.pop()

	def estVide(self):
		if(len(self.valeurs)==0):
			return True
		else:
			return False

	def lireSommet(self):
		return self.valeurs[-1]		#retourne la dernière valeur du tableau