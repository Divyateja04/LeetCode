import heapq
from collections import defaultdict
class MovieRentingSystem(object):

    def __init__(self, n, entries):
        self.dir = {}
        self.log = SortedSet(key=lambda x: (x[0], x[1], x[2]))
        self.rented = {}

        for shop, movie, price in entries:
            if movie not in self.dir:
                self.dir[movie] = SortedSet(key=lambda x: (x[0], x[1]))
            self.dir[movie].add((price, shop, movie))
            self.rented[self.encode(shop, movie)] = [price, False]

    def encode(self, shop, movie) :
        return (shop << 20) | movie
    def search(self, movie):
        if movie not in self.dir:
            return []
        result = []
        for price, shop, mov in self.dir[movie]:
            if len(result) == 5:
                break
            if not self.rented[self.encode(shop, mov)][1]:
                result.append(shop)
        return result

    def rent(self, shop, movie):
        key = self.encode(shop, movie)
        self.rented[key][1] = True
        price = self.rented[key][0]
        self.log.add((price, shop, movie))

    def drop(self, shop, movie):
        key = self.encode(shop, movie)
        self.rented[key][1] = False
        price = self.rented[key][0]
        self.log.remove((price, shop, movie))

    def report(self):
        result = []
        for price, shop, movie in self.log:
            if len(result) == 5:
                break
            result.append([shop, movie])
        return result