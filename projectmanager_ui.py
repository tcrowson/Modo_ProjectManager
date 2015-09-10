# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file ...
#
# Created: Fri May 08 16:50:11 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_projectManager(object):
    def setupUi(self, projectManager):
        projectManager.setObjectName("projectManager")
        projectManager.resize(796, 537)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/tree.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        projectManager.setWindowIcon(icon)
        projectManager.setStyleSheet("QWidget{\n"
"  dialogbuttonbox-buttons-have-icons: 0;\n"
"  combobox-popup: 1;\n"
"  tabbar-prefer-no-arrows: true;\n"
"  color: #cccccc;\n"
"  background-color: #484848;\n"
"}\n"
"\n"
"\n"
"QMenuBar{\n"
"  background-color: #484848;\n"
"border-bottom: 1px solid #282828;\n"
"}\n"
"\n"
"\n"
"QMenuBar::item{\n"
"  background: transparent;\n"
"}\n"
"\n"
"\n"
"\n"
"QMenuBar::item:selected{\n"
"  background: transparent;\n"
"  color:#f49c1c ;\n"
"  border: 1px solid #f49c1c;\n"
"}\n"
"\n"
"\n"
"QMenuBar::item:pressed{\n"
"  background: #545454;\n"
"  border: 1px solid #000;\n"
"  margin-bottom:-1px;\n"
"  padding-bottom:1px;\n"
"}\n"
"\n"
"\n"
"QMenu{\n"
"  border: 1px solid #000;\n"
"background: #484848;\n"
"padding:5px;\n"
"}\n"
"\n"
"QMenu::separator{\n"
"height: 1px;\n"
"background-color: #303030;\n"
"}\n"
"\n"
"\n"
"QMenu::item{\n"
"  padding: 2px 20px 2px 20px;\n"
"background: #484848;\n"
"}\n"
"\n"
"\n"
"QMenu::item:selected{\n"
"  color: #f89a2b;\n"
" background: #545454;\n"
"}\n"
"\n"
"QGroupBox{\n"
"border: 1px solid #696969;\n"
"border-radius:6px;\n"
"margin-top: 5px;\n"
"}\n"
"\n"
"QGroupBox::title{\n"
"margin-top: -12px;\n"
"}\n"
"\n"
"\n"
"QToolTip\n"
"{\n"
"  border: 1px solid black;\n"
"  background-color: #f0f0b4;\n"
"  color: #000000;\n"
"  border-radius: 3px;\n"
"  opacity: 220;\n"
"}\n"
"\n"
"QLabel{\n"
"background: none;\n"
"color: #919191;\n"
"}\n"
"\n"
"QLineEdit\n"
"{\n"
"  color: #000000;\n"
"  background-color: #9098a0;\n"
"  padding: 1px;\n"
"  border-style: solid;\n"
"  border: 1px solid #353535;\n"
"  border-radius: 6px;\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton\n"
"{\n"
"  icon-size: 12px;\n"
"  background-color: #606060;\n"
"  border-width: 1px;\n"
"  border-color: #353535;\n"
"  border-style: solid;\n"
"  border-radius: 6px;\n"
"  padding: 5px;\n"
"  padding-left: 2px;\n"
"  padding-right: 2px;\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"  border: none;\n"
"  background-color: none;\n"
"}\n"
"\n"
"QPushButton:disabled\n"
"{\n"
"border: 1px solid #4A4A4A;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover\n"
"{\n"
"  background-color: #686868;\n"
"}\n"
"\n"
"QPushButton:pressed,QPushButton:focus:pressed\n"
"{\n"
"  color: #000;\n"
"  background-color: #f89a2b;\n"
"}\n"
"\n"
"\n"
"\n"
"QScrollBar:horizontal {\n"
"  background: #404040;\n"
"  height: 16px;\n"
"  margin: 0 -2px 0 -2px;\n"
"  border: 1px solid #383838;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"  background: none;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"  border-radius: 0px;\n"
"  border: none;\n"
"  width: 0px;\n"
"  subcontrol-position: left;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"  border-radius: 0px;\n"
"  border: none;\n"
"  width: 0px;\n"
"  subcontrol-position: left;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"/*\n"
"QScrollBar::right-arrow:horizontal, QScrollBar::left-arrow:horizontal\n"
"{\n"
"  border: 1px solid black;\n"
"  width: 1px;\n"
"  height: 1px;\n"
"  background: white;\n"
"}\n"
"*/\n"
"\n"
"\n"
"\n"
"\n"
"QScrollBar:vertical\n"
"{\n"
"  background: #404040;\n"
"  width: 16px;\n"
"  margin: -2px 0 -2px 0;\n"
"  border: 1px solid #383838;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical\n"
"{\n"
"  border-radius: 2px;\n"
"  border: 1px solid #383838;\n"
"  height: 0px;\n"
"  subcontrol-position: bottom;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical\n"
"{\n"
"  border-radius: 2px;\n"
"  border: 1px solid #383838;\n"
"  height: 0px;\n"
"  subcontrol-position: top;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"/*\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical\n"
"{\n"
"  border: 1px solid black;\n"
"  width: 1px;\n"
"  height: 1px;\n"
"  background: white;\n"
"}\n"
"*/\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
"{\n"
"  background: none;\n"
"}\n"
"\n"
"\n"
"QTreeView {\n"
"  color: #000000;\n"
"  background-color: #9098a0;\n"
"  alternate-background-color: #9098a0;\n"
"/*\n"
"  padding-top: 6px;\n"
"  padding-bottom: 6px;\n"
"  border-radius: 6px;\n"
"*/\n"
"  border-style: solid;\n"
"  border-width: 1px;\n"
"  border-color: #282828;\n"
"}\n"
"\n"
"\n"
" QTreeView::item:hover {\n"
"background-color: #A2A9B0;\n"
" }\n"
"\n"
" QTreeView::item:selected {\n"
"background-color: #B5BCC4;\n"
"color: black;\n"
" }\n"
"\n"
"\n"
"QHeaderView:section {\n"
"min-height: 18px;\n"
"  background-color: #64707c;\n"
"  color: #bbbbbb;\n"
"  padding-left: 4px;\n"
"  border: 1px solid #44505c;\n"
"border-top: none;\n"
"border-left: none;\n"
"}\n"
"\n"
"\n"
"\n"
"QHeaderView::section:last{\n"
"\n"
"border-right:none;\n"
"}\n"
"\n"
"/*\n"
"QHeaderView::down-arrow {\n"
"  image: url(down_arrow.png);\n"
"}\n"
"\n"
"QHeaderView::up-arrow {\n"
"  image: url(up_arrow.png);\n"
"}\n"
"*/\n"
"\n"
"\n"
"\n"
"")
        self.centralwidget = QtGui.QWidget(projectManager)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.gridLayout.setObjectName("gridLayout")
        self.togglePathsCheckBox = QtGui.QCheckBox(self.centralwidget)
        self.togglePathsCheckBox.setMinimumSize(QtCore.QSize(0, 20))
        self.togglePathsCheckBox.setMaximumSize(QtCore.QSize(16777215, 20))
        self.togglePathsCheckBox.setObjectName("togglePathsCheckBox")
        self.gridLayout.addWidget(self.togglePathsCheckBox, 0, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(583, 17, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        self.filtersBtn = QtGui.QToolButton(self.centralwidget)
        self.filtersBtn.setMinimumSize(QtCore.QSize(106, 20))
        self.filtersBtn.setMaximumSize(QtCore.QSize(120, 20))
        self.filtersBtn.setStyleSheet("\n"
"QToolButton\n"
"{\n"
"min-width: 100px;\n"
"  icon-size: 12px;\n"
"  background-color: #606060;\n"
"  border-width: 1px;\n"
"  border-color: #353535;\n"
"  border-style: solid;\n"
"  border-radius: 6px;\n"
"  padding: 2px;\n"
"  padding-left: 2px;\n"
"  padding-right: 2px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"min-width: 100px;\n"
"  border: none;\n"
"  background-color: none;\n"
"}\n"
"\n"
"QToolButton:hover\n"
"{\n"
"min-width: 100px;\n"
"  background-color: #686868;\n"
"}\n"
"\n"
"QToolButton:pressed,QToolButton:focus:pressed\n"
"{\n"
"min-width: 100px;\n"
"  color: #000;\n"
"  background-color: #f89a2b;\n"
"}\n"
"")
        self.filtersBtn.setCheckable(False)
        self.filtersBtn.setPopupMode(QtGui.QToolButton.InstantPopup)
        self.filtersBtn.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.filtersBtn.setObjectName("filtersBtn")
        self.gridLayout.addWidget(self.filtersBtn, 0, 2, 1, 1)
        self.projectsSplitter = QtGui.QSplitter(self.centralwidget)
        self.projectsSplitter.setOrientation(QtCore.Qt.Horizontal)
        self.projectsSplitter.setObjectName("projectsSplitter")
        self.projectTree = QtGui.QTreeWidget(self.projectsSplitter)
        self.projectTree.setFocusPolicy(QtCore.Qt.NoFocus)
        self.projectTree.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.projectTree.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.projectTree.setAlternatingRowColors(True)
        self.projectTree.setIndentation(5)
        self.projectTree.setRootIsDecorated(False)
        self.projectTree.setUniformRowHeights(False)
        self.projectTree.setItemsExpandable(False)
        self.projectTree.setHeaderHidden(False)
        self.projectTree.setExpandsOnDoubleClick(False)
        self.projectTree.setObjectName("projectTree")
        self.projectTree.header().setVisible(True)
        self.projectTree.header().setDefaultSectionSize(200)
        self.projectTree.header().setMinimumSectionSize(25)
        self.projectTree.header().setSortIndicatorShown(False)
        self.sceneTree = QtGui.QTreeWidget(self.projectsSplitter)
        self.sceneTree.setMinimumSize(QtCore.QSize(0, 0))
        self.sceneTree.setFocusPolicy(QtCore.Qt.NoFocus)
        self.sceneTree.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.sceneTree.setIndentation(5)
        self.sceneTree.setRootIsDecorated(False)
        self.sceneTree.setHeaderHidden(False)
        self.sceneTree.setExpandsOnDoubleClick(False)
        self.sceneTree.setObjectName("sceneTree")
        self.sceneTree.header().setVisible(True)
        self.sceneTree.header().setDefaultSectionSize(200)
        self.gridLayout.addWidget(self.projectsSplitter, 1, 0, 1, 3)
        projectManager.setCentralWidget(self.centralwidget)
        self.menuBar = QtGui.QMenuBar(projectManager)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 796, 21))
        self.menuBar.setNativeMenuBar(True)
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtGui.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        self.menuScenes = QtGui.QMenu(self.menuBar)
        self.menuScenes.setObjectName("menuScenes")
        self.menuHelp = QtGui.QMenu(self.menuBar)
        self.menuHelp.setObjectName("menuHelp")
        projectManager.setMenuBar(self.menuBar)
        self.act_addExisting = QtGui.QAction(projectManager)
        self.act_addExisting.setObjectName("act_addExisting")
        self.act_removeSelected = QtGui.QAction(projectManager)
        self.act_removeSelected.setObjectName("act_removeSelected")
        self.act_setAsCurrent = QtGui.QAction(projectManager)
        self.act_setAsCurrent.setObjectName("act_setAsCurrent")
        self.act_openSelectedScene = QtGui.QAction(projectManager)
        self.act_openSelectedScene.setObjectName("act_openSelectedScene")
        self.act_importSelectedScene = QtGui.QAction(projectManager)
        self.act_importSelectedScene.setObjectName("act_importSelectedScene")
        self.act_importSelectedAsRef = QtGui.QAction(projectManager)
        self.act_importSelectedAsRef.setObjectName("act_importSelectedAsRef")
        self.act_about = QtGui.QAction(projectManager)
        self.act_about.setObjectName("act_about")
        self.act_docs = QtGui.QAction(projectManager)
        self.act_docs.setObjectName("act_docs")
        self.act_exploreProject = QtGui.QAction(projectManager)
        self.act_exploreProject.setObjectName("act_exploreProject")
        self.act_exploreSceneFolder = QtGui.QAction(projectManager)
        self.act_exploreSceneFolder.setObjectName("act_exploreSceneFolder")
        self.act_newProject = QtGui.QAction(projectManager)
        self.act_newProject.setObjectName("act_newProject")
        self.menuFile.addAction(self.act_newProject)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.act_setAsCurrent)
        self.menuFile.addAction(self.act_exploreProject)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.act_addExisting)
        self.menuFile.addAction(self.act_removeSelected)
        self.menuScenes.addAction(self.act_openSelectedScene)
        self.menuScenes.addAction(self.act_importSelectedScene)
        self.menuScenes.addAction(self.act_importSelectedAsRef)
        self.menuScenes.addAction(self.act_exploreSceneFolder)
        self.menuHelp.addAction(self.act_docs)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuScenes.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(projectManager)
        QtCore.QMetaObject.connectSlotsByName(projectManager)

    def retranslateUi(self, projectManager):
        projectManager.setWindowTitle(QtGui.QApplication.translate("projectManager", "Project Manager", None, QtGui.QApplication.UnicodeUTF8))
        self.togglePathsCheckBox.setToolTip(QtGui.QApplication.translate("projectManager", "Toggle the display of project and scene paths in the lists", None, QtGui.QApplication.UnicodeUTF8))
        self.togglePathsCheckBox.setText(QtGui.QApplication.translate("projectManager", "Show Paths", None, QtGui.QApplication.UnicodeUTF8))
        self.filtersBtn.setToolTip(QtGui.QApplication.translate("projectManager", "Choose which filetypes to display in the Scene List", None, QtGui.QApplication.UnicodeUTF8))
        self.filtersBtn.setText(QtGui.QApplication.translate("projectManager", "Show filetypes...", None, QtGui.QApplication.UnicodeUTF8))
        self.projectTree.setToolTip(QtGui.QApplication.translate("projectManager", "The Project List", None, QtGui.QApplication.UnicodeUTF8))
        self.projectTree.headerItem().setText(0, QtGui.QApplication.translate("projectManager", "Project", None, QtGui.QApplication.UnicodeUTF8))
        self.projectTree.headerItem().setText(1, QtGui.QApplication.translate("projectManager", "Path", None, QtGui.QApplication.UnicodeUTF8))
        self.sceneTree.setToolTip(QtGui.QApplication.translate("projectManager", "The Scene List", None, QtGui.QApplication.UnicodeUTF8))
        self.sceneTree.headerItem().setText(0, QtGui.QApplication.translate("projectManager", "Scene", None, QtGui.QApplication.UnicodeUTF8))
        self.sceneTree.headerItem().setText(1, QtGui.QApplication.translate("projectManager", "Path", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("projectManager", "Projects", None, QtGui.QApplication.UnicodeUTF8))
        self.menuScenes.setTitle(QtGui.QApplication.translate("projectManager", "Scenes", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("projectManager", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.act_addExisting.setText(QtGui.QApplication.translate("projectManager", "Add Existing Project to List...", None, QtGui.QApplication.UnicodeUTF8))
        self.act_removeSelected.setText(QtGui.QApplication.translate("projectManager", "Remove Selected from List", None, QtGui.QApplication.UnicodeUTF8))
        self.act_setAsCurrent.setText(QtGui.QApplication.translate("projectManager", "Set Selected As Current", None, QtGui.QApplication.UnicodeUTF8))
        self.act_openSelectedScene.setText(QtGui.QApplication.translate("projectManager", "Open Selected Scene", None, QtGui.QApplication.UnicodeUTF8))
        self.act_importSelectedScene.setText(QtGui.QApplication.translate("projectManager", "Import Selected Scene", None, QtGui.QApplication.UnicodeUTF8))
        self.act_importSelectedAsRef.setText(QtGui.QApplication.translate("projectManager", "Import Selected as Referenced", None, QtGui.QApplication.UnicodeUTF8))
        self.act_about.setText(QtGui.QApplication.translate("projectManager", "About...", None, QtGui.QApplication.UnicodeUTF8))
        self.act_docs.setText(QtGui.QApplication.translate("projectManager", "Documentation", None, QtGui.QApplication.UnicodeUTF8))
        self.act_exploreProject.setText(QtGui.QApplication.translate("projectManager", "Open Project Folder...", None, QtGui.QApplication.UnicodeUTF8))
        self.act_exploreProject.setToolTip(QtGui.QApplication.translate("projectManager", "Open Project Folder", None, QtGui.QApplication.UnicodeUTF8))
        self.act_exploreSceneFolder.setText(QtGui.QApplication.translate("projectManager", "Open Scene Folder...", None, QtGui.QApplication.UnicodeUTF8))
        self.act_exploreSceneFolder.setToolTip(QtGui.QApplication.translate("projectManager", "Open Containing Folder", None, QtGui.QApplication.UnicodeUTF8))
        self.act_newProject.setText(QtGui.QApplication.translate("projectManager", "New Project...", None, QtGui.QApplication.UnicodeUTF8))
        self.act_newProject.setToolTip(QtGui.QApplication.translate("projectManager", "Create a new project", None, QtGui.QApplication.UnicodeUTF8))

