extends Spatial

var scene_to_instance = preload("res://Scenes/ball1.tscn")
onready var player = $Camera2
func instance_object():
	var object = scene_to_instance.instance()
	player.add_child(object)
	object.translate(Vector3(0,0,-10))
func clickInput():
	if Input.is_action_just_pressed("Click"):
		instance_object()

func _process(delta):
	clickInput()
