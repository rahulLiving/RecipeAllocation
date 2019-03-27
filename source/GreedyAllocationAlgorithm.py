from source.AlgorithmInterface import AlgorithmInterface
import heapq
from heapq import heappush, heappop
import logging
logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)

class GreedyAllocationAlgorithm(AlgorithmInterface):

    def __init__(self, orders=None, stocks=None):
        if orders == None or stocks == None:
            raise ValueError('Stocks or Orders cannot be empty!')
        self.orders = orders
        self.stocks = stocks

    def prelim_check(self):
        total_orders = 0
        for order in self.orders:
            total_orders += order.order_count

        total_stock = 0
        for stock in self.stocks:
            total_stock += stock.portions

        return total_orders < total_stock

    def print_remaining_stocks(self, stocks):
        logger.info('---Remaining Stocks---')
        while stocks:
            stock = stocks.pop()
            logger.info(stock)
        logger.info('---xxx---')

    def print_remaining_orders(self, orders):
        logger.info('---Remaining Orders---')
        while orders:
            order = orders.pop()
            logger.info(order)
        logger.info('---xxx---')


    def output(self):
        if not self.prelim_check():
            return False


        orders_max_pq = self.orders
        stocks_max_pq = self.stocks

        heapq.heapify(orders_max_pq)
        heapq.heapify(stocks_max_pq)

        try:
            while orders_max_pq:
                order = heappop(orders_max_pq)
                recipes = []
                for i in range(order.number_of_recipes):
                    recipe_in_stock = heappop(stocks_max_pq)
                    recipe_in_stock.reduce_portions(order.number_of_portions)
                    recipes.append(recipe_in_stock)
                order.reduce_order_count(1)
                for recipe in recipes:
                    heappush(stocks_max_pq,recipe)
                if order.order_count > 0:
                    heappush(orders_max_pq,order)

        except Exception as e:
            logger.debug(e)
            self.print_remaining_stocks(stocks_max_pq)
            self.print_remaining_orders(orders_max_pq)
            return False

        self.print_remaining_stocks(stocks_max_pq)
        self.print_remaining_orders(orders_max_pq)
        return True