# PROJECT MANAGER, Tim Crowson, June 2014
#----------------------------------------------------------------------------------------------------------------------


import os
import sys
import subprocess

import lx
import lxu
import lxifc
import lxu.select

from PySide.QtGui import QMessageBox, QGridLayout

import projectmanager as pm



def os_startFile(filename):
	'''
	Platform-respective function for running a file.
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
		pass

	def basic_Execute(self, msg, flags):
		''' Show the Project Manager '''
		lx.eval("layout.createOrClose viewCookie ProjectManagerLayout width:750 height:500 class:normal title:{Project Manager}")


#----------------------------------------------------------------------------------------------------------------------
class ExploreProjectFolder (lxu.command.BasicCommand):
	'''
	Modo Command to explore the current project directory.
	'''
	def __init__(self):
		lxu.command.BasicCommand.__init__(self)
		self.fileServ = lx.service.File()

	def cmd_Interact(self):
		pass

	def basic_Execute(self, msg, flags):
		'''
		Explore the current project directory
		'''
		projDir = self.fileServ.FileSystemPath( lx.symbol.sSYSTEM_PATH_PROJECT )
		os_startFile(projDir)


#----------------------------------------------------------------------------------------------------------------------
class ExploreSceneFolder (lxu.command.BasicCommand):
	'''
	Modo Command to explore the current scene's directory.
	'''
	def __init__(self):
		lxu.command.BasicCommand.__init__(self)

	def cmd_Interact(self):
		pass

	def basic_Execute(self, msg, flags):
		'''
		Explore the current project directory
		'''
		scene = lxu.select.SceneSelection().current().Filename()
		os_startFile( os.path.dirname( scene ) )

			
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
			self.form = pm.ProjectManager_Actual()
			layout.addWidget( self.form )
			parentWidget.setLayout( layout )
			return True

		return False


#----------------------------------------------------------------------------------------------------------------------
# BLESS THIS MESS!
lx.bless( ShowProjectManager, "project.manager" )
lx.bless( ExploreProjectFolder, "project.exploreCurrent" )
lx.bless( ExploreSceneFolder, "project.exploreSceneFolder" )
lx.bless( ProjectManager_CustomView, "ProjectManager" )
