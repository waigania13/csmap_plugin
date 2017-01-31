from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.utils import *
from osgeo import gdal
import processing

def setLayerStyle(iface, layer, color_name, rank, reverse, min=None, max=None):
    if min is None or max is None:
        data = gdal.Open(layer.dataProvider().dataSourceUri())
        band = data.GetRasterBand(1)
        (min,max) = band.ComputeRasterMinMax(1)
    
    sa = (max - min)/rank
    
    if color_name == 'WhiteToBlack':
        lst =  [ QgsColorRampShader.ColorRampItem(min, QColor(255,255,255), str(round(min,3))), QgsColorRampShader.ColorRampItem(max, QColor(0,0,0), str(round(max,3))) ]
    else :
        lst = []
        for i in range(rank):
            idx = rank-1-i if reverse else i
            lst.append(QgsColorRampShader.ColorRampItem(min+sa*i, QgsColorBrewerPalette.listSchemeColors(color_name, rank)[idx], str(round(min+sa*i,3))))
    
    myRasterShader = QgsRasterShader()
    myColorRamp = QgsColorRampShader()

    myColorRamp.setColorRampItemList(lst)
    myColorRamp.setColorRampType(QgsColorRampShader.INTERPOLATED)
    myRasterShader.setRasterShaderFunction(myColorRamp)

    myPseudoRenderer = QgsSingleBandPseudoColorRenderer(layer.dataProvider(), layer.type(),  myRasterShader)

    layer.setRenderer(myPseudoRenderer)
    layer.renderer().setOpacity(0.5)

    layer.triggerRepaint()
    iface.legendInterface().refreshLayerSymbology(layer)

def csmapMake(iface, dem):
    dem_result = processing.runalg("saga:slopeaspectcurvature", dem,  6, 0, 0, None, None, None, None, None, None,None, None, None, None, None, None)

    gaussian = processing.runalg("saga:gaussianfilter", dem, 3, 1, 12, None)
    result = processing.runalg("saga:slopeaspectcurvature", gaussian["RESULT"],  6, 0, 0, None, None, None, None, None, None,None, None, None, None, None, None)

    #gaussian_layer = processing.load(gaussian["RESULT"])
    curvature_layer = processing.load(result["C_PLAN"])
    slope_layer = processing.load(dem_result["SLOPE"])
    curvature_layer2 = processing.load(result["C_PLAN"])
    slope_layer2 = processing.load(dem_result["SLOPE"])

    setLayerStyle(iface, curvature_layer, "Blues", 9, True, -0.2, 0.2)
    setLayerStyle(iface, curvature_layer2, "RdBu", 9, True, -0.2, 0.2)
    setLayerStyle(iface, slope_layer, "Oranges", 9, False)
    setLayerStyle(iface, slope_layer2, "WhiteToBlack", 2, False)
