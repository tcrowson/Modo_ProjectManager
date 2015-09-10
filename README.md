Project Manager Kit for Modo 901
==============

This kit augments Modo 901’s production workflow by providing a way to create and manage projects on a basic level, similar to what may be found in other 3D applications.

![](http://www.timcrowson.com/wp-content/uploads/2015/01/pm_001_c.png)

### Installation
ProjectManager is only available for Modo 801 on Linux, since its Windows and Mac versions do not yet offer PySide-based Custom Viewports.

1. Download [ProjectManager](http://www.timcrowson.com/downloads/projectmanager/tc_ProjectManager.zip)
2. Place the kit in your Modo User Scripts or Configs directory
3. Restart Modo

***

### Overview

The Project Manager lets you:
* Maintain a list of projects
* Switch active projects
* Create a new Modo project
* View a list of Modo-compatible scenes and file types belonging to a selected project
* Open or Import a compatible scene file
* Open a project folder
* Open a scene’s folder
* Add an existing project to the project list
* Remove a project from the list (does not delete anything on disk!)

*Note: This kit does not delete or rename anything inside a project directory! The only files this kit alters are data files used by the kit itself.*

This kit is purposely limited in its scope. It deals strictly with high-level functions and root structures, and does not attempt to manage dependencies or databases.
This kit is NOT…
* an asset management tool
* a version management tool
* a production management tool
* a database management tool

***

### Usage

1. Once installed, launch the Project Manager by running Projects > Project Manager.
![](http://www.timcrowson.com/wp-content/uploads/2015/01/pm_005.png)

2. The Project Manager is split into two lists. The left-side displays any projects you have added or created. The right-side shows scene files nested inside a selected project. To display scenes for the selected project, right-click on it and choose ‘Show Scenes’ or just double-click on the project. This can be a time-consuming process depending on several factors, which is why the Scenes list defaults to empty.
![](http://www.timcrowson.com/wp-content/uploads/2015/01/pm_006.png)

3. To set a project as the current working project, right-click on a project and choose ‘Set Selected As Current’. You can quickly explore the selected project’s root directory via ‘Open Project Folder…’.

4. You can change which filetypes displayed in the Scenes list by clicking ‘Show Filetypes…’. This will let you enable the file formats you want to see. The menu will stay open until you click off of it, at which point the Scenes list will update. (Your selected filetypes are saved in the background and persist between sessions).
![](http://www.timcrowson.com/wp-content/uploads/2015/01/pm_004.png)

5. From the Scenes list, you can load scenes into Modo by right-clicking on a scene and choosing either ‘Open Selected…’, ‘Import Selected’, or ‘Import Selected As Referenced’.  To quickly open a scene, double-click on it in the scenes list. You can quickly explore the containing folder for a scene via ‘Open Scene Folder’.
![](http://www.timcrowson.com/wp-content/uploads/2015/01/pm_003.png)

6. To create a new project, choose ‘New Project’ from either the ‘Projects’ Menu, or from the Project list’s contextual menu. You’ll be asked to choose a location and specify a name for the project. Please note that if you do not create the project from within the Project Manager, and use instead the native ‘New Project…’ command from Modo’s File menu, your new project will not be added to the list automatically.

7. To add an existing project to your list, right-click in the projects list and choose ‘Add Existing Project…’. Then choose the root directory of an existing project. If the selected directory is not a valid Modo project, it will be set up as such (a generic .luxproject file will be created), but no new directories will be created.

8. If a project cannot be found, the Project Manager will display it in red in the project list. If you wish to remove it from the list, right-click on it and choose ‘Remove Project’. This command does not interact with project files on disk, but simply removes it from the Manager’s list.

9. Behind the scenes, the Project Manager stores its list of projects in a simple text file ( \data\projects.projlist).

 

### Known Issues

Creating a new scene will cause Modo to (partially) forget what the current project is! This is a known bug of which The Foundry is aware. This bug will break the ‘Open Current Project Dirtectory’ command in the ‘Projects’ menu.

