#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
from math import sqrt


from readtle import CatalogTLE

from calcsigma import drawShort_R
from calcsigma import drawShort_3
from calcsigma import drawShort_ephem

from calcsigma import drawLong_R
from calcsigma import drawLong_3
from calcsigma import drawLong_ephem

import matplotlib.pyplot as mpl


def oneSat(name_file):
    '''  Открытие файла -- каталога TLE
    '''
    catalog = CatalogTLE()
    catalog.readFullTLE(name_file)

#    print('Графики полной ошибки:')
#     drawShort_R(catalog)
#    drawLong_R(catalog)
#    drawLong_R(catalog, 10)

    print('Орбитальные ошибки:')
    # drawShort_3(catalog)
    drawLong_3(catalog)
#    drawLong_3(catalog, 10)

#    print('Ошибки большой полуоси:')
#    drawShort_ephem(catalog, 'a')
#    drawLong_ephem(catalog, 'a')
#    drawLong_ephem(catalog, 'a', 10)
#    
#    print('Эволюция параметров орбиты (на месяц):')
#    dT = range(0, 30, 1)
#    drawEphem_oneSat(catalog, 'a', dT)
#    drawEphem_allcatalog(catalog, 'a')
        

def plotGraf():

    print('Два раза Ку, земляне!')

    mpl.style.use('./presentation.mplstyle')

    oneSat('catalogs/ISS_2018-03-01+31.txt')
    
    oneSat('catalogs/navstar50_2018_01_01_30.txt')
        
    oneSat('catalogs/HIPPARCOS_2018_02_01+59.txt')
            
    oneSat('catalogs/SKRL_1_2018-03-01+31.txt')


if __name__ == "__main__":
    plotGraf()

