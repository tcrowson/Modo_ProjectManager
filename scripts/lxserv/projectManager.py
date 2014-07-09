# PROJECT MANAGER, Tim Crowson, June 2014
#----------------------------------------------------------------------------------------------------------------------





#----------------------------------------------------------------------------------------------------------------------
# IMPORTS

import os
import sys
import subprocess

import lx
import lxu
import lxifc
import lxu.select

import PySide
from PySide.QtGui import *
from PySide.QtCore import *

import xml.etree.ElementTree as tree



#----------------------------------------------------------------------------------------------------------------------
# GET BASIC SERVICES
fileServ = lx.service.File()
logServ = lx.service.Log()


#----------------------------------------------------------------------------------------------------------------------
# ESTABLISH PATHS

# kit folder
scriptsPath = fileServ.FileSystemPath( lx.symbol.sSYSTEM_PATH_SCRIPTS )
kitPath = os.path.join(scriptsPath,  'ProjectManager')

# data folder
dataPath = os.path.join(kitPath, 'scripts', 'lxserv', 'data')

# resource folder
resrcPath = os.path.join(kitPath, 'scripts', 'lxserv', 'resrc')

# project list file
projectListFile = os.path.join(dataPath, 'projects.projlist')

# templates folder
templatesDir = os.path.join(dataPath, 'templates')



#----------------------------------------------------------------------------------------------------------------------
# IMPORT THE UI
sys.path.append( resrcPath )
import projectManager_UI



#----------------------------------------------------------------------------------------------------------------------
# DIALOG STRING CONSTANTS
aboutText = '''
version 0.1  - Tim Crowson, July 2014 

This kit offers a simple 3rd party solution for project management in Modo. See the documentation for details.
'''

notImpl = ['---------- Not yet Implemented ----------']



#----------------------------------------------------------------------------------------------------------------------
# LOGGING CLASS
class Log:
	'''
	Provide an easy way for logging messages into choosen log subsystem.
	Original class by Lukasz Pazera: https://gist.github.com/lukpazera/10017005
	'''
	def __init__ (self):

	    self.log_service = lx.service.Log()
	    self.log = lx.object.Log()

	def set (self, log_name):
		'''
		This method has to be called before we can use the Log class instance.
		'''

		try:

			self.log = lx.object.Log(self.log_service.SubSystemLookup(log_name))
		except LookupError:
			return False
		return True

	def Out (self, message_type, head_message, child_messages=None):
		'''
		Output a message comprising of:
			- one head message,
			- a set of child messages passed as a list.
		Arguments:
			- message_type --- one of message type symbols such as lx.symbol.e_INFO, e_WARNING or e_FAILED.
			- head_message --- main message string.
			- child_messages --- list of string messages that will be printed under the head one.
		'''

		if not self.log.test():
			return False

		head_entry = lx.object.LogEntry(self.log_service.CreateEntryMessage(message_type, head_message))

		if not child_messages:
			child_messages = []

		if not isinstance(child_messages, list):
			child_messages = [child_messages]

		for child_message in child_messages:
			child_entry = lx.object.LogEntry(self.log_service.CreateEntryMessage(message_type, child_message))
			head_entry.AddEntry(child_entry)

		self.log.AddEntry(head_entry)



#----------------------------------------------------------------------------------------------------------------------
# HELPERS

def logMessage(type, child):
	'''
	Convenience function for intercepting and logging messages
	'''
	log = Log()
	if log.set('scripts'):
		log.Out(type, '   === Project Manager ===', child)


def messageBox(title, text):
	'''
	Generic Qt info dialog
	'''
	box = QMessageBox()
	box.setWindowTitle(title)
	text = '\n'.join(text)
	box.setContentsMargins( 10,10,30,10 )
	box.setText(text)
	box.exec_()


def inputDialog(title, text):
	'''
	Gneeric Qt string input dialog
	'''
	dialog = QInputDialog()
	dialog.setWindowTitle(title)
	dialog.setLabelText(text)
	dialog.exec_()
	if dialog.textValue():
		return dialog.textValue()
	else:
		return None


