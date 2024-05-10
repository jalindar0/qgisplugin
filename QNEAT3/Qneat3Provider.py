# -*- coding: utf-8 -*-
"""
/***************************************************************************
 QNEAT3 - Qgis Network Analysis Toolbox 3
 A QGIS processing provider for network analysis
 
 Qneat3Provider.py
 
-------------------
        begin                : 2018-01-15
        copyright            : (C) 2018 by Clemens Raffler
        email                : clemens.raffler@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import os

from qgis.core import QgsProcessingProvider
from qgis.PyQt.QtGui import QIcon

from importlib import util
matplotlib_specification = util.find_spec("matplotlib", "pyplot")
matplotlib_found = matplotlib_specification is not None #evaluates to true if matplotlib.pyplot can be importet


#import all algorithms that work with basic qgis modules
from .algs import ( 
    ShortestPathBetweenPoints 
    )



pluginPath = os.path.split(os.path.dirname(__file__))[0]

class Qneat3Provider(QgsProcessingProvider):
    def __init__(self):
        super().__init__()
        self.matplotlib_specification = util.find_spec("matplotlib", "pyplot")
        self.matplotlib_found = self.matplotlib_specification is not None #evaluates to true if matplotlib.pyplot can be importet


    def id(self, *args, **kwargs):
        return 'qneat3'

    def name(self, *args, **kwargs):
        return 'Quanta - Qgis Network Analysis Toolbox'

    def icon(self):
        return QIcon(os.path.join(pluginPath, 'QNEAT3', 'icon_qneat3.svg'))

    def svgIconPath(self):
        return os.path.join(pluginPath, 'QNEAT3', 'icon_qneat3.svg')

    def loadAlgorithms(self, *args, **kwargs):
        self.addAlgorithm(ShortestPathBetweenPoints.ShortestPathBetweenPoints())
      

       