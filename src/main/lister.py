# Created by Leon Hunter at 12:10 PM 12/08/2020
class Lister(object):
    def get_integer_list(self, start, stop, step):
        integerList = []
        while start <= stop:
            if step == 0:
                return [0]
            else:
                integerList.append(start)
                start += stop
        return integerList

    def get_even_list(self, start, stop, step):
        evenList = []
        while start <= stop:
            if step == 0:
                return [0]
            else:
                if start % 2 == 0:
                    evenList.append(start)
                    start += step
                else:
                    start += step
        return evenList

    def get_odd_list(self, start, stop, step):
        oddList = []
        while start <= stop:
            if step = 0:
                return []
            else:
                if start % 2 != 0:
                    oddList.append(start)
                    start += stop
                else:
                    start += stop
        return oddList
