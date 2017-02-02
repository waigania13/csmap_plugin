# CS立体図作成 QGISプラグイン
QGISで、長野県林業総合センター 戸田さまが開発したCS立体図を作成するためのプラグインです　　

- zipでダウンロード
- 解凍後のディレクトリを丸ごと、ユーザディレクトリ/.qgis2/python/pluginsにコピー
- QGISを起動してプラグインを有効にすると、メニューの「ラスタ」に「csmap」が入ります 
- 実行して、ラスタレイヤを選択して「OK」をクリックすると一式計算します 

# 開発向け注意
qtデザイナでqgis custom widgetを使った場合に、エラーになる問題への対処  
- csmap_dialog_base.uiのcustomwidget headerの部分をqgis.guiに書き換え　　
- csmap_dialog_base.uiをpyuic4 -o csmap_dialog_base.py csmap_dialog_base.ui
 で変換　　
- 変換後のcsmap_dialog_base.pyにself.mMapLayerComboBox.setFilters(QgsMapLayerProxyModel.RasterLayer)を追記　　
- 変換後のcsmap_dialog_base.pyをfrom qgis.gui import QgsMapLayerComboBox, QgsMapLayerProxyModelに変更
