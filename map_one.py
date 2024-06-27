from tutorial import Block, HEIGHT

def map_og(block_size, fire, spike):
    list = [
        Block(0, HEIGHT - block_size * 2, block_size),
        Block(block_size * 3, HEIGHT - block_size * 4, block_size),
        fire,
        Block(block_size * 6, HEIGHT - block_size * 6, block_size),
        Block(block_size * 9, HEIGHT - block_size * 4, block_size),
        Block(block_size * 12, HEIGHT - block_size * 4, block_size),
        fire,
        Block(block_size * 15, HEIGHT - block_size * 6, block_size),
        Block(block_size * 18, HEIGHT - block_size * 4, block_size),
        Block(block_size * 21, HEIGHT - block_size * 2, block_size),
        Block(block_size * 24, HEIGHT - block_size * 4, block_size),
        Block(block_size * 27, HEIGHT - block_size * 6, block_size),
        Block(block_size * 30, HEIGHT - block_size * 6, block_size),
        Block(block_size * 33, HEIGHT - block_size * 4, block_size),
        Block(block_size * 36, HEIGHT - block_size * 2, block_size),
        Block(block_size * 39, HEIGHT - block_size * 4, block_size),
        Block(block_size * 42, HEIGHT - block_size * 6, block_size),
        Block(block_size * 45, HEIGHT - block_size * 4, block_size),
        Block(block_size * 48, HEIGHT - block_size * 2, block_size),
        Block(block_size * 51, HEIGHT - block_size * 4, block_size),
        Block(block_size * 54, HEIGHT - block_size * 6, block_size),
        Block(block_size * 57, HEIGHT - block_size * 6, block_size),
        Block(block_size * 60, HEIGHT - block_size * 4, block_size),
        Block(block_size * 63, HEIGHT - block_size * 2, block_size),
        Block(block_size * 66, HEIGHT - block_size * 4, block_size),
        Block(block_size * 69, HEIGHT - block_size * 6, block_size),
        Block(block_size * 72, HEIGHT - block_size * 4, block_size),
        Block(block_size * 75, HEIGHT - block_size * 2, block_size),
        Block(block_size * 78, HEIGHT - block_size * 4, block_size),
        Block(block_size * 81, HEIGHT - block_size * 6, block_size),
        Block(block_size * 84, HEIGHT - block_size * 4, block_size),
        Block(block_size * 87, HEIGHT - block_size * 2, block_size),
    ]

    return list
