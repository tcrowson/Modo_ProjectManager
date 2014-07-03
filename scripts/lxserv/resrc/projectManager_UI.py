# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'projectManager.ui'
#
# Created: Thu Jul  3 13:20:10 2014
#      by: pyside-uic 0.2.13 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_projectManager(object):
    def setupUi(self, projectManager):
        projectManager.setObjectName("projectManager")
        projectManager.resize(936, 544)
        projectManager.setStyleSheet("QWidget{\n"
"  dialogbuttonbox-buttons-have-icons: 0;\n"
"  combobox-popup: 1;\n"
"  tabbar-prefer-no-arrows: true;\n"
"  color: #cccccc;\n"
"  background-color: #303030;\n"
"}\n"
"\n"
"\n"
"QMenuBar{\n"
"  background-color: QLinearGradient(\n"
"      x1:0, y1:0,\n"
"      x2:0, y2:1,\n"
"      stop:1 #484848,\n"
"      stop:0.4 #666666);\n"
"}\n"
"\n"
"QMenu::separator{\n"
"height: 1px;\n"
"background-color: #303030;\n"
"}\n"
"\n"
"QMenuBar::item{\n"
"  background: transparent;\n"
"}\n"
"\n"
"\n"
"QMenuBar::item:selected{\n"
"  background: transparent;\n"
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
"\n"
"")
        self.centralwidget = QtGui.QWidget(projectManager)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_7 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_7.setContentsMargins(4, 4, 4, 4)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet("QWidget\n"
"{\n"
"  dialogbuttonbox-buttons-have-icons: 0;\n"
"  combobox-popup: 1;\n"
"  tabbar-prefer-no-arrows: true;\n"
"  color: #cccccc;\n"
"  background-color: #484848;\n"
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
"QComboBox\n"
"{\n"
"  combobox-popup: 1;\n"
"  selection-background-color: #666666;\n"
"  selection-color: #f89a2b;;\n"
"  background-color: #606060;\n"
"  border-style: solid;\n"
"  border: 1px solid #1e1e1e;\n"
"  border-radius: 6px;\n"
"  padding-left: 6px;\n"
"}\n"
"\n"
"  \n"
"QComboBox:hover,QPushButton:hover\n"
"{\n"
"  background-color: #6c6c6c;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView\n"
"{\n"
"\n"
"  background-color: #545454;\n"
"  border-width: 0px;\n"
"  border-radius: 0px;\n"
"  selection-background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"  padding-top: 10px;\n"
"  padding-bottom: 10px;\n"
"  padding-left: 2px;\n"
"  padding-right: 2px;\n"
"border: 1px solid #1e1e1e;\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"  subcontrol-origin: padding;\n"
"  subcontrol-position: top right;\n"
"  width: 25px;\n"
"  border-left-width: 0px;\n"
"  border-left-color: darkgray;\n"
"  border-left-style: solid;\n"
"  border-top-right-radius: 3px;\n"
"  border-bottom-right-radius: 3px;\n"
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
"QTabWidget:pane{\n"
"}\n"
"\n"
"\n"
"QTabBar {\n"
"background: none;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"min-width: 100px;\n"
"max-width:100px;\n"
"  color: #c0c0c0;\n"
"  border-width: 1px;\n"
"  border-color: #484848;\n"
"  border-left-style: solid;\n"
"  border-right-style: solid;\n"
"  border-top-style: solid;\n"
"  border-bottom-style: none;\n"
"  border-style: none;\n"
"  border-top-left-radius: 6px;\n"
"  border-top-right-radius: 6px;\n"
"  padding-left: 10px;\n"
"  padding-right: 10px;\n"
"  padding-top: 3px;\n"
"  padding-bottom: 2px;\n"
"  margin-left: 0px;\n"
"  margin-right: 2px;\n"
"  margin-top: 3px;\n"
"  background-color: QLinearGradient(\n"
"      x1:0, y1:0,\n"
"      x2:0, y2:1,\n"
"      stop:1 #484848,\n"
"      stop:0.4 #565656);\n"
"}\n"
"\n"
"\n"
"QTabWidget::right-corner {\n"
"  background-color: #28ff28;\n"
"}\n"
"\n"
"QTabBar::tab:last\n"
"{\n"
"  margin-right: 0;\n"
"}\n"
"\n"
"QTabBar::tab:first:!selected\n"
"{\n"
"  margin-left: 0px;\n"
"}\n"
"\n"
"QTabBar::tab:!selected\n"
"{\n"
"margin-top: 5px;\n"
"  color: #787878;\n"
"  border-bottom-style: none;\n"
"  background-color: QLinearGradient(\n"
"      x1:0, y1:0,\n"
"      x2:0, y2:1,\n"
"      stop:1 #353535,\n"
"      stop:0.4 #404040);\n"
"}\n"
"\n"
"QTabBar::tab:selected\n"
"{\n"
"\n"
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
"border-radius: 6px;\n"
"}\n"
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
"\n"
"\n"
"\n"
"QListView {\n"
"border-radius: 6px;\n"
"  color: #000000;\n"
"  background-color: #949ca4;\n"
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
"QHeaderView::section:first{\n"
"border-top-left-radius: 6px;\n"
"}\n"
"\n"
"QHeaderView::section:last{\n"
"border-top-right-radius: 6px;\n"
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
"")
        self.tabWidget.setObjectName("tabWidget")
        self.existingProjectsTab = QtGui.QWidget()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.existingProjectsTab.sizePolicy().hasHeightForWidth())
        self.existingProjectsTab.setSizePolicy(sizePolicy)
        self.existingProjectsTab.setCursor(QtCore.Qt.ArrowCursor)
        self.existingProjectsTab.setStyleSheet("")
        self.existingProjectsTab.setObjectName("existingProjectsTab")
        self.gridLayout_5 = QtGui.QGridLayout(self.existingProjectsTab)
        self.gridLayout_5.setContentsMargins(3, 3, 3, 3)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.existingProjectsSplitter = QtGui.QSplitter(self.existingProjectsTab)
        self.existingProjectsSplitter.setOrientation(QtCore.Qt.Horizontal)
        self.existingProjectsSplitter.setObjectName("existingProjectsSplitter")
        self.layoutWidget = QtGui.QWidget(self.existingProjectsSplitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.projectTreeGridLayout = QtGui.QGridLayout(self.layoutWidget)
        self.projectTreeGridLayout.setContentsMargins(0, 0, 0, 0)
        self.projectTreeGridLayout.setVerticalSpacing(1)
        self.projectTreeGridLayout.setObjectName("projectTreeGridLayout")
        spacerItem = QtGui.QSpacerItem(178, 21, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.projectTreeGridLayout.addItem(spacerItem, 0, 1, 1, 1)
        self.projectTree = QtGui.QTreeWidget(self.layoutWidget)
        self.projectTree.setFocusPolicy(QtCore.Qt.NoFocus)
        self.projectTree.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.projectTree.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.projectTree.setAlternatingRowColors(True)
        self.projectTree.setIndentation(5)
        self.projectTree.setRootIsDecorated(False)
        self.projectTree.setUniformRowHeights(False)
        self.projectTree.setItemsExpandable(False)
        self.projectTree.setExpandsOnDoubleClick(False)
        self.projectTree.setObjectName("projectTree")
        item_0 = QtGui.QTreeWidgetItem(self.projectTree)
        item_0 = QtGui.QTreeWidgetItem(self.projectTree)
        self.projectTree.header().setVisible(False)
        self.projectTree.header().setDefaultSectionSize(200)
        self.projectTree.header().setMinimumSectionSize(25)
        self.projectTree.header().setSortIndicatorShown(False)
        self.projectTreeGridLayout.addWidget(self.projectTree, 1, 0, 1, 2)
        self.layoutWidget1 = QtGui.QWidget(self.existingProjectsSplitter)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout_4 = QtGui.QGridLayout(self.layoutWidget1)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setVerticalSpacing(1)
        self.gridLayout_4.setObjectName("gridLayout_4")
        spacerItem1 = QtGui.QSpacerItem(138, 10, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem1, 0, 1, 1, 1)
        self.fileTypeLabel = QtGui.QLabel(self.layoutWidget1)
        self.fileTypeLabel.setStyleSheet("")
        self.fileTypeLabel.setObjectName("fileTypeLabel")
        self.gridLayout_4.addWidget(self.fileTypeLabel, 0, 2, 1, 1)
        self.fileTypeCbx = QtGui.QComboBox(self.layoutWidget1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fileTypeCbx.sizePolicy().hasHeightForWidth())
        self.fileTypeCbx.setSizePolicy(sizePolicy)
        self.fileTypeCbx.setMinimumSize(QtCore.QSize(100, 20))
        self.fileTypeCbx.setMaximumSize(QtCore.QSize(16777215, 90))
        self.fileTypeCbx.setMouseTracking(False)
        self.fileTypeCbx.setFocusPolicy(QtCore.Qt.NoFocus)
        self.fileTypeCbx.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.fileTypeCbx.setStyleSheet("min-height: 18px;")
        self.fileTypeCbx.setMaxVisibleItems(15)
        self.fileTypeCbx.setObjectName("fileTypeCbx")
        self.fileTypeCbx.addItem("")
        self.fileTypeCbx.addItem("")
        self.fileTypeCbx.addItem("")
        self.fileTypeCbx.addItem("")
        self.fileTypeCbx.addItem("")
        self.fileTypeCbx.addItem("")
        self.fileTypeCbx.addItem("")
        self.fileTypeCbx.addItem("")
        self.fileTypeCbx.addItem("")
        self.fileTypeCbx.addItem("")
        self.fileTypeCbx.addItem("")
        self.fileTypeCbx.addItem("")
        self.fileTypeCbx.addItem("")
        self.fileTypeCbx.addItem("")
        self.gridLayout_4.addWidget(self.fileTypeCbx, 0, 3, 1, 1)
        self.sceneTree = QtGui.QTreeWidget(self.layoutWidget1)
        self.sceneTree.setFocusPolicy(QtCore.Qt.NoFocus)
        self.sceneTree.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.sceneTree.setIndentation(5)
        self.sceneTree.setRootIsDecorated(False)
        self.sceneTree.setExpandsOnDoubleClick(False)
        self.sceneTree.setObjectName("sceneTree")
        self.sceneTree.header().setVisible(False)
        self.sceneTree.header().setDefaultSectionSize(200)
        self.gridLayout_4.addWidget(self.sceneTree, 1, 0, 1, 4)
        self.gridLayout_5.addWidget(self.existingProjectsSplitter, 0, 0, 1, 1)
        self.tabWidget.addTab(self.existingProjectsTab, "")
        self.newProjectTab = QtGui.QWidget()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.newProjectTab.sizePolicy().hasHeightForWidth())
        self.newProjectTab.setSizePolicy(sizePolicy)
        self.newProjectTab.setObjectName("newProjectTab")
        self.gridLayout_3 = QtGui.QGridLayout(self.newProjectTab)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.projectLocationGroup = QtGui.QGroupBox(self.newProjectTab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.projectLocationGroup.sizePolicy().hasHeightForWidth())
        self.projectLocationGroup.setSizePolicy(sizePolicy)
        self.projectLocationGroup.setMinimumSize(QtCore.QSize(0, 45))
        self.projectLocationGroup.setMaximumSize(QtCore.QSize(16777215, 45))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.projectLocationGroup.setFont(font)
        self.projectLocationGroup.setObjectName("projectLocationGroup")
        self.gridLayout_2 = QtGui.QGridLayout(self.projectLocationGroup)
        self.gridLayout_2.setContentsMargins(-1, 4, 7, 4)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.newProjectPathLabel = QtGui.QLabel(self.projectLocationGroup)
        self.newProjectPathLabel.setMinimumSize(QtCore.QSize(85, 0))
        self.newProjectPathLabel.setMaximumSize(QtCore.QSize(85, 16777215))
        self.newProjectPathLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.newProjectPathLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.newProjectPathLabel.setObjectName("newProjectPathLabel")
        self.gridLayout_2.addWidget(self.newProjectPathLabel, 0, 0, 1, 1)
        self.newProjectPathBtn = QtGui.QPushButton(self.projectLocationGroup)
        self.newProjectPathBtn.setMinimumSize(QtCore.QSize(51, 20))
        self.newProjectPathBtn.setMaximumSize(QtCore.QSize(30, 20))
        self.newProjectPathBtn.setStyleSheet("min-width: 45px;")
        self.newProjectPathBtn.setObjectName("newProjectPathBtn")
        self.gridLayout_2.addWidget(self.newProjectPathBtn, 0, 2, 1, 1)
        self.newProjectPath = QtGui.QLineEdit(self.projectLocationGroup)
        self.newProjectPath.setMinimumSize(QtCore.QSize(0, 20))
        self.newProjectPath.setMaximumSize(QtCore.QSize(16777215, 20))
        self.newProjectPath.setText("")
        self.newProjectPath.setObjectName("newProjectPath")
        self.gridLayout_2.addWidget(self.newProjectPath, 0, 1, 1, 1)
        self.gridLayout_3.addWidget(self.projectLocationGroup, 0, 0, 1, 1)
        self.rootFoldersGroup = QtGui.QGroupBox(self.newProjectTab)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.rootFoldersGroup.setFont(font)
        self.rootFoldersGroup.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.rootFoldersGroup.setStyleSheet("")
        self.rootFoldersGroup.setObjectName("rootFoldersGroup")
        self.gridLayout = QtGui.QGridLayout(self.rootFoldersGroup)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem2 = QtGui.QSpacerItem(85, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 0, 0, 1, 1)
        self.createFoldersCheckBox = QtGui.QCheckBox(self.rootFoldersGroup)
        self.createFoldersCheckBox.setObjectName("createFoldersCheckBox")
        self.gridLayout.addWidget(self.createFoldersCheckBox, 0, 1, 1, 1)
        self.folderTemplateLabel = QtGui.QLabel(self.rootFoldersGroup)
        self.folderTemplateLabel.setMinimumSize(QtCore.QSize(85, 0))
        self.folderTemplateLabel.setMaximumSize(QtCore.QSize(80, 16777215))
        self.folderTemplateLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.folderTemplateLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.folderTemplateLabel.setObjectName("folderTemplateLabel")
        self.gridLayout.addWidget(self.folderTemplateLabel, 1, 0, 1, 1)
        self.templateCbx = QtGui.QComboBox(self.rootFoldersGroup)
        self.templateCbx.setMinimumSize(QtCore.QSize(0, 20))
        self.templateCbx.setMaximumSize(QtCore.QSize(16777215, 20))
        self.templateCbx.setObjectName("templateCbx")
        self.templateCbx.addItem("")
        self.gridLayout.addWidget(self.templateCbx, 1, 1, 1, 1)
        self.newTemplateBtn = QtGui.QPushButton(self.rootFoldersGroup)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.newTemplateBtn.sizePolicy().hasHeightForWidth())
        self.newTemplateBtn.setSizePolicy(sizePolicy)
        self.newTemplateBtn.setMinimumSize(QtCore.QSize(0, 20))
        self.newTemplateBtn.setMaximumSize(QtCore.QSize(32, 24))
        self.newTemplateBtn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/newTemplate.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.newTemplateBtn.setIcon(icon)
        self.newTemplateBtn.setIconSize(QtCore.QSize(24, 24))
        self.newTemplateBtn.setObjectName("newTemplateBtn")
        self.gridLayout.addWidget(self.newTemplateBtn, 1, 2, 1, 1)
        self.scenesRootLabel_2 = QtGui.QLabel(self.rootFoldersGroup)
        self.scenesRootLabel_2.setMinimumSize(QtCore.QSize(85, 0))
        self.scenesRootLabel_2.setMaximumSize(QtCore.QSize(80, 16777215))
        self.scenesRootLabel_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.scenesRootLabel_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.scenesRootLabel_2.setObjectName("scenesRootLabel_2")
        self.gridLayout.addWidget(self.scenesRootLabel_2, 2, 0, 1, 1)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.addFolderBtn = QtGui.QPushButton(self.rootFoldersGroup)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addFolderBtn.sizePolicy().hasHeightForWidth())
        self.addFolderBtn.setSizePolicy(sizePolicy)
        self.addFolderBtn.setMaximumSize(QtCore.QSize(32, 32))
        self.addFolderBtn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/addFolder.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addFolderBtn.setIcon(icon1)
        self.addFolderBtn.setIconSize(QtCore.QSize(26, 26))
        self.addFolderBtn.setObjectName("addFolderBtn")
        self.verticalLayout.addWidget(self.addFolderBtn)
        self.delFolderBtn = QtGui.QPushButton(self.rootFoldersGroup)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.delFolderBtn.sizePolicy().hasHeightForWidth())
        self.delFolderBtn.setSizePolicy(sizePolicy)
        self.delFolderBtn.setMaximumSize(QtCore.QSize(32, 32))
        self.delFolderBtn.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/removeFolder.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.delFolderBtn.setIcon(icon2)
        self.delFolderBtn.setIconSize(QtCore.QSize(26, 26))
        self.delFolderBtn.setObjectName("delFolderBtn")
        self.verticalLayout.addWidget(self.delFolderBtn)
        self.resetTreeBtn = QtGui.QPushButton(self.rootFoldersGroup)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.resetTreeBtn.sizePolicy().hasHeightForWidth())
        self.resetTreeBtn.setSizePolicy(sizePolicy)
        self.resetTreeBtn.setMaximumSize(QtCore.QSize(32, 32))
        self.resetTreeBtn.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/reset.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.resetTreeBtn.setIcon(icon3)
        self.resetTreeBtn.setIconSize(QtCore.QSize(26, 26))
        self.resetTreeBtn.setObjectName("resetTreeBtn")
        self.verticalLayout.addWidget(self.resetTreeBtn)
        self.saveTemplateBtn = QtGui.QPushButton(self.rootFoldersGroup)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.saveTemplateBtn.sizePolicy().hasHeightForWidth())
        self.saveTemplateBtn.setSizePolicy(sizePolicy)
        self.saveTemplateBtn.setMaximumSize(QtCore.QSize(32, 32))
        self.saveTemplateBtn.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icons/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.saveTemplateBtn.setIcon(icon4)
        self.saveTemplateBtn.setIconSize(QtCore.QSize(26, 26))
        self.saveTemplateBtn.setObjectName("saveTemplateBtn")
        self.verticalLayout.addWidget(self.saveTemplateBtn)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.gridLayout.addLayout(self.verticalLayout, 2, 2, 1, 1)
        self.folderTree = QtGui.QTreeWidget(self.rootFoldersGroup)
        self.folderTree.setFocusPolicy(QtCore.Qt.NoFocus)
        self.folderTree.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.folderTree.setDragEnabled(True)
        self.folderTree.setDragDropMode(QtGui.QAbstractItemView.InternalMove)
        self.folderTree.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.folderTree.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.folderTree.setAutoExpandDelay(0)
        self.folderTree.setIndentation(30)
        self.folderTree.setAnimated(True)
        self.folderTree.setHeaderHidden(True)
        self.folderTree.setExpandsOnDoubleClick(False)
        self.folderTree.setObjectName("folderTree")
        item_0 = QtGui.QTreeWidgetItem(self.folderTree)
        item_0 = QtGui.QTreeWidgetItem(self.folderTree)
        item_0 = QtGui.QTreeWidgetItem(self.folderTree)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_2 = QtGui.QTreeWidgetItem(item_1)
        self.folderTree.header().setVisible(False)
        self.gridLayout.addWidget(self.folderTree, 2, 1, 1, 1)
        self.gridLayout_3.addWidget(self.rootFoldersGroup, 1, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem4 = QtGui.QSpacerItem(223, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.createProjectBtn = QtGui.QPushButton(self.newProjectTab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.createProjectBtn.sizePolicy().hasHeightForWidth())
        self.createProjectBtn.setSizePolicy(sizePolicy)
        self.createProjectBtn.setMinimumSize(QtCore.QSize(150, 0))
        self.createProjectBtn.setObjectName("createProjectBtn")
        self.horizontalLayout.addWidget(self.createProjectBtn)
        spacerItem5 = QtGui.QSpacerItem(223, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.gridLayout_3.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        self.tabWidget.addTab(self.newProjectTab, "")
        self.gridLayout_7.addWidget(self.tabWidget, 0, 0, 1, 1)
        projectManager.setCentralWidget(self.centralwidget)
        self.menuBar = QtGui.QMenuBar(projectManager)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 936, 21))
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
        self.act_exportList = QtGui.QAction(projectManager)
        self.act_exportList.setObjectName("act_exportList")
        self.act_importList = QtGui.QAction(projectManager)
        self.act_importList.setObjectName("act_importList")
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
        self.menuFile.addAction(self.act_setAsCurrent)
        self.menuFile.addAction(self.act_exploreProject)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.act_addExisting)
        self.menuFile.addAction(self.act_removeSelected)
        self.menuFile.addAction(self.act_exportList)
        self.menuFile.addAction(self.act_importList)
        self.menuScenes.addAction(self.act_openSelectedScene)
        self.menuScenes.addAction(self.act_importSelectedScene)
        self.menuScenes.addAction(self.act_importSelectedAsRef)
        self.menuHelp.addAction(self.act_docs)
        self.menuHelp.addAction(self.act_about)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuScenes.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(projectManager)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(projectManager)

    def retranslateUi(self, projectManager):
        projectManager.setWindowTitle(QtGui.QApplication.translate("projectManager", "Project Manager", None, QtGui.QApplication.UnicodeUTF8))
        self.projectTree.headerItem().setText(0, QtGui.QApplication.translate("projectManager", "Project", None, QtGui.QApplication.UnicodeUTF8))
        self.projectTree.headerItem().setText(1, QtGui.QApplication.translate("projectManager", "Path", None, QtGui.QApplication.UnicodeUTF8))
        __sortingEnabled = self.projectTree.isSortingEnabled()
        self.projectTree.setSortingEnabled(False)
        self.projectTree.topLevelItem(0).setText(0, QtGui.QApplication.translate("projectManager", "projectName", None, QtGui.QApplication.UnicodeUTF8))
        self.projectTree.topLevelItem(0).setText(1, QtGui.QApplication.translate("projectManager", "path/to/this/project", None, QtGui.QApplication.UnicodeUTF8))
        self.projectTree.topLevelItem(1).setText(0, QtGui.QApplication.translate("projectManager", "projectName2", None, QtGui.QApplication.UnicodeUTF8))
        self.projectTree.topLevelItem(1).setText(1, QtGui.QApplication.translate("projectManager", "path/to/this/project", None, QtGui.QApplication.UnicodeUTF8))
        self.projectTree.setSortingEnabled(__sortingEnabled)
        self.fileTypeLabel.setText(QtGui.QApplication.translate("projectManager", "Scene Filter ", None, QtGui.QApplication.UnicodeUTF8))
        self.fileTypeCbx.setToolTip(QtGui.QApplication.translate("projectManager", "Choose which file type will be displayed in the Scenes list", None, QtGui.QApplication.UnicodeUTF8))
        self.fileTypeCbx.setItemText(0, QtGui.QApplication.translate("projectManager", "Modo (*.lxo)", None, QtGui.QApplication.UnicodeUTF8))
        self.fileTypeCbx.setItemText(1, QtGui.QApplication.translate("projectManager", "Preset (*.lxl)", None, QtGui.QApplication.UnicodeUTF8))
        self.fileTypeCbx.setItemText(2, QtGui.QApplication.translate("projectManager", "Lightwave (*.lwo)", None, QtGui.QApplication.UnicodeUTF8))
        self.fileTypeCbx.setItemText(3, QtGui.QApplication.translate("projectManager", "Wavefront (*.obj)", None, QtGui.QApplication.UnicodeUTF8))
        self.fileTypeCbx.setItemText(4, QtGui.QApplication.translate("projectManager", "Alembic (*.abc)", None, QtGui.QApplication.UnicodeUTF8))
        self.fileTypeCbx.setItemText(5, QtGui.QApplication.translate("projectManager", "Filmbox (*.fbx)", None, QtGui.QApplication.UnicodeUTF8))
        self.fileTypeCbx.setItemText(6, QtGui.QApplication.translate("projectManager", "Collada (*.dae)", None, QtGui.QApplication.UnicodeUTF8))
        self.fileTypeCbx.setItemText(7, QtGui.QApplication.translate("projectManager", "Rhino (*.3dm)", None, QtGui.QApplication.UnicodeUTF8))
        self.fileTypeCbx.setItemText(8, QtGui.QApplication.translate("projectManager", "Autodesk DXF (.*dxf)", None, QtGui.QApplication.UnicodeUTF8))
        self.fileTypeCbx.setItemText(9, QtGui.QApplication.translate("projectManager", "Adobe Illustrator (*.eps, *.ai)", None, QtGui.QApplication.UnicodeUTF8))
        self.fileTypeCbx.setItemText(10, QtGui.QApplication.translate("projectManager", "Stereolithography (*.stl)", None, QtGui.QApplication.UnicodeUTF8))
        self.fileTypeCbx.setItemText(11, QtGui.QApplication.translate("projectManager", "Videoscape (*.geo)", None, QtGui.QApplication.UnicodeUTF8))
        self.fileTypeCbx.setItemText(12, QtGui.QApplication.translate("projectManager", "Solidworks (*.sldprt, *.sldasm)", None, QtGui.QApplication.UnicodeUTF8))
        self.fileTypeCbx.setItemText(13, QtGui.QApplication.translate("projectManager", "Protein DB (*.pdb)", None, QtGui.QApplication.UnicodeUTF8))
        self.sceneTree.headerItem().setText(0, QtGui.QApplication.translate("projectManager", "Scene", None, QtGui.QApplication.UnicodeUTF8))
        self.sceneTree.headerItem().setText(1, QtGui.QApplication.translate("projectManager", "Path", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.existingProjectsTab), QtGui.QApplication.translate("projectManager", "Existing Projects", None, QtGui.QApplication.UnicodeUTF8))
        self.projectLocationGroup.setTitle(QtGui.QApplication.translate("projectManager", "Project Location", None, QtGui.QApplication.UnicodeUTF8))
        self.newProjectPathLabel.setText(QtGui.QApplication.translate("projectManager", "Root Path", None, QtGui.QApplication.UnicodeUTF8))
        self.newProjectPathBtn.setToolTip(QtGui.QApplication.translate("projectManager", "Browse for the location of your new project. The title of the project will be the directory you choose.", None, QtGui.QApplication.UnicodeUTF8))
        self.newProjectPathBtn.setText(QtGui.QApplication.translate("projectManager", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.newProjectPath.setToolTip(QtGui.QApplication.translate("projectManager", "This is the path where your new project will be created. The title of the project will be the name of root directory. ", None, QtGui.QApplication.UnicodeUTF8))
        self.rootFoldersGroup.setTitle(QtGui.QApplication.translate("projectManager", "Directory Structure", None, QtGui.QApplication.UnicodeUTF8))
        self.createFoldersCheckBox.setText(QtGui.QApplication.translate("projectManager", "Create Folders (EXPERIMENTAL)", None, QtGui.QApplication.UnicodeUTF8))
        self.folderTemplateLabel.setText(QtGui.QApplication.translate("projectManager", "Template", None, QtGui.QApplication.UnicodeUTF8))
        self.templateCbx.setItemText(0, QtGui.QApplication.translate("projectManager", "Modo Default", None, QtGui.QApplication.UnicodeUTF8))
        self.newTemplateBtn.setToolTip(QtGui.QApplication.translate("projectManager", "Create a new template", None, QtGui.QApplication.UnicodeUTF8))
        self.scenesRootLabel_2.setText(QtGui.QApplication.translate("projectManager", "Structure", None, QtGui.QApplication.UnicodeUTF8))
        self.addFolderBtn.setToolTip(QtGui.QApplication.translate("projectManager", "Add a new folder to the structure tree", None, QtGui.QApplication.UnicodeUTF8))
        self.delFolderBtn.setToolTip(QtGui.QApplication.translate("projectManager", "Remove the selected folder from the structure tree", None, QtGui.QApplication.UnicodeUTF8))
        self.resetTreeBtn.setToolTip(QtGui.QApplication.translate("projectManager", "Erase the structure tree", None, QtGui.QApplication.UnicodeUTF8))
        self.saveTemplateBtn.setToolTip(QtGui.QApplication.translate("projectManager", "Save the template", None, QtGui.QApplication.UnicodeUTF8))
        self.saveTemplateBtn.setShortcut(QtGui.QApplication.translate("projectManager", "Ctrl+R", None, QtGui.QApplication.UnicodeUTF8))
        self.folderTree.setSortingEnabled(False)
        self.folderTree.headerItem().setText(0, QtGui.QApplication.translate("projectManager", "Folders", None, QtGui.QApplication.UnicodeUTF8))
        __sortingEnabled = self.folderTree.isSortingEnabled()
        self.folderTree.setSortingEnabled(False)
        self.folderTree.topLevelItem(0).setText(0, QtGui.QApplication.translate("projectManager", "New Item", None, QtGui.QApplication.UnicodeUTF8))
        self.folderTree.topLevelItem(1).setText(0, QtGui.QApplication.translate("projectManager", "New Item", None, QtGui.QApplication.UnicodeUTF8))
        self.folderTree.topLevelItem(2).setText(0, QtGui.QApplication.translate("projectManager", "New Item", None, QtGui.QApplication.UnicodeUTF8))
        self.folderTree.topLevelItem(2).child(0).setText(0, QtGui.QApplication.translate("projectManager", "New Subitem", None, QtGui.QApplication.UnicodeUTF8))
        self.folderTree.topLevelItem(2).child(0).child(0).setText(0, QtGui.QApplication.translate("projectManager", "New Subitem", None, QtGui.QApplication.UnicodeUTF8))
        self.folderTree.setSortingEnabled(__sortingEnabled)
        self.createProjectBtn.setToolTip(QtGui.QApplication.translate("projectManager", "If you need a tooltip for this...", None, QtGui.QApplication.UnicodeUTF8))
        self.createProjectBtn.setText(QtGui.QApplication.translate("projectManager", "Create Project", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.newProjectTab), QtGui.QApplication.translate("projectManager", "New Project", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("projectManager", "Projects", None, QtGui.QApplication.UnicodeUTF8))
        self.menuScenes.setTitle(QtGui.QApplication.translate("projectManager", "Scenes", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("projectManager", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.act_addExisting.setText(QtGui.QApplication.translate("projectManager", "Add Existing Project To List", None, QtGui.QApplication.UnicodeUTF8))
        self.act_removeSelected.setText(QtGui.QApplication.translate("projectManager", "Remove Selected", None, QtGui.QApplication.UnicodeUTF8))
        self.act_exportList.setText(QtGui.QApplication.translate("projectManager", "Export List", None, QtGui.QApplication.UnicodeUTF8))
        self.act_importList.setText(QtGui.QApplication.translate("projectManager", "Import List", None, QtGui.QApplication.UnicodeUTF8))
        self.act_setAsCurrent.setText(QtGui.QApplication.translate("projectManager", "Set Selected As Current", None, QtGui.QApplication.UnicodeUTF8))
        self.act_openSelectedScene.setText(QtGui.QApplication.translate("projectManager", "Open Selected", None, QtGui.QApplication.UnicodeUTF8))
        self.act_importSelectedScene.setText(QtGui.QApplication.translate("projectManager", "Import Selected", None, QtGui.QApplication.UnicodeUTF8))
        self.act_importSelectedAsRef.setText(QtGui.QApplication.translate("projectManager", "Import Selected as Referenced", None, QtGui.QApplication.UnicodeUTF8))
        self.act_about.setText(QtGui.QApplication.translate("projectManager", "About...", None, QtGui.QApplication.UnicodeUTF8))
        self.act_docs.setText(QtGui.QApplication.translate("projectManager", "Documentation", None, QtGui.QApplication.UnicodeUTF8))
        self.act_exploreProject.setText(QtGui.QApplication.translate("projectManager", "Explore Project", None, QtGui.QApplication.UnicodeUTF8))

