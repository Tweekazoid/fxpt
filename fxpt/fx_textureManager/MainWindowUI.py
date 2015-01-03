# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindowUI.ui'
#
# Created: Sat Jan 03 21:46:25 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 610)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(4)
        self.verticalLayout.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.uiBTN_filter = QtGui.QToolButton(self.centralwidget)
        self.uiBTN_filter.setMinimumSize(QtCore.QSize(24, 24))
        self.uiBTN_filter.setMaximumSize(QtCore.QSize(24, 24))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/filterDisabled.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap(":/icons/filterActive.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.uiBTN_filter.setIcon(icon)
        self.uiBTN_filter.setIconSize(QtCore.QSize(18, 18))
        self.uiBTN_filter.setCheckable(True)
        self.uiBTN_filter.setObjectName("uiBTN_filter")
        self.horizontalLayout.addWidget(self.uiBTN_filter)
        self.uiLED_filter = QtGui.QLineEdit(self.centralwidget)
        self.uiLED_filter.setMinimumSize(QtCore.QSize(0, 24))
        self.uiLED_filter.setObjectName("uiLED_filter")
        self.horizontalLayout.addWidget(self.uiLED_filter)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.uiTBL_textures = QtGui.QTableView(self.centralwidget)
        self.uiTBL_textures.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.uiTBL_textures.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.uiTBL_textures.setAlternatingRowColors(True)
        self.uiTBL_textures.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.uiTBL_textures.setTextElideMode(QtCore.Qt.ElideLeft)
        self.uiTBL_textures.setHorizontalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.uiTBL_textures.setShowGrid(False)
        self.uiTBL_textures.setSortingEnabled(True)
        self.uiTBL_textures.setObjectName("uiTBL_textures")
        self.uiTBL_textures.horizontalHeader().setSortIndicatorShown(True)
        self.uiTBL_textures.horizontalHeader().setStretchLastSection(True)
        self.uiTBL_textures.verticalHeader().setVisible(False)
        self.uiTBL_textures.verticalHeader().setDefaultSectionSize(15)
        self.uiTBL_textures.verticalHeader().setMinimumSectionSize(15)
        self.verticalLayout.addWidget(self.uiTBL_textures)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuActions = QtGui.QMenu(self.menubar)
        self.menuActions.setObjectName("menuActions")
        self.menuEdit = QtGui.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuOptions = QtGui.QMenu(self.menubar)
        self.menuOptions.setObjectName("menuOptions")
        self.menuSelect = QtGui.QMenu(self.menubar)
        self.menuSelect.setObjectName("menuSelect")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setMovable(False)
        self.toolBar.setIconSize(QtCore.QSize(24, 24))
        self.toolBar.setFloatable(False)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.uiACT_refresh = QtGui.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/refresh.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.uiACT_refresh.setIcon(icon1)
        self.uiACT_refresh.setObjectName("uiACT_refresh")
        self.uiACT_exit = QtGui.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.uiACT_exit.setIcon(icon2)
        self.uiACT_exit.setObjectName("uiACT_exit")
        self.uiACT_retarget = QtGui.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/retarget.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.uiACT_retarget.setIcon(icon3)
        self.uiACT_retarget.setObjectName("uiACT_retarget")
        self.uiACT_copyMove = QtGui.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/copyMove.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.uiACT_copyMove.setIcon(icon4)
        self.uiACT_copyMove.setObjectName("uiACT_copyMove")
        self.uiACT_searchReplace = QtGui.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/replace.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.uiACT_searchReplace.setIcon(icon5)
        self.uiACT_searchReplace.setObjectName("uiACT_searchReplace")
        self.uiACT_copyFullPath = QtGui.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/copy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.uiACT_copyFullPath.setIcon(icon6)
        self.uiACT_copyFullPath.setObjectName("uiACT_copyFullPath")
        self.uiACT_copyFilename = QtGui.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icons/copy2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.uiACT_copyFilename.setIcon(icon7)
        self.uiACT_copyFilename.setObjectName("uiACT_copyFilename")
        self.uiACT_selectAssigned = QtGui.QAction(MainWindow)
        self.uiACT_selectAssigned.setCheckable(True)
        self.uiACT_selectAssigned.setObjectName("uiACT_selectAssigned")
        self.uiACT_removeDuplicatesFromClipboard = QtGui.QAction(MainWindow)
        self.uiACT_removeDuplicatesFromClipboard.setCheckable(True)
        self.uiACT_removeDuplicatesFromClipboard.setObjectName("uiACT_removeDuplicatesFromClipboard")
        self.uiACT_selectAll = QtGui.QAction(MainWindow)
        self.uiACT_selectAll.setObjectName("uiACT_selectAll")
        self.uiACT_selectNone = QtGui.QAction(MainWindow)
        self.uiACT_selectNone.setObjectName("uiACT_selectNone")
        self.uiACT_selectInvert = QtGui.QAction(MainWindow)
        self.uiACT_selectInvert.setObjectName("uiACT_selectInvert")
        self.menuFile.addAction(self.uiACT_refresh)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.uiACT_exit)
        self.menuActions.addAction(self.uiACT_copyMove)
        self.menuActions.addAction(self.uiACT_retarget)
        self.menuActions.addAction(self.uiACT_searchReplace)
        self.menuEdit.addAction(self.uiACT_copyFullPath)
        self.menuEdit.addAction(self.uiACT_copyFilename)
        self.menuOptions.addAction(self.uiACT_selectAssigned)
        self.menuOptions.addAction(self.uiACT_removeDuplicatesFromClipboard)
        self.menuSelect.addAction(self.uiACT_selectAll)
        self.menuSelect.addAction(self.uiACT_selectInvert)
        self.menuSelect.addAction(self.uiACT_selectNone)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuSelect.menuAction())
        self.menubar.addAction(self.menuActions.menuAction())
        self.menubar.addAction(self.menuOptions.menuAction())
        self.toolBar.addAction(self.uiACT_refresh)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.uiACT_copyFullPath)
        self.toolBar.addAction(self.uiACT_copyFilename)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.uiACT_copyMove)
        self.toolBar.addAction(self.uiACT_retarget)
        self.toolBar.addAction(self.uiACT_searchReplace)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.uiACT_exit, QtCore.SIGNAL("triggered()"), MainWindow.close)
        QtCore.QObject.connect(self.uiACT_refresh, QtCore.SIGNAL("triggered()"), MainWindow.onRefreshTriggered)
        QtCore.QObject.connect(self.uiACT_copyFullPath, QtCore.SIGNAL("triggered()"), MainWindow.onCopyFullPathTriggered)
        QtCore.QObject.connect(self.uiACT_copyFilename, QtCore.SIGNAL("triggered()"), MainWindow.onCopyFilenameTriggered)
        QtCore.QObject.connect(self.uiACT_copyMove, QtCore.SIGNAL("triggered()"), MainWindow.onCopyMoveTriggered)
        QtCore.QObject.connect(self.uiACT_retarget, QtCore.SIGNAL("triggered()"), MainWindow.onRetargetTriggered)
        QtCore.QObject.connect(self.uiACT_searchReplace, QtCore.SIGNAL("triggered()"), MainWindow.onSearchReplaceTriggered)
        QtCore.QObject.connect(self.uiLED_filter, QtCore.SIGNAL("textChanged(QString)"), MainWindow.onFilterTextChanged)
        QtCore.QObject.connect(self.uiBTN_filter, QtCore.SIGNAL("toggled(bool)"), MainWindow.onFilterButtonToggled)
        QtCore.QObject.connect(self.uiACT_selectAll, QtCore.SIGNAL("triggered()"), MainWindow.onSelectAllTriggered)
        QtCore.QObject.connect(self.uiACT_selectInvert, QtCore.SIGNAL("triggered()"), MainWindow.onSelectInvertTriggered)
        QtCore.QObject.connect(self.uiACT_selectNone, QtCore.SIGNAL("triggered()"), MainWindow.onSelectNoneTriggered)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Texture Manager", None, QtGui.QApplication.UnicodeUTF8))
        self.uiBTN_filter.setText(QtGui.QApplication.translate("MainWindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuActions.setTitle(QtGui.QApplication.translate("MainWindow", "Actions", None, QtGui.QApplication.UnicodeUTF8))
        self.menuEdit.setTitle(QtGui.QApplication.translate("MainWindow", "Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.menuOptions.setTitle(QtGui.QApplication.translate("MainWindow", "Options", None, QtGui.QApplication.UnicodeUTF8))
        self.menuSelect.setTitle(QtGui.QApplication.translate("MainWindow", "Select", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("MainWindow", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.uiACT_refresh.setText(QtGui.QApplication.translate("MainWindow", "Refresh", None, QtGui.QApplication.UnicodeUTF8))
        self.uiACT_refresh.setToolTip(QtGui.QApplication.translate("MainWindow", "Refresh", None, QtGui.QApplication.UnicodeUTF8))
        self.uiACT_refresh.setShortcut(QtGui.QApplication.translate("MainWindow", "F5", None, QtGui.QApplication.UnicodeUTF8))
        self.uiACT_exit.setText(QtGui.QApplication.translate("MainWindow", "Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.uiACT_retarget.setText(QtGui.QApplication.translate("MainWindow", "Retarget", None, QtGui.QApplication.UnicodeUTF8))
        self.uiACT_copyMove.setText(QtGui.QApplication.translate("MainWindow", "Copy/Move", None, QtGui.QApplication.UnicodeUTF8))
        self.uiACT_searchReplace.setText(QtGui.QApplication.translate("MainWindow", "Search and Replace", None, QtGui.QApplication.UnicodeUTF8))
        self.uiACT_copyFullPath.setText(QtGui.QApplication.translate("MainWindow", "Copy Full Path", None, QtGui.QApplication.UnicodeUTF8))
        self.uiACT_copyFilename.setText(QtGui.QApplication.translate("MainWindow", "Copy Filename", None, QtGui.QApplication.UnicodeUTF8))
        self.uiACT_selectAssigned.setText(QtGui.QApplication.translate("MainWindow", "Select Assigned", None, QtGui.QApplication.UnicodeUTF8))
        self.uiACT_removeDuplicatesFromClipboard.setText(QtGui.QApplication.translate("MainWindow", "Remove Duplicates From Clipboard", None, QtGui.QApplication.UnicodeUTF8))
        self.uiACT_selectAll.setText(QtGui.QApplication.translate("MainWindow", "Select All", None, QtGui.QApplication.UnicodeUTF8))
        self.uiACT_selectNone.setText(QtGui.QApplication.translate("MainWindow", "Select None", None, QtGui.QApplication.UnicodeUTF8))
        self.uiACT_selectInvert.setText(QtGui.QApplication.translate("MainWindow", "Select Invert", None, QtGui.QApplication.UnicodeUTF8))

import resources_rc
