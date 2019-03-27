import abc


class AlgorithmInterface(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def output(self): raise NotImplementedError

    @abc.abstractmethod
    def prelim_check(self): raise NotImplementedError

    @abc.abstractmethod
    def print_remaining_stocks(self, stocks): raise NotImplementedError

    @abc.abstractmethod
    def print_remaining_orders(self, orders): raise NotImplementedError




