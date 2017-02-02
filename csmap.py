# -*- coding: utf-8 -*-
"""
/***************************************************************************
 CSMap
                                 A QGIS plugin
 CSMapMaker plugin
                              -------------------
        begin                : 2017-01-31
        git sha              : $Format:%H$
        copyright            : (C) 2017 by MIERUNE,LCC.
        email                : info@mierune.co.jp
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
from PyQt4.QtCore import QSettings, QTranslator, qVersion, QCoreApplication
from PyQt4.QtGui import QAction, QIcon
# Initialize Qt resources from file resources.py
import resources
# Import the code for the dialog
from csmap_dialog import CSMapDialog
import os.path
from csmap_make import *


class CSMap:
    """QGIS Plugin Implementation."""

    def __init__(self, iface):
        """Constructor.

        :param iface: An interface instance that will be passed to this class
            which provides the hook by which you can manipulate the QGIS
            application at run time.
        :type iface: QgsInterface
        """
        # Save reference to the QGIS interface
        self.iface = iface
        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)
        # initialize locale
        locale = QSettings().value('locale/userLocale')[0:2]
        locale_path = os.path.join(
            self.plugin_dir,
            'i18n',
            'CSMap_{}.qm'.format(locale))

        if os.path.exists(locale_path):
            self.translator = QTranslator()
            self.translator.load(locale_path)

            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)

        # Create the dialog (after translation) and keep reference
        self.dlg = CSMapDialog()
        self.dlg.button_box.accepted.connect(self.csmap)

        # Declare instance attributes
        self.actions = []
        self.menu = self.tr(u'&CSMapMaker')
        # TODO: We are going to let the user set this up in a future iteration
        self.toolbar = self.iface.addToolBar(u'CSMap')
        self.toolbar.setObjectName(u'CSMap')

    # noinspection PyMethodMayBeStatic
    def tr(self, message):
        """Get the translation for a string using Qt translation API.

        We implement this ourselves since we do not inherit QObject.

        :param message: String for translation.
        :type message: str, QString

        :returns: Translated version of message.
        :rtype: QString
        """
        # noinspection PyTypeChecker,PyArgumentList,PyCallByClass
        return QCoreApplication.translate('CSMap', message)


    def add_action(
        self,
        icon_path,
        text,
        callback,
        enabled_flag=True,
        add_to_menu=True,
        add_to_toolbar=True,
        status_tip=None,
        whats_this=None,
        parent=None):
        """Add a toolbar icon to the toolbar.

        :param icon_path: Path to the icon for this action. Can be a resource
            path (e.g. ':/plugins/foo/bar.png') or a normal file system path.
        :type icon_path: str

        :param text: Text that should be shown in menu items for this action.
        :type text: str

        :param callback: Function to be called when the action is triggered.
        :type callback: function

        :param enabled_flag: A flag indicating if the action should be enabled
            by default. Defaults to True.
        :type enabled_flag: bool

        :param add_to_menu: Flag indicating whether the action should also
            be added to the menu. Defaults to True.
        :type add_to_menu: bool

        :param add_to_toolbar: Flag indicating whether the action should also
            be added to the toolbar. Defaults to True.
        :type add_to_toolbar: bool

        :param status_tip: Optional text to show in a popup when mouse pointer
            hovers over the action.
        :type status_tip: str

        :param parent: Parent widget for the new action. Defaults None.
        :type parent: QWidget

        :param whats_this: Optional text to show in the status bar when the
            mouse pointer hovers over the action.

        :returns: The action that was created. Note that the action is also
            added to self.actions list.
        :rtype: QAction
        """

        icon = QIcon(icon_path)
        action = QAction(icon, text, parent)
        action.triggered.connect(callback)
        action.setEnabled(enabled_flag)

        if status_tip is not None:
            action.setStatusTip(status_tip)

        if whats_this is not None:
            action.setWhatsThis(whats_this)

        if add_to_toolbar:
            self.toolbar.addAction(action)

        if add_to_menu:
            self.iface.addPluginToRasterMenu(
                self.menu,
                action)

        self.actions.append(action)

        return action

    def initGui(self):
        """Create the menu entries and toolbar icons inside the QGIS GUI."""

        icon_path = ':/plugins/CSMap/icon.png'
        self.add_action(
            icon_path,
            text=self.tr(u'CSMapMaker'),
            callback=self.run,
            parent=self.iface.mainWindow())


    def unload(self):
        """Removes the plugin menu item and icon from QGIS GUI."""
        for action in self.actions:
            self.iface.removePluginRasterMenu(
                self.tr(u'&CSMapMaker'),
                action)
            self.iface.removeToolBarIcon(action)
        # remove the toolbar
        del self.toolbar


    def run(self):
        """Run method that performs all the real work"""
        # show the dialog
        self.dlg.show()
        # Run the dialog event loop
        result = self.dlg.exec_()
        # See if OK was pressed
        if result:
            # Do something useful here - delete the line containing pass and
            # substitute with your code.
            pass

    def csmap(self): 
        layer = self.dlg.mMapLayerComboBox.currentLayer()
        curvature_text = self.dlg.curvature_box.currentText()
        if layer is None:
            return
        if curvature_text == 'General Curvature':
            curvature_method = 'C_GENE'
        elif curvature_text == 'Profile Curvature':
            curvature_method = 'C_PROF'
        elif curvature_text == 'Plan Curvature':
            curvature_method = 'C_PLAN'
        elif curvature_text == 'Tangential Curvature':
            curvature_method = 'C_TANG'
        elif curvature_text == 'Longitudinal Curvature':
            curvature_method = 'C_LONG'
        elif curvature_text == 'Cross-Sectional Curvature':
            curvature_method = 'C_CROS'
        elif curvature_text == 'Minimal Curvature':
            curvature_method = 'C_MINI'
        elif curvature_text == 'Maximal Curvature':
            curvature_method = 'C_MAXI'
        elif curvature_text == 'Total Curvature':
            curvature_method = 'C_TOTA'
        elif curvature_text == 'Flow Line Curvature':
            curvature_method = 'C_ROTO'
        csmapMake(self.iface, layer, curvature_method)
