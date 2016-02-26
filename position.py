
class Position(tuple):
    ''' A tuple representing a position
            that supports some vector
            operations
    '''

    def __add__(self,other):
        return Position(v + w for v,w in zip(self,other))

    def __radd__(self,other):
        return Position(w+v for v,w in zip(self,other))

    def __sub__(self,other):
        return Position(v - w for v,w in zip(self,other))

    def __rsub__(self,other):
        return Position(w - v for v,w in zip(self,other))

    def __mul__(self,other):
        return Position(v * other for v in self)

    def __rmul__(self, other):
        return Position(v * other for v in self)

    def __neg__(self):
        return -1*self
