extends Spatial


onready var screensize = OS.get_screen_size() 
onready var viewporth =  ProjectSettings.get_setting("display/window/size/width")

func _ready():
	OS.window_position = Vector2(0,(screensize.y/2)-(viewporth/3))
	
