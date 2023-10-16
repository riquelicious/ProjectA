extends RigidBody

export var velocity: Vector3 = Vector3(0,0,30.0)
onready var viewportCenter = get_viewport().get_visible_rect().size
func _ready() -> void:
	pass


func _process(delta:float):
	apply_impulse(Vector3(0,0,0),Vector3(-0.80,1,-0.60))
	
	#apply_impulse(velocity.rotated(Vector3.UP, rotation.y), Vector3.ZERO)
	#var collision = contacts_reported
	#if collision < 1: return
	#self.queue_free()
