

# classe list surchargée avec des fonctions plus parlante
class overlist(list):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    # renvoie le dernier élément de la liste
    @property
    def last(self):
        return self[-1]
