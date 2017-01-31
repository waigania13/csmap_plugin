# -*- coding: utf-8 -*-
"""
/***************************************************************************
 CSMapDialog
                                 A QGIS plugin
 csmap plugin
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

import os

from PyQt4 import QtGui, uic
from csmap_dialog_base import Ui_CSMapDialogBase
#FORM_CLASS, _ = uic.loadUiType(os.path.join(
#    os.path.dirname(__file__), 'csmap_dialog_base.ui'))


class CSMapDialog(QtGui.QDialog, Ui_CSMapDialogBase):
    def __init__(self, parent=None):
        """Constructor."""
        super(CSMapDialog, self).__init__(parent)
        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)

    def accept(self):
        pass
