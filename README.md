# csmap_plugin
csmap plugin for qgis

# 注意
- csmap_dialog_base.uiをpyuic4 -o csmap_dialog_base.py csmap_dialog_base.ui
 で変換　　
- csmap_dialog_base.uiのcustomwidget headerの部分をgis.guiに書き換え　　
- 変換後のcsmap_dialog_base.pyにself.mMapLayerComboBox.setFilters(QgsMapLayerProxyModel.RasterLayer)を追記　　
