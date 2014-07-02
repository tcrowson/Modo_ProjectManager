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
# CONTENTS OF THE 'ABOUT' DIALOG
aboutText = '''
version 0.1  - Tim Crowson, July 2014 

This kit offers a simple 3rd party solution for project management in Modo. See the documentation for details.
'''


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


def infoDialog(title, text):
	'''
	Pop up a standard info dialog box
	'''

	lx.eval( "dialog.setup info" )
	lx.eval( "dialog.title {%s}" %title )
	lx.eval( "dialog.msg {%s}" %text )
	#lx.eval( "dialog.result ok" )
	lx.eval( "dialog.open" )


def customStartFile(filename):
	'''
	Platform-respective function for opening a file
	'''
	if sys.platform == "win32":
		os.startfile( filename )
	else:
		opener ="open" if sys.platform == "darwin" else "xdg-open"
		subprocess.call( [opener, filename] )






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
			logMessage(lx.symbol.e_FAILED, ['Trouble exploring project folder.',
											'No project has been set.',
											'Please set the active project.'])
			infoDialog( 'Explore Current Project...', 'No project has been set. Please set the active project first')


#----------------------------------------------------------------------------------------------------------------------
class ExploreSceneFolder (lxu.command.BasicCommand):
	'''
	Modo Command to explore the current scene's directory.
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
			logMessage(lx.symbol.e_WARNING, ['Failed to explore scene directory...', 'No scene file is currently open!'] )
		else:
			customStartFile( os.path.dirname( scene ) )
			




#----------------------------------------------------------------------------------------------------------------------
class CleanXML():
	'''
	Tidies the formatting of an XML file to include carriage returns and
	indentations, facilitating readbility.

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
		self.newProjectPathButton.released.connect( self.project_PickRoot )
		self.createProjectButton.released.connect( self.project_Create )
		self.newTemplateButton.released.connect( self.template_new )
		self.addFolderButton.released.connect( self.template_addFolder )
		self.removeFolderButton.released.connect( self.template_removeFolder)
		self.resetTreeButton.released.connect( self.template_resetTree )
		self.saveTemplateButton.released.connect( self.template_save )

		# widgets
		self.projectTree.itemSelectionChanged.connect( self.get_scenes )
		self.projectTree.itemDoubleClicked.connect( self.act_proj_setAsCurrent )
		self.sceneTree.itemDoubleClicked.connect( self.act_scn_openSelected )
		self.fileTypeCombo.activated.connect( self.get_scenes )
		self.folderTree.itemDoubleClicked.connect( self.template_beginItemEdit )
		self.folderTree.itemChanged.connect( self.template_endItemEdit )
		self.folderTree.itemSelectionChanged.connect( self.template_endItemEdit )
		self.folderTemplateCombo.activated.connect( self.template_set)

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
		self.get_projects()
		self.projectTree.setColumnWidth( 0, 150 )
		self.sceneTree.setColumnWidth( 0, 150 )
		self.template_resetTree()
		self.get_templateList()
		self.newTemplateButton.setIcon( QIcon( os.path.join( resrcPath, 'icons/newTemplate.png' ) ) )
		self.addFolderButton.setIcon( QIcon( os.path.join( resrcPath, 'icons/addFolder.png' ) ) )
		self.removeFolderButton.setIcon( QIcon( os.path.join( resrcPath, 'icons/removeFolder.png' ) ) )
		self.resetTreeButton.setIcon( QIcon( os.path.join( resrcPath, 'icons/reset.png' ) ) )
		self.saveTemplateButton.setIcon( QIcon( os.path.join( resrcPath, 'icons/save.png' ) ) )


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


