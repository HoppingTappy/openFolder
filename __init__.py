import bpy
import bmesh
from pathlib import Path
import os

bl_info = {
	"name": "open folder",
	"author": "tappy",
	"version": (1, 0),
	"blender": (3, 4, 0),
	"location": "",
	"description": "各種フォルダを開く",
	"warning": "",
	"wiki_url": "",
	"tracker_url": "",
	"category": "Custom",
}

translationDict = {
	"en_US": {
		("*", "Open addons folder"):"Open addons folder",
		("*", "Open project folder"):"Open project folder",
		("*", "Open extensions folder"):"Open extensions folder",
	},
	"ja_JP": {
		("*", "Open addons folder"):"アドオンフォルダを開く",
		("*", "Open project folder"):"プロジェクトフォルダを開く",
		("*", "Open extensions folder"):"エクステンションフォルダを開く",
	}
}

class OpenAddonsFolder(bpy.types.Operator):
	bl_idname = "wm.open_addons_folder"
	bl_label = "Open addons folder"
	bl_description = "Open addons folder"
	bl_options = {"REGISTER"}

	def execute(self, context):
		p = Path(bpy.utils.user_resource("SCRIPTS")) / "addons"
		os.startfile(p)
		return {"FINISHED"}

class OpenProjectFolder(bpy.types.Operator):
	bl_idname = "wm.open_project_folder"
	bl_label = "Open project folder"
	bl_description = "Open project folder"
	bl_options = {"REGISTER"}

	@classmethod
	def poll(cls, context):
		return bpy.data.filepath != ""

	def execute(self, context):
		p = Path(bpy.data.filepath).parent
		os.startfile(p)
		return {"FINISHED"}

class OpenExtensionsFolder(bpy.types.Operator):
	bl_idname = "wm.open_extensions_folder"
	bl_label = "Open extensions folder"
	bl_description = "Open extensions folder"
	bl_options = {"REGISTER"}

	def execute(self, context):
		p = Path(bpy.utils.user_resource("EXTENSIONS")) / "user_default"
		os.startfile(p)
		return {"FINISHED"}

def addMenu(self, context):
	self.layout.separator()
	self.layout.operator(OpenProjectFolder.bl_idname, icon="FILE_FOLDER",text=bpy.app.translations.pgettext("Open project folder"))
	self.layout.operator(OpenAddonsFolder.bl_idname,   icon="FILE_FOLDER",text=bpy.app.translations.pgettext("Open addons folder"))
	self.layout.operator(OpenExtensionsFolder.bl_idname,   icon="FILE_FOLDER",text=bpy.app.translations.pgettext("Open extensions folder"))

classes = [
	OpenAddonsFolder,
	OpenProjectFolder,
	OpenExtensionsFolder,
]

def register():
	bpy.app.translations.register(__name__, translationDict)
	for c in classes:
		bpy.utils.register_class(c)
	bpy.types.TOPBAR_MT_file.append(addMenu)


def unregister():
	bpy.app.translations.unregister(__name__)
	bpy.types.TOPBAR_MT_file.remove(addMenu)
	for c in classes:
		bpy.utils.unregister_class(c)


if __name__ == "__main__":
	register()
