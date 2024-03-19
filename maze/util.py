# -------------------------------------------------
# DON'T CHANGE THIS FILE.
# Utility classes and methods.
#
# __author__ = 'Jeffrey Chan'
# __copyright__ = 'Copyright 2024, RMIT University'
# -------------------------------------------------



class Coordinates:
    """
    Forward declaration.
    """
    def getRow(self)->int:
        pass

    def getCol(self)->int:
        pass


class Coordinates:
    """
    Represent coordinates for maze cells.
    """

    def __init__(self, row:int, col:int):
        """
        Constructor.
        
        @param row: Row of coordinates.
        @param col: Column of coordinates.
        """

        self.m_r = row
        self.m_c = col



    def getRow(self)->int:
        """
        @returns Row of coordinate.
        """
        return self.m_r
    


    def getCol(self)->int:
        """
        @returns Column of coordinate.
        """
        return self.m_c
    


    def isAdjacent(self, other:Coordinates)->bool:
        """
        Determine if two coordinates are adjacent to each other.
        """
        if (abs(self.m_r - other.getRow()) == 1 and self.m_c == other.getCol()) or\
                (self.m_r == other.getRow() and abs(self.m_c - other.getCol()) == 1): 
            return True
        else:
            return False
        


    def __eq__(self, other:Coordinates):
        """
        Define == operator.

        @param other: Other coordinates that we are comparing with.
        """
        if other != None:
            return self.m_r == other.getRow() and self.m_c == other.getCol()
        else:
            return False



    def __hash__(self):
        """
        Returns has value of Coordinates.  Needed for being a key in dictionaries.
        """
        return hash(str(self.m_r)+'|'+str(self.m_c))
        
        
    


