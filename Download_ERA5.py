# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 16:52:34 2021

@author: MZG
"""

import cdsapi

#yrs = ['2015','2016','2017','2018','2019']
yrs =['2015']
mns = ['01', '02', '03',
            '04', '05', '06',
            '07', '08', '09',
            '10', '11', '12',
            ]

c = cdsapi.Client()

c.retrieve(
    'reanalysis-era5-single-levels',
    {
        'product_type':'reanalysis',
        'variable':[
            'total_precipitation','10m_u_component_of_wind', 
            '10m_v_component_of_wind', '2m_temperature',
        ],
        'year':yrs,
        'month':mns,
        'day':[
            '01','02','03',
            '04','05','06',
            '07','08','09',
            '10','11','12',
            '13','14','15',
            '16','17','18',
            '19','20','21',
            '22','23','24',
            '25','26','27',
            '28','29','30',
            '31',
        ],
        'time':['00:00','01:00','02:00','03:00','04:00','05:00','06:00','07:00',
                '08:00','09:00','10:00','11:00','12:00','13:00','14:00','15:00',
               '16:00','17:00','18:00','19:00','20:00','21:00','22:00','23:00',
               ],

        'area': [60,-120,49,-110,],
        'grid':[0.25,0.25],
        'format':'netcdf',
    },
    r'D:\ERA5_LDARSim\ERA5_weather.nc')