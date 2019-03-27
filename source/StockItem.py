

class StockItem:
    def __init__(self, name=None,portions=None):
        """
        :param name:(string) Name of the recipe in the stock
        :param portions:(integer) Number of portions in the stock
        """
        try:
            self.__name = str(name)
            self.__portions = int(portions)
        except Exception as e:
            raise ValueError('Arguments not recognized or missing',e)

    def reduce_portions(self,reduce_by):
        """
        :param reduce_by:(integer) Update the portions of the recipe by reducing it by the portions served
        :return: None
        """
        if self.portions - reduce_by < 0:
            raise ValueError('Amount of the recipe %s in stock is not sufficient. Available %d'%(self.name,self.portions))
        self.portions = self.portions - reduce_by

    @property
    def name(self):
        return self.__name

    @property
    def portions(self):
        return self.__portions

    @portions.setter
    def portions(self,new_portions):
        self.__portions = new_portions

    def __repr__(self):
        return "<StockItem Name:%s Portions:%d>" % (self.name, self.portions)


    def __str__(self):
        return "Name:%s Portions:%d" % (self.name, self.portions)

    def __lt__(self, other):
        return self.portions  < other.portions

    def __eq__(self, other):
        return self.portions == other.portions

    def __gt__(self, other):
        return self.portions > other.portions