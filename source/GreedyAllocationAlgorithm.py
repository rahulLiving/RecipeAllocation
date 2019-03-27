from source.AlgorithmInterface import AlgorithmInterface
import heapq
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class GreedyAllocationAlgorithm(AlgorithmInterface):

    def __init__(self, orders=None, stocks=None):
        if orders == None or stocks == None:
            raise ValueError('Stocks or Orders cannot be empty!')
        self.__orders = orders
        self.__stocks = stocks

    def prelim_check(self):
        total_orders = 0
        for order in self.__orders:
            total_orders += order.order_count

        total_stock = 0
        for stock in self.__stocks:
            total_stock += stock.portions

        return total_orders > total_stock

    def print_remaining_stocks(self, stocks):
        logger.debug('---Remaining Stocks---')
        while stocks:
            stock = stocks.pop()
            logger.debug(stock)
        logger.debug('---xxx---')

    def print_remaining_orders(self, orders):
        logger.debug('---Remaining Orders---')
        while orders:
            order = orders.pop()
            logger.debug(order)
        logger.debug('---xxx---')


    def output(self):
        if not self.prelim_check():
            return False

        orders_max_pq = heapq._heapify_max(self.__orders)
        stocks_max_pq = heapq._heapify_max(self.__stocks)

        try:
            while orders_max_pq:
                order = orders_max_pq.pop()
                recipes = []
                for i in range(order.number_of_recipes):
                    recipe_in_stock = stocks_max_pq.pop()
                    recipes.append(recipe_in_stock.reduce_portions(order.number_of_portions))
                order.reduce_order_count(1)
                for recipe in recipes:
                    stocks_max_pq.push(recipe)
                if order.order_count > 0:
                    stocks_max_pq.push(order)

        except Exception as e:
            logger.debug(e)
            self.print_remaining_stocks(stocks_max_pq)
            self.print_remaining_orders(orders_max_pq)
            return False

        self.print_remaining_stocks(stocks_max_pq)
        self.print_remaining_orders(orders_max_pq)
        return True