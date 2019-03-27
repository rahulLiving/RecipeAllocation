class StringToValueGenerator:
    __instance = None

    def __init__(self):
        if StringToValueGenerator.__instance is None:
            self.string_to_value_mapping = {
                'two_recipes':2,
                'three_recipes':3,
                'four_recipes':4,
                'two_portions':2,
                'four_portions':4
            }
            StringToValueGenerator.__instance = self
        else:
            raise Exception('Use the class method getInstance for getting an instance')

    @staticmethod
    def get_instance():
        if StringToValueGenerator.__instance is None:
            StringToValueGenerator()
        return StringToValueGenerator.__instance



    def get_string_value(self,string_query=None):
        """
        Returns the matching value for the input query
        :param string_query:(string) Category of the recipe or size of the proportion from the data
        :return:(integer) Value corresponding to the query
        """
        try:
            value = StringToValueGenerator.__instance.string_to_value_mapping[string_query]
        except:
            raise KeyError('%s value doesnot exist in the map'%(string_query))
        return value
