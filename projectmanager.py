#------------------------------------------------------------------------------
# PROJECT MANAGER v1.0.7, Tim Crowson
#------------------------------------------------------------------------------


import os
import sys
import pickle
import subprocess

import lx

from PySide.QtGui import *
from PySide.QtCore import *

from projectmanager_ui import Ui_projectManager

version = '1.0.7'


# PATHS
KITPATH = os.path.dirname(__file__)
DATAPATH = os.path.join(KITPATH, 'data')
FILTERSPATH = os.path.join(DATAPATH, 'filters.p')
PROJECTLISTFILE = os.path.join(DATAPATH, 'projects.projlist')


class StickyMenu(QObject):
    '''
    Enables a menu behavior whereby clicking on an item keeps the menu open.
    Thanks to Jon Swindells for his help here.
    '''
    def eventFilter(self, obj, event):
        mods = QApplication.keyboardModifiers()
        if not mods or mods == Qt.ShiftModifier:
            if event.type() in [QEvent.MouseButtonRelease] and isinstance(obj, QMenu):
                if obj.activeAction() and not obj.activeAction().menu():
                    obj.activeAction().trigger()
                    return True
        return super(StickyMenu, self).eventFilter(obj, event)


class ProjectManager(QMainWindow):
    '''
    Modo Project Manager Class.
    '''
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.ui = Ui_projectManager()
        self.ui.setupUi(self)
        self.ui_setConnections()

        # set some initial UI states
        self.ui.projectsSplitter.setSizes([450,450])
        self.projects_getExisting()
        self.ui.projectTree.setColumnWidth(0, 200)
        self.ui.sceneTree.setColumnWidth(0, 200)
        self.ui.projectTree.setColumnHidden(1, True)
        self.ui.sceneTree.setColumnHidden(1, True)
        self.ui_buildFileTypeFilterMenu()

    def ui_setConnections(self):
        '''
        Connect signals and slots.
        '''
        # widgets
        self.ui.togglePathsCheckBox.stateChanged.connect(self.ui_togglePaths)
        self.ui.projectTree.itemDoubleClicked.connect(self.scenes_getAll)
        self.ui.projectTree.itemSelectionChanged.connect(self.scenes_clearList)
        self.ui.sceneTree.itemDoubleClicked.connect(self.act_scn_openSelected)

        # project actions
        self.ui.act_newProject.triggered.connect(self.act_project_create)
        self.ui.act_addExisting.triggered.connect(self.act_proj_addExisting)
        self.ui.act_removeSelected.triggered.connect(self.act_proj_removeSelected)
        self.ui.act_setAsCurrent.triggered.connect(self.act_proj_setAsCurrent)
        self.ui.act_exploreProject.triggered.connect(self.act_proj_explore)
        self.ui.act_exploreSceneFolder.triggered.connect(self.act_scn_openFolder)
        self.ui.act_docs.triggered.connect(self.act_launchDocs)

        # scene actions
        self.ui.act_openSelectedScene.triggered.connect(self.act_scn_openSelected)
        self.ui.act_importSelectedScene.triggered.connect(self.act_scn_importSelected)
        self.ui.act_importSelectedAsRef.triggered.connect(self.act_scn_importSelectedAsRef)

        # context menus
        self.ui.projectTree.customContextMenuRequested.connect(self.contextMenu_projectList)
        self.ui.sceneTree.customContextMenuRequested.connect(self.contextMenu_sceneList)

    def ui_clearTreeWidget(self, treewidget):
        '''
        Remove all items from the specified QTreeWidget.
        Arg 1: the target widget <QTreeWidget>
        '''
        iterator = QTreeWidgetItemIterator(treewidget, QTreeWidgetItemIterator.All)
        while iterator.value():
            iterator.value().takeChildren()
            iterator +=1
        i = treewidget.topLevelItemCount()
        while i > -1:
            treewidget.takeTopLevelItem(i)
            i -= 1

    def ui_buildFileTypeFilterMenu(self):
        '''
        Build and display the filetype filters menu.
        This menu will stay open until you click off of it.
        '''
        # create a new menu
        self.ui.filtersMenu = QMenu()

        # inherit the stylesheet from main ui
        self.ui.filtersMenu.setStyleSheet(self.styleSheet())

        # set up the menu's event filter and action
        self.ui.evFilter = StickyMenu()
        self.ui.filtersMenu.installEventFilter(self.ui.evFilter)
        self.ui.filtersMenu.aboutToHide.connect(self.ui_closeFileTypeFilterMenu)

        # load prevous selection if possible
        data = False
        if os.path.exists(FILTERSPATH):
            try:
                data = pickle.load(open(FILTERSPATH, 'r'))
            except IOError:
                lx.out('PROJECT MANAGER: Unable to apply previous filters. Data incorrectly serialized.')

        # populate the list of filetype options
        fileTypes = self.ui_getFileTypes()
        for i in sorted(fileTypes):
            action = self.ui.filtersMenu.addAction(i)
            action.setCheckable(True)
            if data:
                if i in data:
                    action.setChecked(True)

        # apply the menu to the button
        self.ui.filtersBtn.setMenu(self.ui.filtersMenu)

    def ui_closeFileTypeFilterMenu(self):
        '''
        Close the file type filter menu, save out the checked items, and refresh the scene list
        '''
        # serialize and store the checked items for later use
        selectedTypes = [action.text() for action in self.ui.filtersMenu.actions() if action.isChecked()]
        pickle.dump(selectedTypes, open(FILTERSPATH, 'w'))

        # refresh the scenes list
        self.scenes_getAll()

    def ui_getFileTypes(self):
        '''
        Return compatible scene filetypes as a dictionary.
        '''
        fileTypeLookup = {
            'Modo (*.lxo)': '.lxo',
            'Preset (*.lxl)': '.lxl',
            'Lightwave (*.lwo)': '.lwo',
            'Wavefront (*.obj)': '.obj',
            'Alembic (*.abc)':'.abc',
            'Filmbox (*.fbx)': '.fbx',
            'Collada (*.dae)': '.dae',
            'Rhino (*.3dm)': '.3dm',
            'Autodesk DXF (.*dxf)': '.dxf',
            'Adobe Illustrator (*.eps, *.ai)': '.eps|.ai',
            'Stereolithography (*.stl)': '.stl',
            'Videoscape (*.geo)': '.geo',
            'Solidworks (*.sldprt, *.sldasm)': '.sldprt|.sldasm',
            'Protein DB (*.pdb)': '.pdb'
            }
        return fileTypeLookup

    def ui_togglePaths(self):
        '''
        Show or hide the path columns for the projects and scenes lists.
        '''
        state = self.ui.togglePathsCheckBox.isChecked()
        self.ui.projectTree.setColumnHidden(1,  not state)
        self.ui.projectTree.setColumnWidth(0, 150)
        self.ui.sceneTree.setColumnHidden(1, not state)
        self.ui.sceneTree.setColumnWidth(0, 200)

    def dialog_info(self, title, message):
        '''
        Generic Qt Message box
        Arg 1: the window title <string> 
        Arg 2: the message <string>
        '''
        box = QMessageBox()
        box.setWindowTitle(title)
        box.setText(message)
        box.exec_()

    def dialog_inputString(self, title, text):
        '''
        Generic Qt string input dialog.
        Arg 1: the window title <string> 
        Arg 2: the field label <string>
        '''
        dialog = QInputDialog()
        dialog.setWindowTitle(title)
        dialog.setLabelText(text)
        dialog.exec_()
        if dialog.textValue():
            return dialog.textValue()
        return None

    def dialog_confirm(self, title, text):
        '''
        Generic Qt confirmation request.
        Arg 1: the window title <string>  
        Arg 2: the question <list>
        '''
        box = QMessageBox()
        box.setWindowTitle(title)
        box.setText('\n'.join(text))
        box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        box.setDefaultButton(QMessageBox.No)
        return box.exec_()

    def explore(self, filename):
        '''
        Platform-respective function for opening a file.
        Arg 1: the path to the file/folder <string>
        '''
        if sys.platform == "win32":
            os.startfile(filename)
        else:
            opener ="open" if sys.platform == "darwin" else "xdg-open"
            subprocess.call([opener, filename])

    def write_genericSysFile(self, folder):
        '''
        Write a generic '.luxproject' system file to the specified path.
        Arg 1: the path to the file <string>
        '''
        contents =  [   
            '#LXProject#',
            'Associate image Images',
            'Associate irrad IrradianceCaches',
            'Associate movie Movies',
            'Associate image@renderframes Renders/Frames',
            'Associate movie@rendermovies Renders/Movies',
            'Associate movie_st@rendermovies Renders/Movies',
            'Associate movie_nost@rendermovies Renders/Movies',
            'Associate scene Scenes',
            'Associate scene.saveAs Scenes',
            'ScriptSearchPath Scripts'
            ]

        if os.path.exists(folder):
            sysFile = os.path.join(folder, '.luxproject')
            f = open(sysFile, 'w') 
            f.write('\n'.join(contents))
            f.close()

    def write_rootDefaultSysFile(self, folder):
        '''
        Write a '.luxproject' system file to the specified path.
        Arg 1: the path to the file <string>
        
        The associations defined by this file are deliberately empty for now,
        forcing Modo's file requesters to default to the project root.
        '''
        contents =  [   
            '#LXProject#',
            'Associate image ',
            'Associate irrad ',
            'Associate movie ',
            'Associate image@renderframes ',
            'Associate movie@rendermovies ',
            'Associate movie_st@rendermovies ',
            'Associate movie_nost@rendermovies ',
            'Associate scene ',
            'Associate scene.saveAs ',
            'ScriptSearchPath '
            ]

        if os.path.exists(folder):
            sysFile = os.path.join(folder, '.luxproject')
            f = open(sysFile, 'w') 
            f.write('\n'.join(contents))
            f.close()

    def write_projectListFile(self, projectPath):
        '''
        Open the Project List File and append the specified path.
        Arg 1: the project path <string>.
        '''
        # read the lines
        with open(PROJECTLISTFILE, 'r') as f:
            lines = [line.strip() for line in f if line.strip()]
            f.close()

        # if the path isn't already in the list, add it
        if not projectPath in lines:
            with open(PROJECTLISTFILE, 'w') as f:
                for line in lines:
                    f.write(line + '\n')
                f.write(projectPath + '\n')
                f.close()

    def projects_getExisting(self):
        '''
        Populate the Existing Projects list, via the projects.projlist file.
        '''
        # clear the list
        self.ui_clearTreeWidget(self.ui.projectTree)

        # ensure the project list file exists:
        if not os.path.exists(PROJECTLISTFILE):
            open(PROJECTLISTFILE, 'w').close

        # read the contents of the projects.projlist file and add them to the list
        else:
            with open(PROJECTLISTFILE) as fileList:

                lines = [line.strip() for line in fileList if line.strip()]

                for line in lines:
                    projectTitle = os.path.split(line)[1]

                    # create the projectItem
                    projectItem = QTreeWidgetItem()
                    projectItem.setSizeHint(0, QSize(200, 25))
                    projectItem.setText(0, projectTitle)
                    projectItem.setText(1, line)
                    projectItem.setForeground(1 , QBrush(QColor('#575757')))

                    # display bad project paths in red
                    if not os.path.exists(line):
                        projectItem.setForeground(0, QBrush(QColor('#8C2727')))
                        projectItem.setForeground(1, QBrush(QColor('#8C2727')))

                    # add the item to the tree
                    self.ui.projectTree.addTopLevelItem(projectItem)

                    # sort the tree
                    self.ui.projectTree.sortItems(0, Qt.AscendingOrder)

    def projects_getSelectedPath(self):
        '''
        Return the path to the selected project.
        '''
        if len(self.ui.projectTree.selectedItems()) > 0:
            selection = self.ui.projectTree.selectedItems()[0]
            projDir = str(selection.text(1))
            return projDir.strip()
        return False

    def scenes_clearList(self):
        '''
        Clear the contents of the Scenes List.
        '''
        self.ui_clearTreeWidget(self.ui.sceneTree)

    def scenes_getAll(self):
        '''
        Search the selected project for files and display them in the scene list.
        Display only filetypes which are checked in the filters menu.
        '''
        if self.ui.projectTree.selectedItems():

            # change the cursor to indicate activity
            QApplication.setOverrideCursor(Qt.BusyCursor) 

            # start by clearing the scene list
            self.ui_clearTreeWidget(self.ui.sceneTree)

            # get a clean project path
            projectItem = self.ui.projectTree.selectedItems()[0]
            projDir = projectItem.text(1).strip()

            # get the checked file types from the filter list
            fileTypes = self.ui_getFileTypes()          
            selectedTypes = [fileTypes[action.text()] for action in self.ui.filtersMenu.actions() if action.isChecked()]

            # walk the project and display all files of the checked types
            for root, dirs, files in os.walk(projDir):
                for file in files:
                    filename, ext = os.path.splitext(file)
                    if ext in selectedTypes:
                        filePath = os.path.join(root, file)
                        fileName = os.path.basename(filePath)
                        relativePath = filePath.replace(projDir, '')

                        # create the file item
                        item = QTreeWidgetItem()
                        item.setText(0, fileName)
                        item.setText(1, relativePath)
                        item.setSizeHint(0, QSize(200, 25))
                        item.setForeground(1 , QBrush(QColor('#575757')))

                        # add the item to the scene tree
                        self.ui.sceneTree.addTopLevelItem(item)

                        # sort the scene tree
                        self.ui.sceneTree.sortItems(0, Qt.AscendingOrder)

            # restore the cursor to its normal state
            QApplication.restoreOverrideCursor()

    def scenes_getSelectedPath(self):
        '''
        Return the path to the selected scene.
        '''
        scenePath = None
        if self.ui.sceneTree.selectedItems():
            projectItem = self.ui.projectTree.selectedItems()[0]
            projDir = projectItem.text(1).strip()
            sceneItem = self.ui.sceneTree.selectedItems()[0]
            sceneRelativePath = sceneItem.text(1)
            if os.path.exists(projDir + sceneRelativePath):
                scenePath = projDir + sceneRelativePath
        return scenePath

    def scenes_openOrImport(self, type):
        '''
        Open or Import the selected 3D file.
        Arg 1: the type of operation <string> ('ref' | 'normal' | 'open')
        '''
        scenePath = self.scenes_getSelectedPath()
        if scenePath is not None:
            if type == 'ref':
                lx.eval("+scene.importReference {%s}" %scenePath)
            else:
                lx.eval('scene.open "%s" %s' %(scenePath, type))

    def act_project_create(self):
        '''
        Create a Modo project at the destination specified by the user via File Dialog.
        '''
        # create the project with the standard template
        try:
            lx.eval('?projdir.instantiate')
            folderPicked = True
        except:
            folderPicked = False

        if folderPicked:
            # get the path we just set
            platform = lx.service.Platform()
            for idx in range(platform.PathCount()):
                if platform.PathNameByIndex(idx) == "project":
                    folder = platform.PathByIndex(idx)

            # update the project list file
            self.write_projectListFile(folder)

            # update the project list in the UI
            self.projects_getExisting()

            # log and inform
            lx.out('PROJECT MANAGER: A new project was created: %s' %folder)
            self.dialog_info('Project Manager', "Project '%s' was created!" %os.path.basename(folder))

    def act_proj_explore(self):
        '''
        Explore the selected project's directory.
        '''
        if self.ui.projectTree.selectedItems():
            projDir = self.projects_getSelectedPath()
            if os.path.exists(projDir):
                self.explore(projDir)
            else:
                self.dialog_info('Trouble exploring project folder...', 'Invalid project path.')

    def act_proj_setAsCurrent(self):
        '''
        Set the selected project as the current project in Modo.
        '''
        if self.ui.projectTree.selectedItems():
            projDir = self.projects_getSelectedPath()
            if os.path.exists(projDir):
                lx.eval('projDir.chooseProject "%s"' %projDir)
            else:
                self.dialog_info('Trouble setting the project...', 'Invalid project path.')

    def act_proj_removeSelected(self):
        '''
        Remove the selected project from the project list.
        '''
        project = self.projects_getSelectedPath()

        if project:
            confirm = self.dialog_confirm(  'Remove Project...', ['Remove the selected project from the list?'])
            if confirm == QMessageBox.Yes:

                # start by reading the current list
                with open(PROJECTLISTFILE, 'r') as f:
                    lines = [line.strip() for line in f if line.strip()]
                    f.close()

                # if the path is in the list, remove it
                if project in lines:
                    lines.remove(project)
                    # and write the updated list
                    with open(PROJECTLISTFILE, 'w') as f:
                        for line in lines:
                            f.write(line + '\n')
                        f.close()

                # update the UI
                self.projects_getExisting()

    def act_proj_addExisting(self):
        '''
        Add an existing project to the project list.
        '''
        inputPath = QFileDialog.getExistingDirectory(self, 'Select a project...', '/home')
        if os.path.exists(inputPath):

            # look for a '.luxproject' file
            if '.luxproject' in [file for file in os.listdir(inputPath)]:
                f = open(os.path.join(inputPath, '.luxproject'))
                lines = f.readlines()

                # check if the '.luxproject' file is legit
                if lines[0].strip() == '#LXProject#':
                    self.write_projectListFile(inputPath)
                    self.projects_getExisting()
                    return
                else:
                    self.dialog_info('Unable to add project...', 'The .luxproject file is incomplete...') 

            else:
                self.write_rootDefaultSysFile(inputPath)
                self.write_projectListFile(inputPath)
                self.projects_getExisting()

    def act_scn_openSelected(self):
        '''
        Open the selected Modo-compatible file in the current instance of Modo 
        '''
        self.scenes_openOrImport('normal')

    def act_scn_importSelected(self):
        '''
        Import the selected Modo-compatible file into the current instance of Modo 
        '''
        self.scenes_openOrImport('import')

    def act_scn_importSelectedAsRef(self):
        '''
        Import the selected Modo-compatible file as referenced into the current instance of Modo 
        '''
        self.scenes_openOrImport('ref')

    def act_scn_openFolder(self):
        '''
        Open the folder containing the selected scene.
        '''
        scenePath = self.scenes_getSelectedPath()
        if scenePath:
            self.explore(os.path.dirname(scenePath))

    def act_launchDocs(self):
        '''
        Open the documentation in a web browser.
        '''
        self.explore("http://www.timcrowson.com/modo-project-manager/")

    def contextMenu_projectList(self):
        '''
        Build a contextual menu for the Project list.
        '''
        menu = QMenu()
        menu.setStyleSheet('QMenu::item:selected{color: #f89a2b;background: #545454;}')
        menu.addAction('New Project...', self.act_project_create)
        menu.addAction('Set Selected As Current', self.act_proj_setAsCurrent)
        menu.addAction('Open Project Folder...',  self.act_proj_explore)
        menu.addAction('Add Existing Project to List...', self.act_proj_addExisting)
        menu.addAction('Remove Selected Project from List', self.act_proj_removeSelected)
        menu.addAction('Show Scenes', self.scenes_getAll)
        menu.exec_(QCursor.pos())

    def contextMenu_sceneList(self):
        '''
        Build a contextual menu for the Scene list.
        '''
        menu = QMenu()
        menu.setStyleSheet('QMenu::item:selected{color: #f89a2b;background: #545454;}')
        menu.addAction('Open Selected Scene', self.act_scn_openSelected)
        menu.addAction('Import Selected Scene', self.act_scn_importSelected)
        menu.addAction('Import Selected As Referenced', self.act_scn_importSelectedAsRef)
        menu.addAction('Open Scene Folder', self.act_scn_openFolder)
        menu.exec_(QCursor.pos())