#   -----------------------------------------------------------


	def get_templateList(self):
		'''
		Update the entries in the Template list
		'''
		# start by clearing the list
		self.folderTemplateCombo.clear()

		# add an instruction entry
		self.folderTemplateCombo.addItem( "---  Choose a Template  ---" )

		# repopulate based on contents of the templates directory
		for file in os.listdir( templatesDir ):
			basename = os.path.basename( file )
			name, ext = os.path.splitext ( basename )
			if ext == '.xml':
				self.folderTemplateCombo.addItem( name )


	def get_projects(self):
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


	def get_scenes(self):
		'''
		Search the selected project for 3D scenes or files and display them in the scene list
		'''

		if self.projectTree.selectedItems():

			# start by clearing the scene list
			self.ui_clearTreeWidget( self.sceneTree )

			# get a clean project path
			projectItem = self.projectTree.selectedItems()[0]
			projDir = projectItem.text( 1 ).strip()
			
			# define a filetype lookup table
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

			# get the selected filter
			typeFilter = self.fileTypeCombo.currentText()

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


	def get_selectedProject(self):
		'''
		Return the path to the selected project
		'''
		selection = self.projectTree.selectedItems()[0]
		projDir = str(selection.text(1))
		return projDir.strip()


	def get_selectedScene(self):
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

		with open(projectListFile, 'r') as f:
			lines = [line for line in f if line.strip()]

		with open(projectListFile, 'w') as output:
			for line in lines:
			    output.write( line )
			output.write( "%s\n" %path )
			output.close()


#   -----------------------------------------------------------


	def template_set(self):
		'''
		Load the contents of a template into the folder tree.
		'''

		self.template_resetTree()

		if self.folderTemplateCombo.currentText() != "---  Choose a Template  ---":
			
			# start by clearing the current tree
			self.template_resetTree()

			def build(item, root):
				for element in root.getchildren():
					child = QTreeWidgetItem( item, [element.attrib['text']] )
					child.setFlags( child.flags() | Qt.ItemIsEditable )
					self.template_stylizeNewFolder( child )
					build( child, element )
				item.setExpanded( True )


			templateName = self.folderTemplateCombo.currentText()

			for file in os.listdir( templatesDir ):
				name, ext = os.path.splitext ( file )
				templateFile = os.path.join( templatesDir, file )

				if name == templateName and ext == '.xml':
					xmlTree = tree.parse(templateFile)
					root = xmlTree.getroot()
					build( self.folderTree.invisibleRootItem(), root )


	def template_new(self):
		'''
		Create a new blank  template.
		'''
		# request a template name
		name, ok = QInputDialog.getText(self, "Save Template", "Template Name...", QLineEdit.Normal)

		if ok:
			# clear the tree
			self.template_resetTree()

			# write an empty file
			templateFile = os.path.join( templatesDir, '%s.xml' %name )
			f = open(templateFile, 'w').close()

			# Update the UI
			self.get_templateList()

			# set the new template as the selected one
			self.folderTemplateCombo.setCurrentIndex( self.folderTemplateCombo.findText(name) )


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

		template = self.folderTemplateCombo.currentText()
		if template != '---  Choose a Template  ---':

			from xml.etree import cElementTree as etree

			root = etree.Element('root')
			root.attrib['templateName'] = template
			build( self.folderTree.invisibleRootItem(), root )

			# Write the file.
			templateFile = os.path.join( templatesDir, '%s.xml' %template )
			tree = etree.ElementTree( root )
			tree.write( templateFile )

			# Clean it up
			CleanXML().cleanWriteXML( templateFile )

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

			# set this new project as the current project in Modo
			lx.eval( "projDir.chooseProject %s" %inputPath )

			# update the project list file
			self.write_projectListFile( inputPath )

			# update the project list in the UI
			self.get_projects()

			# log
			logMessage( lx.symbol.e_INFO, ['The following project was created:', inputPath])


#   -----------------------------------------------------------


	def scene_openOrImport(self, type):
		'''
		Open or Import the target scene file
		'''
		scenePath = get_selectedScene()
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
			projDir = self.get_selectedProject()
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
			projDir = self.get_selectedProject()
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
		pass


	def act_proj_addExisting(self):
		'''
		Add an existing project to the project list
		'''
		pass


	def act_proj_exportList(self):
		'''
		Export the project list to a file
		'''
		pass


	def act_proj_importList(self):
		'''
		Import a project list from a file
		'''
		pass


	def act_scn_openSelected(self):
		'''  '''
		self.scene_openOrImport( 'normal')


	def act_scn_importSelected(self):
		''' '''
		self.scene_openOrImport( 'import')


	def act_scn_importSelectedAsRef(self):
		''' '''
		self.scene_openOrImport( 'ref')


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
