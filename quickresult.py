from sgp4.earth_gravity import wgs72
from sgp4.io import twoline2rv
from datetime import *

def getSatellites(tlefile):
    '''достает из тле файла имя спутника и создает экземпляр класса
    Satellite, который дальше можно использовать для работы модуля
    экстраполяции'''
    with open(tlefile, 'r') as fi:
        data = fi.readlines()
    satnames = data[0::3]
    indices = [j for j in range(len(data))][0::3]
    sats = []
    di = {}
    for i, name in enumerate(satnames):
        j = indices[i]
        sat = twoline2rv(data[j + 1], data[j + 2], wgs72)
        di[name[:-1]] = sat
    return di

def getCoordinates(tlefile, timetuple = -1):
    '''по названию тле файла и заданному в timetuple времени экстраполяции
    вычисляет положение и скорости, также выдает время привязки в
    секундах. timetuple надо задавать строго как (yyyy, mm, dd, hh, MM),
    mm - месяц ,MM  - минуты). Можно не задавать timetuple, тогда по
    дефолту будyт выдаваться координаты на время привязки'''
    di = getSatellites(tlefile)
    for name in di:
        sat = di[name]
        # TODO: проверить, что время привязки я определяю правильно
        current = sat.jdsatepoch + 17531 * 24 * 3600
        if timetuple == -1:
            time = datetime.fromtimestamp(current)
            timetuple = (time.year, time.month, time.day, time.hour,
                    time.minute, time.second + time.microsecond / 1e6)
        pos, velo = sat.propagate(*timetuple)
        di.update({name: (pos, velo, current)})
    return di

# def getExtroplation(tlefile):
