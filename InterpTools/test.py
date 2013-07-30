# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 17:27:42 2013

@author: chaco3
"""

import pyximport
pyximport.install()
import IDW
import Kriging

def tIDW():
    '''
    IDW Test
    '''
    Loc, POI, Prec = IDW.load_data('TestData\GaugeLoc.csv',
                                       'TestData\InterpPts.csv',
                                       'TestData\Dataset.csv')
    Z, Zavg = IDW.Interp_bat(Loc, POI, Prec, 2.0, 0.00001, 0, 20)
    return 'IDW working fine!'

def tKrig():
    '''
    Kriging test    
    '''
    Loc, POIC, Prec = Kriging.load_data('TestData\GaugeLoc.csv',
                                       'TestData\InterpPts.csv',
                                       'TestData\Dataset.csv')
                      
    SVExp, CovMea = Kriging.exp_semivariogram(Prec, Loc)
    
    xopt, ModOpt, VarFunArr = Kriging.theor_variogram(SVExp)
    
    Z, SP, ZAvg = Kriging.Krig(5.0, POIC, Loc, Prec, CovMea, ModOpt, xopt, 
                               VarFunArr,0 ,20)
    return 1