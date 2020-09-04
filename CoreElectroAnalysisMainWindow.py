# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Python36\Scripts\CoreElectroAnalysis\ui\CoreElectroAnalysisMainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.verticalLayout.setContentsMargins(9, -1, -1, -1)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.InitFilePathSetButton = QtWidgets.QToolButton(self.centralwidget)
        self.InitFilePathSetButton.setMinimumSize(QtCore.QSize(0, 30))
        self.InitFilePathSetButton.setMaximumSize(QtCore.QSize(30, 30))
        self.InitFilePathSetButton.setObjectName("InitFilePathSetButton")
        self.horizontalLayout_3.addWidget(self.InitFilePathSetButton)
        self.InitFilePathField = QtWidgets.QTextEdit(self.centralwidget)
        self.InitFilePathField.setEnabled(True)
        self.InitFilePathField.setMinimumSize(QtCore.QSize(0, 30))
        self.InitFilePathField.setMaximumSize(QtCore.QSize(16777215, 30))
        self.InitFilePathField.setToolTip("")
        self.InitFilePathField.setObjectName("InitFilePathField")
        self.horizontalLayout_3.addWidget(self.InitFilePathField)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Table_layout = QtWidgets.QVBoxLayout()
        self.Table_layout.setObjectName("Table_layout")
        self.Filtrlayout = QtWidgets.QHBoxLayout()
        self.Filtrlayout.setObjectName("Filtrlayout")
        self.combobox_mode = QtWidgets.QComboBox(self.centralwidget)
        self.combobox_mode.setObjectName("combobox_mode")
        self.combobox_mode.addItem("")
        self.combobox_mode.addItem("")
        self.Filtrlayout.addWidget(self.combobox_mode)
        self.verticalLayout_wells = QtWidgets.QVBoxLayout()
        self.verticalLayout_wells.setObjectName("verticalLayout_wells")
        self.wells_sampling_checkbox = QtWidgets.QCheckBox(self.centralwidget)
        self.wells_sampling_checkbox.setObjectName("wells_sampling_checkbox")
        self.verticalLayout_wells.addWidget(self.wells_sampling_checkbox)
        self.listWidget_well_chose = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_well_chose.setMaximumSize(QtCore.QSize(90, 150))
        self.listWidget_well_chose.setObjectName("listWidget_well_chose")
        self.verticalLayout_wells.addWidget(self.listWidget_well_chose)
        self.Filtrlayout.addLayout(self.verticalLayout_wells)
        self.verticalLayout_zones = QtWidgets.QVBoxLayout()
        self.verticalLayout_zones.setObjectName("verticalLayout_zones")
        self.zones_sampling_checkbox = QtWidgets.QCheckBox(self.centralwidget)
        self.zones_sampling_checkbox.setObjectName("zones_sampling_checkbox")
        self.verticalLayout_zones.addWidget(self.zones_sampling_checkbox)
        self.listWidget_zone_chose = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_zone_chose.setMaximumSize(QtCore.QSize(90, 150))
        self.listWidget_zone_chose.setObjectName("listWidget_zone_chose")
        self.verticalLayout_zones.addWidget(self.listWidget_zone_chose)
        self.Filtrlayout.addLayout(self.verticalLayout_zones)
        self.verticalLayout_lith = QtWidgets.QVBoxLayout()
        self.verticalLayout_lith.setObjectName("verticalLayout_lith")
        self.lith_sampling_checkbox = QtWidgets.QCheckBox(self.centralwidget)
        self.lith_sampling_checkbox.setObjectName("lith_sampling_checkbox")
        self.verticalLayout_lith.addWidget(self.lith_sampling_checkbox)
        self.listWidget_lith_chose = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_lith_chose.setMaximumSize(QtCore.QSize(90, 150))
        self.listWidget_lith_chose.setObjectName("listWidget_lith_chose")
        self.verticalLayout_lith.addWidget(self.listWidget_lith_chose)
        self.Filtrlayout.addLayout(self.verticalLayout_lith)
        self.Table_layout.addLayout(self.Filtrlayout)
        self.InitDataTable = QtWidgets.QTableWidget(self.centralwidget)
        self.InitDataTable.setMinimumSize(QtCore.QSize(300, 300))
        self.InitDataTable.setMaximumSize(QtCore.QSize(500, 16777215))
        self.InitDataTable.setObjectName("InitDataTable")
        self.InitDataTable.setColumnCount(0)
        self.InitDataTable.setRowCount(0)
        self.Table_layout.addWidget(self.InitDataTable)
        self.horizontalLayout_2.addLayout(self.Table_layout)
        self.MplWidget = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MplWidget.sizePolicy().hasHeightForWidth())
        self.MplWidget.setSizePolicy(sizePolicy)
        self.MplWidget.setMinimumSize(QtCore.QSize(300, 300))
        self.MplWidget.setObjectName("MplWidget")
        self.horizontalLayout_2.addWidget(self.MplWidget)
        self.ToolbarWidget = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ToolbarWidget.sizePolicy().hasHeightForWidth())
        self.ToolbarWidget.setSizePolicy(sizePolicy)
        self.ToolbarWidget.setObjectName("ToolbarWidget")
        self.horizontalLayout_2.addWidget(self.ToolbarWidget)
        self.horizontalLayout_2.setStretch(1, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.LoadDataButton = QtWidgets.QToolButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LoadDataButton.sizePolicy().hasHeightForWidth())
        self.LoadDataButton.setSizePolicy(sizePolicy)
        self.LoadDataButton.setMinimumSize(QtCore.QSize(50, 50))
        self.LoadDataButton.setMaximumSize(QtCore.QSize(50, 50))
        self.LoadDataButton.setObjectName("LoadDataButton")
        self.horizontalLayout.addWidget(self.LoadDataButton)
        self.GetCategoriesButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.GetCategoriesButton.sizePolicy().hasHeightForWidth())
        self.GetCategoriesButton.setSizePolicy(sizePolicy)
        self.GetCategoriesButton.setMinimumSize(QtCore.QSize(0, 30))
        self.GetCategoriesButton.setMaximumSize(QtCore.QSize(16777215, 30))
        self.GetCategoriesButton.setFocusPolicy(QtCore.Qt.TabFocus)
        self.GetCategoriesButton.setObjectName("GetCategoriesButton")
        self.horizontalLayout.addWidget(self.GetCategoriesButton)
        self.PlotGraphButton = QtWidgets.QToolButton(self.centralwidget)
        self.PlotGraphButton.setMinimumSize(QtCore.QSize(0, 30))
        self.PlotGraphButton.setMaximumSize(QtCore.QSize(16777215, 30))
        self.PlotGraphButton.setObjectName("PlotGraphButton")
        self.horizontalLayout.addWidget(self.PlotGraphButton)
        self.PlotReportButton = QtWidgets.QToolButton(self.centralwidget)
        self.PlotReportButton.setMinimumSize(QtCore.QSize(0, 30))
        self.PlotReportButton.setMaximumSize(QtCore.QSize(16777215, 30))
        self.PlotReportButton.setCheckable(True)
        self.PlotReportButton.setObjectName("PlotReportButton")
        self.horizontalLayout.addWidget(self.PlotReportButton)
        self.AdjustPorosityMButton = QtWidgets.QToolButton(self.centralwidget)
        self.AdjustPorosityMButton.setMinimumSize(QtCore.QSize(0, 30))
        self.AdjustPorosityMButton.setMaximumSize(QtCore.QSize(16777215, 30))
        self.AdjustPorosityMButton.setObjectName("AdjustPorosityMButton")
        self.horizontalLayout.addWidget(self.AdjustPorosityMButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout.setStretch(1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.InitFilePathSetButton.setToolTip(_translate("MainWindow", "Choose file path"))
        self.InitFilePathSetButton.setText(_translate("MainWindow", "..."))
        self.InitFilePathField.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">C:/Python36/Scripts/CoreElectroAnalysis/data/core_studies_ff.txt</span></p></body></html>"))
        self.combobox_mode.setItemText(0, _translate("MainWindow", "general"))
        self.combobox_mode.setItemText(1, _translate("MainWindow", "sampling"))
        self.wells_sampling_checkbox.setText(_translate("MainWindow", "Wells"))
        self.zones_sampling_checkbox.setText(_translate("MainWindow", "Zones"))
        self.lith_sampling_checkbox.setText(_translate("MainWindow", "Lith"))
        self.LoadDataButton.setToolTip(_translate("MainWindow", "Load Data"))
        self.LoadDataButton.setText(_translate("MainWindow", "..."))
        self.GetCategoriesButton.setToolTip(_translate("MainWindow", "Get categories"))
        self.GetCategoriesButton.setText(_translate("MainWindow", "Get Categories"))
        self.PlotGraphButton.setText(_translate("MainWindow", "Plot (Por vs FF)"))
        self.PlotReportButton.setText(_translate("MainWindow", "Plot report"))
        self.AdjustPorosityMButton.setText(_translate("MainWindow", "Adjust porosity-m relation"))

