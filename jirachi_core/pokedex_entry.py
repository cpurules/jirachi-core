class PokedexEntry:
    def __init__(self, id, seen, caught):
        self.id = id
        self.seen = seen
        self.caught = caught
    
    def __eq__(self, obj):
        return (isinstance(obj, PokedexEntry) and
                self.id == obj.id and
                self.seen == obj.seen and
                self.caught == obj.caught)
    
    def __str__(self):
        return "{0},{1},{2}".format(self.id, self.seen, self.caught)