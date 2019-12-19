import json

from PIL import Image

def extrude(image, sprites):
	im = Image.open(image)
	pixels = im.load()
	atlas = json.load(open(sprites, "r"))

	for frame in atlas["frames"]:
		x = atlas["frames"][frame]["frame"]["x"]
		y = atlas["frames"][frame]["frame"]["y"]
		width = atlas["frames"][frame]["sourceSize"]["w"]
		height = atlas["frames"][frame]["sourceSize"]["h"]

		for y in range(y, y + height):
			pixels[x - 1, y] = pixels[x, y]
			pixels[x + width, y] = pixels[x + width - 1, y]

		for x in range(x, x + width):
			pixels[x, y + 1] = pixels[x, y]
			pixels[x, y - height] = pixels[x, y - height + 1]

	im.save(image)
