from utility.StringToValueGenerator import StringToValueGenerator


class Order:
    def __init__(self, number_of_recipes=None, number_of_portions=None, order_count=None):
        try:
            self.__number_of_recipes = StringToValueGenerator.get_instance().get_string_value(str(number_of_recipes))
            self.__number_of_portions = StringToValueGenerator.get_instance().get_string_value(str(number_of_portions))
            self.__order_count = int(order_count)
        except Exception as e:
            raise Exception(e)


    @property
    def number_of_recipes(self):
        return self.__number_of_recipes

    @property
    def number_of_portions(self):
        return self.__number_of_portions

    @property
    def order_count(self):
        return self.__order_count

    @order_count.setter
    def order_count(self, new_count=0):
        self.__order_count = new_count

    def reduce_order_count(self,reduce_by=0):
        if self.order_count - reduce_by < 0:
            raise ArithmeticError('Value of ordered count cannot be negative')
        self.order_count = self.__order_count - reduce_by

    def __repr__(self):
        return "<Order Recipes:%d Portions:%d Count:%d>" % (self.number_of_recipes, self.number_of_portions, self.order_count)


    def __str__(self):
        return "Recipes:%d Portions:%d Count:%d" % (self.number_of_recipes, self.number_of_portions, self.order_count)

    def __lt__(self, other):
        return self.order_count * self.number_of_portions < other.order_count * other.number_of_portions

    def __eq__(self, other):
        return self.order_count * self.number_of_portions == other.order_count * other.number_of_portions

    def __gt__(self, other):
        return self.order_count * self.number_of_portions > other.order_count * other.number_of_portions