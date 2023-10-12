from godot import exposed, export
from godot import *

@exposed
class TextureChange(Node):
	def _ready(self):
		try:
			# Create a new ImageTexture object
			tex = ImageTexture()

			# Load the image from the file
			tex.load("res://icon.png")  # Adjust the path to the actual location of your image

			# Get a reference to the TextureRect node
			self.texture_rect = self.get_node("/root/Spatial/TextureRect")  # Set the appropriate path to your TextureRect
			if self.texture_rect:
				# Assign the texture to the TextureRect
				self.texture_rect.texture = tex
			else:
				print("TextureRect not found. Make sure the path is correct.")
		except Exception as e:
			print("Error loading the image:", e)
