import csv
import sys

def read_rides_as_tuples(filename):
    '''
    Read the bus ride data as a list of tuples
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = (route, date, daytype, rides)
            records.append(record)
    return records

def read_rides_as_dicts(filename):
    '''
    Read the bus ride data as a list of dicts
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = {
                route: route,
                date: date,
                daytype: daytype,
                rides: rides
            }
            records.append(record)
    return records

class Row:
    def __init__(self, route, date, daytype, rides):
        self.route = route
        self.date = date
        self.daytype = daytype
        self.rides = rides

def read_rides_as_classes(filename):
    '''
    Read the bus ride data as a list of class instances
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = Row(route, date, daytype, rides)
            records.append(record)
    return records

def read_rides_as_namedtuples(filename):
    '''
    Read the bus ride data as a list of namedtuple 
    '''
    from collections import namedtuple
    Row = namedtuple('Row', ['route', 'date', 'daytype', 'rides'])

    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = Row(route, date, daytype, rides)
            records.append(record)
    return records

class Row2:
    __slots__ = ['route', 'date', 'daytype', 'rides']
    def __init__(self, route, date, daytype, rides):
        self.route = route
        self.date = date
        self.daytype = daytype
        self.rides = rides

def read_rides_as_class_with_slots(filename):
    '''
    Read the bus ride data as a list of class instances
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = Row2(route, date, daytype, rides)
            records.append(record)
    return records

if __name__ == '__main__':
    import tracemalloc
    tracemalloc.start()
    option = sys.argv[1]
    if option == 'as_tuples':
        rows = read_rides_as_tuples('Data/ctabus.csv')
    elif option == 'as_dicts':
        rows = read_rides_as_dicts('Data/ctabus.csv')
    elif option == 'as_class':
        rows = read_rides_as_classes('Data/ctabus.csv')
    elif option == 'as_slots':
        rows = read_rides_as_class_with_slots('Data/ctabus.csv')
    elif option == 'as_namedtuples':
        rows = read_rides_as_namedtuples('Data/ctabus.csv')
    print('Memory Use: Current %d, Peak %d' % tracemalloc.get_traced_memory())