def customStartFile(filename):
	'''
	Platform-respective function for opening a file
	'''
	if sys.platform == "win32":
		os.startfile( filename )
	else:
		opener ="open" if sys.platform == "darwin" else "xdg-open"
		subprocess.call( [opener, filename] )


def getFiletypeLookup():
	'''
	Return a dictionary representing compatible scene filetypes
	'''
	fileTypeLookup = {
					'Modo (*.lxo)': '.lxo',
					'Preset (*.lxl)': '.lxl',
					'Lightwave (*.lwo)': '.lwo',
					'Wavefront (*.obj)': '.obj',
					'Alembic (*.abc)':' .abc',
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


#----------------------------------------------------------------------------------------------------------------------
class ShowProjectManager ( lxu.command.BasicCommand ):
	'''
	Modo Command to display the Project Manager in a new window.
	'''

	def __init__(self):
		lxu.command.BasicCommand.__init__(self)

	def cmd_Interact(self):
		''' '''
		pass

	def basic_Execute(self, msg, flags):
		''' Show the Project Manager '''
		lx.eval("layout.createOrClose viewCookie ProjectManagerLayout width:900 height:600 class:normal title:{Project Manager}")




#----------------------------------------------------------------------------------------------------------------------
class ExploreProjectFolder (lxu.command.BasicCommand):
	'''
	Modo Command to explore the current project directory.
	Logs and displays a warning if no project is set.
	'''

	def __init__(self):
		lxu.command.BasicCommand.__init__(self)

	def cmd_Interact(self):
		''' '''
		pass

	def basic_Execute(self, msg, flags):
		''' Explore the current project directory '''
		try:
			projDir = fileServ.FileSystemPath( lx.symbol.sSYSTEM_PATH_PROJECT )
			customStartFile(projDir)
		except:
			message = ['Trouble exploring project folder.',
						'No project has been set.',
						'Please set the active project.']
			logMessage( lx.symbol.e_FAILED, message )
			messageBox( 'Warning...', message )



#----------------------------------------------------------------------------------------------------------------------
class ExploreSceneFolder (lxu.command.BasicCommand):
	'''
	Modo Command to explore the current scene's directory.
	Logs and displays a warning if no scene is open.
	'''

	def __init__(self):
		lxu.command.BasicCommand.__init__(self)

	def cmd_Interact(self):
		''' '''
		pass

	def basic_Execute(self, msg, flags):
		''' Explore the current project directory '''
		
		scene = lxu.select.SceneSelection().current().Filename()
		
		if scene == None:
			message = ['Failed to explore scene directory...', 'No scene file is currently open!']
			logMessage(lx.symbol.e_WARNING,  message)
			messageBox( 'Warning...', message )
		else:
			customStartFile( os.path.dirname( scene ) )
			



#----------------------------------------------------------------------------------------------------------------------
class CleanXML():
	'''
	Tidies the formatting of an XML file to include carriage returns and
	indentations, facilitating readability.

	Its one public method is cleanWriteXML(), which takes a single argument: the
	path to an xml file. It opens the file, processes it, and rewrites it.

	Original class by Eric Thivierge. http://www.ethivierge.com/
	'''

	def _indent(self, elem, level=0):
		i = "\n" + level*"  "
		if len(elem):
			if not elem.text or not elem.text.strip():
				elem.text = i + "  "
			if not elem.tail or not elem.tail.strip():
				elem.tail = i
			for elem in elem:
				self._indent(elem, level+1)
			if not elem.tail or not elem.tail.strip():
				elem.tail = i
		else:
			if level and (not elem.tail or not elem.tail.strip()):
				elem.tail = i
	 
	def _cleanxml(self, xml):
		elem = tree.fromstring(xml)
		self._indent(elem)
		strIndented = tree.tostring(elem)
		return strIndented
	 
	def cleanWriteXML(self, strFilePath):
		fOpen = open(strFilePath,"r")
		fRead = fOpen.read()
		fWrite = open(strFilePath,"w")
		strPrettyXML = self._cleanxml(fRead)
		fWrite.write(strPrettyXML)
		fWrite.close()



#----------------------------------------------------------------------------------------------------------------------
class ProjectManager_Actual( QMainWindow, projectManager_UI.Ui_projectManager ):
	'''
	Project Manager Class
	'''

	def __init__(self, parent=None, selected=[], flag=0, *args):
		QMainWindow.__init__(self, parent)
		self.setupUi(self) # boilerplate for pre-converted PySide UIs
		self.ui_setConnections()
		self.ui_customize()


	def ui_setConnections(self):
		'''
		Connect signals and slots
		'''

		# buttons
		self.newProjectPathBtn.released.connect( self.project_PickRoot )
		self.createProjectBtn.released.connect( self.project_Create )
		self.newTemplateBtn.released.connect( self.template_new )
		self.addFolderBtn.released.connect( self.template_addFolder )
		self.delFolderBtn.released.connect( self.template_removeFolder)
		self.resetTreeBtn.released.connect( self.template_resetTree )
		self.saveTemplateBtn.released.connect( self.template_save )

		# widgets
		self.projectTree.itemClicked.connect( self.scenes_getAll )
		self.projectTree.itemDoubleClicked.connect( self.act_proj_setAsCurrent )
		self.sceneTree.itemDoubleClicked.connect( self.act_scn_openSelected )
		self.folderTree.itemDoubleClicked.connect( self.template_beginItemEdit )
		self.folderTree.itemChanged.connect( self.template_endItemEdit )
		self.folderTree.itemSelectionChanged.connect( self.template_endItemEdit )
		self.templateCbx.activated.connect( self.template_load)

		# project actions
		self.act_about.triggered.connect(self.ui_showAbout )
		self.act_addExisting.triggered.connect( self.act_proj_addExisting )
		self.act_removeSelected.triggered.connect( self.act_proj_removeSelected )
		self.act_exportList.triggered.connect( self.act_proj_exportList )
		self.act_importList.triggered.connect( self.act_proj_importList )
		self.act_setAsCurrent.triggered.connect( self.act_proj_setAsCurrent )
		self.act_exploreProject.triggered.connect( self.act_proj_explore )

		# scene actions
		self.act_openSelectedScene.triggered.connect( self.act_scn_openSelected )
		self.act_importSelectedScene.triggered.connect( self.act_scn_importSelected )
		self.act_importSelectedAsRef.triggered.connect( self.act_scn_importSelectedAsRef )

		# context menus
		self.projectTree.customContextMenuRequested.connect( self.contextMenu_projectList )
		self.sceneTree.customContextMenuRequested.connect( self.contextMenu_sceneList )


	def ui_customize(self):
		'''
		Configure some initial UI states
		'''
		self.existingProjectsSplitter.setSizes( [450,450] )
		self.projects_getExisting()
		self.projectTree.setColumnWidth( 0, 150 )
		self.sceneTree.setColumnWidth( 0, 150 )
		self.template_resetTree()
		self.templates_getExisting()
		self.newTemplateBtn.setIcon( QIcon( os.path.join( resrcPath, 'icons/newTemplate.png' ) ) )
		self.addFolderBtn.setIcon( QIcon( os.path.join( resrcPath, 'icons/addFolder.png' ) ) )
		self.delFolderBtn.setIcon( QIcon( os.path.join( resrcPath, 'icons/removeFolder.png' ) ) )
		self.resetTreeBtn.setIcon( QIcon( os.path.join( resrcPath, 'icons/reset.png' ) ) )
		self.saveTemplateBtn.setIcon( QIcon( os.path.join( resrcPath, 'icons/save.png' ) ) )
		self.ui_filtersMenu()



	def ui_clearTreeWidget(self, treewidget):
		'''
		Remove all items from the specified QTreeWidget
		'''
		iterator = QTreeWidgetItemIterator( treewidget, QTreeWidgetItemIterator.All )
		while iterator.value():
			iterator.value().takeChildren()
			iterator +=1
		i = treewidget.topLevelItemCount()
		while i > -1:
			treewidget.takeTopLevelItem(i)
			i -= 1


	def ui_showAbout(self):
		'''
		Display info about Project Manager in a modal window
		'''
		box = QMessageBox()
		box.setWindowTitle( 'About Project Manager...' )
		box.setContentsMargins( 0,5,5,5 )
		box.setText( aboutText )
		box.exec_()


	def ui_filtersMenu(self):
		'''
		Build and display the filetype filter menu
		'''
		fileTypes = getFiletypeLookup()
		self.filtersMenu = QMenu(self)
		for i in fileTypes:
			action = self.filtersMenu.addAction( i )
			action.setCheckable( True )
			self.filtersBtn.setMenu(self.filtersMenu)
			self.filtersBtn.setPopupMode(QToolButton.InstantPopup)


#   -----------------------------------------------------------


	def write_genericSysFile(self, path):
		'''
		Write a generic '.luxproject' system file to the specified path
		'''
		if os.path.exists(path):
			sysFile = os.path.join( path, '.luxproject' )
			f = open( sysFile, 'w' ) 
			f.write( r'#LXProject#\n' ) # bare bones definition
			f.close()


	def write_subdirectories(self, path):
		'''
		Create subdirectories matching the contents of the folder tree
		'''
		pass


	def write_projectListFile(self, path):
		'''
		Open the Project List File and append the specified path
		'''
		# read the lines
		with open(projectListFile, 'r') as f:
			lines = [line.strip() for line in f if line.strip()]
			f.close()

		# if the path isn't already in the list, add it
		if not path in lines:
			with open(projectListFile, 'w') as f:
				for line in lines:
				    f.write( line + '\n')
				f.write( path + '\n')
				f.close()


#   -----------------------------------------------------------


	def templates_getExisting(self):
		'''
		Update the entries in the template list
		'''
		# start by clearing the list
		self.templateCbx.clear()

		# add an instruction entry
		self.templateCbx.addItem( "---  Choose a Template  ---" )

		# repopulate based on contents of the templates directory
		templateList = []
		for file in os.listdir( templatesDir ):
			basename = os.path.basename( file )
			name, ext = os.path.splitext ( basename )
			if ext == '.xml':
				templateList.append( name )
		
		# add the sorted list of template names to the combobox
		self.templateCbx.addItems( sorted(templateList) )


	def template_load(self):
		'''
		Load the contents of a template into the folder tree.
		'''

		self.template_resetTree()

		if self.templateCbx.currentText() != "---  Choose a Template  ---":
			
			# start by clearing the current tree
			self.template_resetTree()

			def build(item, root):
				for element in root.getchildren():
					child = QTreeWidgetItem( item, [element.attrib['text']] )
					child.setFlags( child.flags() | Qt.ItemIsEditable )
					self.template_stylizeNewFolder( child )
					build( child, element )
				item.setExpanded( True )


			templateName = self.templateCbx.currentText()

			for file in os.listdir( templatesDir ):
				name, ext = os.path.splitext ( file )
				templateFile = os.path.join( templatesDir, file )

				if name == templateName and ext == '.xml':
					xmlTree = tree.parse(templateFile)
					root = xmlTree.getroot()
					build( self.folderTree.invisibleRootItem(), root )


	def template_new(self):
		'''
		Create a new blank template, but don't write anything to disk.
		'''

		# request a template name
		name = inputDialog('New Template', 'Template name?')

		if name:
			# clear the tree
			self.template_resetTree()

			# Update the UI
			tempName = '%s *' %name
			self.templateCbx.addItem( tempName )

			# set the new template as the selected one
			self.templateCbx.setCurrentIndex( self.templateCbx.findText(tempName) )


	def template_addFolder(self):
		'''
		Add a new item to the structure tree
		'''
		newItem = QTreeWidgetItem()
		newItem.setText( 0,'__NEW FOLDER__' )
		self.template_stylizeNewFolder( newItem )
		self.folderTree.addTopLevelItem( newItem )


	def template_removeFolder(self):
		'''
		Remove the selected item from the tree
		'''
		root = self.folderTree.invisibleRootItem()
		for item in self.folderTree.selectedItems():
			(item.parent() or root).removeChild( item )


	def template_resetTree(self):
		'''
		Remove all items from the tree
		'''
		self.ui_clearTreeWidget( self.folderTree )


	def template_save(self):
		'''
		Write the contents of the folder tree to an XML file.
		'''

		def build(item, root):
			for row in range(item.childCount()):
				child = item.child(row)
				element = etree.SubElement( root, 'folder', text=child.text(0) )
				build( child, element )

		template = self.templateCbx.currentText()

		if template != '---  Choose a Template  ---':

			# if the template is new, strip the 'not saved' indicator
			if template.endswith(' *'):
				template = template[:-2]

			from xml.etree import cElementTree as etree
			root = etree.Element('root')
			root.attrib['templateName'] = template
			build( self.folderTree.invisibleRootItem(), root )

			# Write the file.
			templateFile = os.path.join( templatesDir, '%s.xml' %template )
			tree = etree.ElementTree( root )
			tree.write( templateFile )

			# clean it up
			CleanXML().cleanWriteXML( templateFile )

			# refresh the template list
			self.templates_getExisting()

			# select and reload the saved template
			self.templateCbx.setCurrentIndex( self.templateCbx.findText(template) )
			self.template_load()

			# log
			logMessage( lx.symbol.e_INFO, ['Structure Template saved:', template])


	def template_beginItemEdit(self):
		'''
		Begin editing template Item
		'''
		self.folderTree.openPersistentEditor( self.folderTree.currentItem(), 0 )


	def template_endItemEdit(self):
		'''
		Stop editing item name and sort the folder tree
		'''
		self.folderTree.closePersistentEditor( self.folderTree.currentItem(), 0 )
		self.folderTree.sortItems( 0, Qt.AscendingOrder )


	def template_stylizeNewFolder(self, item):
		'''
		Customize the look of folder items in the folder tree
		'''
		item.setSizeHint( 0, QSize(100, 20) )
		icon = os.path.join( resrcPath, 'icons/folder.png' ) 
		item.setIcon( 0, QIcon(icon) )


#   -----------------------------------------------------------


	def projects_getExisting(self):
		'''
		Populate the Existing Projects list, via the projects.projlist file
		'''
		# clear the list
		self.ui_clearTreeWidget( self.projectTree )

		# read the contents of the projects.projlist and add them to the list
		with open( projectListFile ) as fileList:

			lines = [line for line in fileList if line.strip()]

			for line in lines:

				cleanLine = line.strip()
				projectTitle = os.path.split(cleanLine)[1]

				# create the projectItem
				projectItem = QTreeWidgetItem()
				projectItem.setSizeHint( 0, QSize(200, 25) )
				projectItem.setText( 0, projectTitle )
				projectItem.setText( 1, cleanLine )

				# designate bad project
				if not os.path.exists(cleanLine):
					projectItem.setForeground( 0, QBrush( QColor('#8C2727') ) )
					projectItem.setForeground( 1, QBrush( QColor('#8C2727') ) )

				# add the item to the tree
				self.projectTree.addTopLevelItem( projectItem )

				# sort the tree
				self.projectTree.sortItems( 0, Qt.AscendingOrder )


	def projects_getSelected(self):
		'''
		Return the path to the selected project
		'''
		if len(self.projectTree.selectedItems()) > 0:
			selection = self.projectTree.selectedItems()[0]
			projDir = str(selection.text(1))
			return projDir.strip()
		else:
			return False


	def project_PickRoot(self):
		'''
		Open a file dialog and let the user choose a project root directory
		'''
		currentPath = self.newProjectPath.text()

		startDir = currentPath if os.path.exists(currentPath) else '/home'

		inputPath = QFileDialog.getExistingDirectory( self, 'Set a location for your new project...', startDir )

		if os.path.exists( inputPath ):
			self.newProjectPath.setText( inputPath )


	def project_Create(self):
		'''
		Create a Modo project at the destination specified by the user
		'''
		inputPath = self.newProjectPath.text()

		if os.path.exists( inputPath ):

			# write the system file
			self.write_genericSysFile( inputPath )

			# create any subdirectories
			if self.createFoldersCheckBox.isChecked():
				self.write_subdirectories( inputPath )


			# update the project list file
			self.write_projectListFile( inputPath )

			# update the project list in the UI
			self.projects_getExisting()

			# log and inform
			message = ['The following project was created:', str(inputPath)]
			logMessage( lx.symbol.e_INFO, message)
			messageBox( 'Project Manager', message )

			# Set this new project as the current project in Modo.
			# If this not done AFTER displaying the message box above, Modo will crash.
			lx.eval( "projDir.chooseProject %s" %inputPath )



#   -----------------------------------------------------------


	def scenes_getAll(self):
		'''
		Search the selected project for 3D scenes or files and display them in the scene list
		'''

		if self.projectTree.selectedItems():

			# start by clearing the scene list
			self.ui_clearTreeWidget( self.sceneTree )

			# get a clean project path
			projectItem = self.projectTree.selectedItems()[0]
			projDir = projectItem.text( 1 ).strip()
			
			# get the selected filter
			typeFilter = self.fileTypeCbx.currentText()

			# walk the project and display all files of the filtered type
			for root, dirs, files in os.walk( projDir ):
				for file in files:
					if file.endswith( fileTypeLookup[typeFilter] ):
						filePath = os.path.join( root, file )
						fileName = os.path.basename( filePath )
						relativePath = filePath.replace( projDir, '' )

						# create the file item
						item = QTreeWidgetItem()
						item.setText( 0, fileName )
						item.setText( 1, relativePath )
						item.setSizeHint( 0, QSize(200, 25) )

						# add the item to the scene tree
						self.sceneTree.addTopLevelItem( item )

						# sort the scene tree
						self.sceneTree.sortItems( 0, Qt.AscendingOrder )


	def scenes_getSelected(self):
		'''
		Return the path to the selected scene
		'''
		if self.sceneTree.selectedItems():
			projectItem = self.projectTree.selectedItems()[0]
			projDir = projectItem.text( 1 ).strip()
			sceneItem = self.sceneTree.selectedItems()[0]
			sceneRelativePath = sceneItem.text( 1 )
			scenePath = projDir + sceneRelativePath
			return scenePath


	def scenes_openOrImport(self, type):
		'''
		Open or Import the target scene file
		'''
		scenePath = self.scenes_getSelected()
		if scenePath:
			if type == 'ref':
				lx.eval( "+scene.importReference {%s}" %scenePath )
			else:
				lx.eval( "scene.open %s %s" %( scenePath, type ) )


#   -----------------------------------------------------------


	def act_proj_explore(self):
		'''
		Explore the selected project's directory
		'''
		if self.projectTree.selectedItems():
			projDir = self.projects_getSelected()
			if os.path.exists( projDir ):
				customStartFile( projDir )
			else:
				logMessage(lx.symbol.e_FAILED, ['Trouble exploring project folder...',
												'Invalid project path.'] )

	
	def act_proj_setAsCurrent(self):
		'''
		Set the selected project as the current project in Modo
		'''
		if self.projectTree.selectedItems():
			projDir = self.projects_getSelected()
			if os.path.exists( projDir ):
				lx.eval( "projDir.chooseProject %s" %projDir )
				logMessage( lx.symbol.e_INFO, ['Successfully set current project:', projDir])

			else:
				logMessage(lx.symbol.e_FAILED, ['Trouble setting current project...',
												'Invalid project path.'] )


	def act_proj_removeSelected(self):
		'''
		Remove the selected project from the project list
		'''
		project = self.projects_getSelected()

		if project:

			# remove it from the project list - start by reading the current list
			with open(projectListFile, 'r') as f:
				lines = [line.strip() for line in f if line.strip()]
				f.close()

			# if the path is in the list, remove it
			if project in lines:
				lines.remove(project)
				# and write the updated list
				with open(projectListFile, 'w') as f:
					for line in lines:
					    f.write( line + '\n')
					f.close()

			# update the UI
			self.projects_getExisting()


	def act_proj_addExisting(self):
		'''
		Add an existing project to the project list
		'''
		messageBox('Add Existing Project', notImpl)


	def act_proj_exportList(self):
		'''
		Export the project list to a file
		'''
		messageBox('Export Project List', notImpl)


	def act_proj_importList(self):
		'''
		Import a project list from a file
		'''
		messageBox('Import Project List', notImpl)


	def act_scn_openSelected(self):
		'''  '''
		self.scenes_openOrImport( 'normal')


	def act_scn_importSelected(self):
		''' '''
		self.scenes_openOrImport( 'import')


	def act_scn_importSelectedAsRef(self):
		''' '''
		self.scenes_openOrImport( 'ref')


#   -----------------------------------------------------------


	def contextMenu_projectList(self):
		'''
		Contextual menu for the Project list
		'''
		# Create the menu object.
		menu = QMenu()

		explore = menu.addAction( 'Explore Project',  self.act_proj_explore)
		setAsCurrent = menu.addAction( 'Set Selected As Current', self.act_proj_setAsCurrent )
		remove = menu.addAction( 'Remove Project From List', self.act_proj_removeSelected )

		menu.addSeparator()

		addExisting = menu.addAction( 'Add Existing Project to List...', self.act_proj_addExisting )
		exportList = menu.addAction( 'Export List', self.act_proj_exportList )
		importList = menu.addAction( 'Import List', self.act_proj_importList )

		# Show the menu.
		action = menu.exec_( QCursor.pos() )


	def contextMenu_sceneList(self):
		'''
		Contextual menu for the Scene list
		'''
		# Create the menu object.
		menu = QMenu()

		openScene = menu.addAction( 'Open Selected Scene', self.act_scn_openSelected )
		importScene = menu.addAction( 'Import Selected Scene', self.act_scn_importSelected )
		importAsRef = menu.addAction('Import Selected Scene As Referenced', self.act_scn_importSelectedAsRef )

		# Show the menu.
		action = menu.exec_( QCursor.pos() )




#----------------------------------------------------------------------------------------------------------------------
class ProjectManager_CustomView(lxifc.CustomView):
	''' '''
	def __init__ (self):
		self.form = None

	def customview_Init(self, pane):
		# Get the pane
		if pane == None:
			return False

		custPane = lx.object.CustomPane( pane )

		if custPane.test() == False:
			return False

		# Get the parent QWidget
		parent = custPane.GetParent()
		parentWidget = lx.getQWidget( parent )

		# Check that it suceeds
		if parentWidget != None:
			layout = QGridLayout()
			layout.setContentsMargins( 2,2,2,2 )
			self.form = ProjectManager_Actual()
			layout.addWidget( self.form )
			parentWidget.setLayout( layout )
			return True

		return False


#----------------------------------------------------------------------------------------------------------------------
# BLESS THIS MESS!
lx.bless( ShowProjectManager, "project.manager" )
lx.bless( ExploreProjectFolder, "project.exploreCurrent" )
lx.bless( ExploreSceneFolder, "project.ExploreSceneFolder" )
lx.bless( ProjectManager_CustomView, "ProjectManager" )
