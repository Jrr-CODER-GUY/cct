def on_on_chat():
    castles.build_castle_tower(1000, 1000, TNT, player.position())
player.on_chat("Hi", on_on_chat)

def on_on_chat2():
    castles.build_castle_tower(1000, 1000, FIRE, player.position())
player.on_chat("Now", on_on_chat2)
