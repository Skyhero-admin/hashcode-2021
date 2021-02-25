#!/bin/python3

def main():
    print(parse_file("inputs/a.txt"))
    duration, nb_intersec, streets, cars = parse_file("inputs/a.txt")


def parse_file(path):
    with open(path, "r") as f:
        # First line
        counts = f.readline().split(" ")
        duration = int(counts[0])
        nb_intersec = int(counts[1])
        nb_streets = int(counts[2])
        nb_cars = int(counts[3])
        bonus_score = int(counts[4])

        # Streets
        streets = dict()
        for i in range(nb_streets):
            street = f.readline().split(" ")
            origin = int(street[0])
            dest = int(street[1])
            if origin not in streets:
                streets[origin] = dict()
            streets[origin][dest] = (street[2], int(street[3]))

        # Cars
        cars = []
        for i in range(nb_cars):
            car = f.readline().split(" ")
            cars.append(car[1:])

        return duration, nb_intersec, streets, cars

main()