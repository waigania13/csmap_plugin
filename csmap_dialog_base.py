# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'csmap_dialog_base.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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
        CSMapDialogBase.resize(411, 330)
        self.button_box = QtGui.QDialogButtonBox(CSMapDialogBase)
        self.button_box.setGeometry(QtCore.QRect(50, 290, 341, 32))
        self.button_box.setOrientation(QtCore.Qt.Horizontal)
        self.button_box.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.button_box.setObjectName(_fromUtf8("button_box"))
        self.mMapLayerComboBox = QgsMapLayerComboBox(CSMapDialogBase)
        self.mMapLayerComboBox.setGeometry(QtCore.QRect(140, 90, 251, 27))
        self.mMapLayerComboBox.setObjectName(_fromUtf8("mMapLayerComboBox"))
        self.mMapLayerComboBox.setFilters(QgsMapLayerProxyModel.RasterLayer)
        self.label = QtGui.QLabel(CSMapDialogBase)
        self.label.setGeometry(QtCore.QRect(20, 90, 101, 31))
        self.label.setObjectName(_fromUtf8("label"))
        self.curvature_box = QtGui.QComboBox(CSMapDialogBase)
        self.curvature_box.setGeometry(QtCore.QRect(140, 250, 251, 22))
        self.curvature_box.setObjectName(_fromUtf8("curvature_box"))
        self.curvature_box.addItem(_fromUtf8(""))
        self.curvature_box.addItem(_fromUtf8(""))
        self.curvature_box.addItem(_fromUtf8(""))
        self.curvature_box.addItem(_fromUtf8(""))
        self.curvature_box.addItem(_fromUtf8(""))
        self.curvature_box.addItem(_fromUtf8(""))
        self.curvature_box.addItem(_fromUtf8(""))
        self.curvature_box.addItem(_fromUtf8(""))
        self.curvature_box.addItem(_fromUtf8(""))
        self.curvature_box.addItem(_fromUtf8(""))
        self.label_2 = QtGui.QLabel(CSMapDialogBase)
        self.label_2.setGeometry(QtCore.QRect(20, 250, 111, 31))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.csmap_button = QtGui.QRadioButton(CSMapDialogBase)
        self.csmap_button.setGeometry(QtCore.QRect(30, 40, 86, 16))
        self.csmap_button.setChecked(True)
        self.csmap_button.setObjectName(_fromUtf8("csmap_button"))
        self.csmap_mode = QtGui.QButtonGroup(CSMapDialogBase)
        self.csmap_mode.setObjectName(_fromUtf8("csmap_mode"))
        self.csmap_mode.addButton(self.csmap_button)
        self.csmpa_button2 = QtGui.QRadioButton(CSMapDialogBase)
        self.csmpa_button2.setGeometry(QtCore.QRect(130, 40, 211, 16))
        self.csmpa_button2.setObjectName(_fromUtf8("csmpa_button2"))
        self.csmap_mode.addButton(self.csmpa_button2)
        self.groupBox = QtGui.QGroupBox(CSMapDialogBase)
        self.groupBox.setGeometry(QtCore.QRect(20, 10, 371, 71))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.label_3 = QtGui.QLabel(CSMapDialogBase)
        self.label_3.setGeometry(QtCore.QRect(20, 130, 161, 31))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.param_standard = QgsSpinBox(CSMapDialogBase)
        self.param_standard.setGeometry(QtCore.QRect(190, 160, 83, 27))
        self.param_standard.setProperty("value", 3)
        self.param_standard.setObjectName(_fromUtf8("param_standard"))
        self.label_4 = QtGui.QLabel(CSMapDialogBase)
        self.label_4.setGeometry(QtCore.QRect(40, 160, 121, 31))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(CSMapDialogBase)
        self.label_5.setGeometry(QtCore.QRect(40, 200, 41, 31))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.param_radius = QgsSpinBox(CSMapDialogBase)
        self.param_radius.setGeometry(QtCore.QRect(190, 200, 83, 27))
        self.param_radius.setProperty("value", 12)
        self.param_radius.setObjectName(_fromUtf8("param_radius"))
        self.groupBox.raise_()
        self.button_box.raise_()
        self.mMapLayerComboBox.raise_()
        self.label.raise_()
        self.curvature_box.raise_()
        self.label_2.raise_()
        self.csmap_button.raise_()
        self.csmpa_button2.raise_()
        self.label_3.raise_()
        self.param_standard.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.param_radius.raise_()

        self.retranslateUi(CSMapDialogBase)
        QtCore.QObject.connect(self.button_box, QtCore.SIGNAL(_fromUtf8("accepted()")), CSMapDialogBase.accept)
        QtCore.QObject.connect(self.button_box, QtCore.SIGNAL(_fromUtf8("rejected()")), CSMapDialogBase.reject)
        QtCore.QObject.connect(self.csmpa_button2, QtCore.SIGNAL(_fromUtf8("pressed()")), self.curvature_box.hide)
        QtCore.QObject.connect(self.csmap_button, QtCore.SIGNAL(_fromUtf8("pressed()")), self.curvature_box.show)
        QtCore.QObject.connect(self.csmpa_button2, QtCore.SIGNAL(_fromUtf8("pressed()")), self.label_2.hide)
        QtCore.QObject.connect(self.csmap_button, QtCore.SIGNAL(_fromUtf8("pressed()")), self.label_2.show)
        QtCore.QMetaObject.connectSlotsByName(CSMapDialogBase)

    def retranslateUi(self, CSMapDialogBase):
        CSMapDialogBase.setWindowTitle(_translate("CSMapDialogBase", "CSMapMaker", None))
        self.label.setText(_translate("CSMapDialogBase", "DEM Layer", None))
        self.curvature_box.setItemText(0, _translate("CSMapDialogBase", "General Curvature", None))
        self.curvature_box.setItemText(1, _translate("CSMapDialogBase", "Profile Curvature", None))
        self.curvature_box.setItemText(2, _translate("CSMapDialogBase", "Plan Curvature", None))
        self.curvature_box.setItemText(3, _translate("CSMapDialogBase", "Tangential Curvature", None))
        self.curvature_box.setItemText(4, _translate("CSMapDialogBase", "Longitudinal Curvature", None))
        self.curvature_box.setItemText(5, _translate("CSMapDialogBase", "Cross-Sectional Curvature", None))
        self.curvature_box.setItemText(6, _translate("CSMapDialogBase", "Minimal Curvature", None))
        self.curvature_box.setItemText(7, _translate("CSMapDialogBase", "Maximal Curvature", None))
        self.curvature_box.setItemText(8, _translate("CSMapDialogBase", "Total Curvature", None))
        self.curvature_box.setItemText(9, _translate("CSMapDialogBase", "Flow Line Curvature", None))
        self.label_2.setText(_translate("CSMapDialogBase", "Curvature Method", None))
        self.csmap_button.setText(_translate("CSMapDialogBase", "CS-MAP", None))
        self.csmpa_button2.setText(_translate("CSMapDialogBase", "CS-MAP(Plan+General)", None))
        self.groupBox.setTitle(_translate("CSMapDialogBase", "mode", None))
        self.label_3.setText(_translate("CSMapDialogBase", "Gaussian Filter Parameters", None))
        self.label_4.setText(_translate("CSMapDialogBase", "Standard Deviation", None))
        self.label_5.setText(_translate("CSMapDialogBase", "Radius", None))

from qgis.gui import QgsMapLayerComboBox, QgsSpinBox, QgsMapLayerProxyModel
