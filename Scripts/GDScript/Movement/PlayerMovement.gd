extends Spatial

export var Movespeed = 0.1
onready var path = $Path1
onready var pathLeft = $Path1/PathL
onready var pathRight = $Path1/PathR
onready var player = $Path1/Player
onready var camAnimation = $Path1/Player/PlayerComponents/Camera/AnimationPlayer
onready var world = $"."
onready var handtracking = preload("res://Scenes/Test.tscn")
var cnit = true
# Called when the node enters the scene tree for the first time.
func _ready():
	#showCam()
	pass
func _process(delta):
	if player.unit_offset < 1:
		player.unit_offset += Movespeed * delta
		camAnimation.play("HeadBob")
	else:
		camAnimation.stop()
		checkInput()
	#showCam()
	
func checkInput():
	if Input.is_action_just_pressed("ui_left"):
		turnDirection("Left")
	elif Input.is_action_just_pressed("ui_right"):
		turnDirection("Right")
	else:
		pass
	
func turnDirection(tdir):
	var parent = player.get_parent()
	if parent.get_child_count() > 1:
		parent.remove_child(player)
		if 	tdir == "Left":
			parent.find_node("PathL").add_child(player)
		elif tdir == "Right":
			parent.find_node("PathR").add_child(player)
		player.unit_offset = 0
		
#func showCam():
#	if cnit == true:
#		if Input.is_action_just_pressed("ui_accept"):
#			var instancedScene = handtracking.instance()
#			world.add_child(instancedScene)
#			cnit = false
