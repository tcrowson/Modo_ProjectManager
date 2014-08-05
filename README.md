Project Manager Kit for Modo 801
==============


***IMPORTANT:***
* This is a work in progress!
* This is for Modo 801 Linux only, as Modo does not support Qt on Windows and Mac.

***

* [Overview](https://github.com/tcrowson/ProjectManager/wiki#overview)
  * [What This Is](https://github.com/tcrowson/ProjectManager/wiki#what-this-is)
  * [What This Is Not](https://github.com/tcrowson/ProjectManager/wiki#what-this-is-not)
* [Existing Projects](https://github.com/tcrowson/ProjectManager/wiki#existing-projects)
  * [The Projects List](https://github.com/tcrowson/ProjectManager/wiki#the-projects-list)
  * [The Scenes List](https://github.com/tcrowson/ProjectManager/wiki#the-scenes-list)
* [New Project](https://github.com/tcrowson/ProjectManager/wiki#new-project)
  * [Set the Project Root](https://github.com/tcrowson/ProjectManager/wiki#set-the-project-root)
  * [Create Folders](https://github.com/tcrowson/ProjectManager/wiki#create-folders)
  * [Create the Project](https://github.com/tcrowson/ProjectManager/wiki#create-the-project)

***

#Overview
### What This Is
This kit attempts to fill a gap in Modo's production workflow by providing a way to create and manage projects on a basic level. Other popular DCC applications offer basic tools for project setup and management, and this kit aims to bring some of that to Modo, with a couple of twists.

This Project Manager kit lets you:
* View a list of existing projects
* Switch active projects
* View a list Modo-compatible scenes and file types belonging to a selected project
* Open, Import, or Import a file as referenced
* Open a given project folder
* Open a given scene's folder
* Create and save custom directory structure templates for later use
* Create a new Modo project along with any template-driven folder structures
* Add an existing project to the project list
* Remove a project from the list (does not delete anything on disk!)

> Note:
> This kit does not delete or rename anything inside a project directory! If folders already exist at the target location, they are left alone. The only files this kit alters are data files used by the kit itself (i.e. the project list, the template files...)


![](http://www.timcrowson.com/wp-content/uploads/2014/07/projectInList.jpg)


### What This Is Not
The Project Manager kit is purposely limited in its scope. It deals strictly with high-level functions and root structures, and does not attempt to manage dependencies, databases, or sub-entity branching. It is **NOT**...
* an _asset_ management tool
* a _version_ management tool
* a _production_ management tool
* a _database_ management tool


# Existing Projects
### The Projects List
The window on the left side of the `Existing Projects` Tab shows existing projects that you have either created with the Project Manager, or which you have added to it (via the 'Add Existing...' command). Right-clicking in the projects list brings up a context menu with the following commands:

![](http://www.timcrowson.com/wp-content/uploads/2014/07/projectsMenu.jpg)

* **Set Selected As Current** - Tells Modo to set the selected project as the active one. This will update the project title in Modo's main menu bar, and set default paths for file requesters.
* **Open Project Folder** - Opens the project's root directory in a new OS window.
* **Add Existing Project To List** - If a project has already been created, and you simply want to include it in your list of existing projects, this command will let you do that. The target directory must be a valid Modo project.
* **Remove Selected** - Removes the project from the list. This does not delete anything on disk, but merely removes the entry from the list of existing projects.

> Note:
> If a project path is invalid, the project will still appear in the list, but will be displayed in red. There is currently no mechanism for 're-linking' a project to a new path.

### The Scenes List
The list on the right shows scene files belonging to the selected project. You can control which file types show up in the scenes list by using the `Filetypes...` button. Clicking on this button will display a menu listing all the filetypes Modo can import. By default, only the '.lxo' format is checked on, meaning that only native Modo scene files will be displayed in the list. Checking other formats will cause the list to update to include file types matching the checked formats.

> Note:
> With the `Filetypes...` menu open, holding the Shift key down will allow you check/uncheck multiple file types without closing the menu.

Right-clicking on a file in the scenes list brings up a context menu with the following commands:

![](http://www.timcrowson.com/wp-content/uploads/2014/07/scenesMenu.jpg)

* **Open Selected** - Opens the selected file in Modo.
* **Import Selected** - Imports the selected file into the currently open scene.
* **Import Selected As Referenced** - Imports the selected file as referenced into the currently open scene. Running this will be followed by the standard Modo dialog for referenced imports.
* **Open Scene Folder** - Opens the selected file's folder in a new OS window .


# New Project
The `New Project` tab allows you to create a new project and to specify what kind of directory structure to create for it, if any.

![](http://www.timcrowson.com/wp-content/uploads/2014/07/newTab.jpg)

### Set the Project Root
The first step is to choose a root location for the new project. Clicking on the `...` button will bring up a file browser to let you choose or create the project root folder. Whatever folder you choose will be the name of the project.
> Note:
> The Project Manager kit differs here from the standard Modo way. The native Modo workflow is to choose a directory, and then set a name separately. Modo will then create a folder with that name inside the path you specified. The Project Manager kit does not operate this way, and instead combines both of those steps into one. Whatever path you set in the `Root Path` field will be the root of the project. Consequently the project name will be the name of the last folder in that path.

### Create Folders
The next step is to tell the kit what kind of folder structure it needs to create. Pipelines and workflows differ widely, and therefore so do project directory structures. The Project Manager kit does not seek to impose any specific structure, but instead allows you to create structure templates that can be saved, edited, and used by the Project Manager to create folders on disk.
> Note:
> By default the `Create Folders` option is off. Leaving it this way will prevent any folders from being created at all, effectively resulting in an empty project root, apart from the requisite '.luxproject' file required for identifying the directory as a valid Modo project. Likewise, if `Create Folders` is enabled but the structure tree is empty at the time of creation, the result will be the same: an empty project root.

To get started, click on the 'New Template' button on the right, and choose a name for your template...
![](http://www.timcrowson.com/wp-content/uploads/2014/07/newTemplate.jpg)


Once you've done this, you'll be ready to start building your template. The buttons along the right offer the following commands:
* **Add New Folder** - This will add a new folder at the root level of the template tree, called `__NEW FOLDER__`.
* **Remove Folders** - This will remove the selected folders from the tree. This is not undoable!
* **Reset Tree** - This dramatic command wipes the contents of the tree entirely. Don't worry, it asks you first.
* **Save Template** - Saves the template. Behind the scenes, the kit writes the template to an XML file on disk, inside the kit directory, in `ProjectManager/data/templates/`
* **Save Template As** - Save the current template as a new one, with a new name.

> Note:
> There is currently no undo system or intelligent management of changes made to a template. If you switch to another template without saving, your changes will be lost.

Use the following behaviors to customize your structure template:
* Double-click a folder at any time to rename it. As you rename folders in the tree, they will automatically sort alphabetically.
* Drag and drop folders on top of each other to create hierachies.
* Use the Add/Remove buttons along the right any time you like.

### Create the Project
Once you are ready to create your project, press the `Create Project` button. The following will happen:
* A new Modo project will be created at the specified root
* It will be set as the current project
* It will also be added to the project list
* If the `Create Folders` option is checked, and a non-empty template is selected, corresponding folders will be created on disk.

> Note:
> If folders or files already exist at the target location, they are left alone. This kit does not delete or rename anything inside a project directory on disk.
