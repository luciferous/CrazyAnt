
constants = """
SIZE
FILE
FONT
LEVELS
LEVEL_DATA
PLAYER
ENEMY
TILE
BRICK
TITLE
LEFT
RIGHT
JUMP
CONTROLS
""".strip()

globs = globals()
for constant in constants.split():
	globs[constant] = constant
