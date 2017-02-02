# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'csmap_dialog_base.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from qgis.gui import QgsMapLayerComboBox, QgsMapLayerProxyModel

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_CSMapDialogBase(object):
    def setupUi(self, CSMapDialogBase):
        CSMapDialogBase.setObjectName(_fromUtf8("CSMapDialogBase"))
        CSMapDialogBase.resize(383, 85)
        self.button_box = QtGui.QDialogButtonBox(CSMapDialogBase)
        self.button_box.setGeometry(QtCore.QRect(30, 50, 341, 32))
        self.button_box.setOrientation(QtCore.Qt.Horizontal)
        self.button_box.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.button_box.setObjectName(_fromUtf8("button_box"))
        self.mMapLayerComboBox = QgsMapLayerComboBox(CSMapDialogBase)
        self.mMapLayerComboBox.setGeometry(QtCore.QRect(99, 10, 271, 27))
        self.mMapLayerComboBox.setFilters(QgsMapLayerProxyModel.RasterLayer)
        self.mMapLayerComboBox.setObjectName(_fromUtf8("mMapLayerComboBox"))
        self.label = QtGui.QLabel(CSMapDialogBase)
        self.label.setGeometry(QtCore.QRect(10, 10, 81, 31))
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(CSMapDialogBase)
        QtCore.QObject.connect(self.button_box, QtCore.SIGNAL(_fromUtf8("accepted()")), CSMapDialogBase.accept)
        QtCore.QObject.connect(self.button_box, QtCore.SIGNAL(_fromUtf8("rejected()")), CSMapDialogBase.reject)
        QtCore.QMetaObject.connectSlotsByName(CSMapDialogBase)

    def retranslateUi(self, CSMapDialogBase):
        CSMapDialogBase.setWindowTitle(_translate("CSMapDialogBase", "CSMapMaker", None))
        self.label.setText(_translate("CSMapDialogBase", "DEM Layer", None))
