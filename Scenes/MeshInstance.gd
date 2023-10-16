extends MeshInstance

var velocity = Vector2(200,200)
var position
func _ready():
	pass # Replace with function body.



func _physics_process(delta):
	move(delta)
	
func move(delta):
	position += velocity * delta
	
