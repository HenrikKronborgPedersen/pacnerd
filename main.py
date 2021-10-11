@namespace
class SpriteKind:
    BigDots = SpriteKind.create()
    Victim = SpriteKind.create()
def createPacNerd():
    global PacNerd
    PacNerd = sprites.create(img("""
            . . . . . . . 2 . . . . . . . . 
                    . . . . . 2 2 2 2 2 . . . . . . 
                    . . . . 2 2 . . . 2 . . . . . . 
                    . . . . 2 . f . f . 2 . . . . . 
                    . . . . 2 2 . . . . 2 . . . . . 
                    . . . . . 2 2 2 2 2 2 . . . . . 
                    . . 2 2 . . 2 2 2 2 . . . . . . 
                    . . . 2 2 2 2 . . . . 2 . . . . 
                    . . . . . . 2 2 2 2 2 . . . . . 
                    . . . . . . . 2 . . . . . . . . 
                    . . . . . . 2 2 . . . . . . . . 
                    . . . . . 2 2 . 2 2 . . . . . . 
                    . . . . . 2 . . . 2 2 . . . . . 
                    . . . . . . . . . . . 2 . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKind.player)
    PacNerd.set_position(10, 105)
    controller.move_sprite(PacNerd)

def on_on_overlap(sprite, otherSprite):
    global ghost1, ghost2
    if otherSprite == ghost1:
        ghost1 = sprites.create(img("""
                . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . 5 5 5 5 . . . . . . . 
                            . . . . . 5 5 5 5 5 5 . . . . . 
                            . . . . 5 5 5 5 5 5 5 . . . . . 
                            . . . 5 5 5 5 5 5 5 5 5 . . . . 
                            . . . 5 5 f 5 5 5 f 5 5 . . . . 
                            . . . 5 5 f 5 5 5 f 5 5 . . . . 
                            . . 5 5 5 5 5 5 5 5 5 5 5 . . . 
                            . . 5 5 5 5 5 5 5 5 5 5 5 . . . 
                            . 5 5 5 5 5 5 5 5 5 5 5 5 . . . 
                            . 5 5 5 5 5 5 5 5 5 5 5 5 . . . 
                            . 5 5 5 5 5 5 5 5 5 5 5 5 5 . . 
                            . 5 . 5 5 . 5 5 . 5 5 . 5 5 . . 
                            . 5 . 5 . . 5 . . . 5 . 5 5 . . 
                            . . . . . . . . . . . . . . . .
            """),
            SpriteKind.enemy)
        ghost1.set_position(148, 6)
        ghost1.set_kind(SpriteKind.enemy)
        ghost1.follow(PacNerd, 30)
    if otherSprite == ghost2:
        ghost2 = sprites.create(img("""
                . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . 7 7 7 7 . . . . . . . 
                            . . . . . 7 7 7 7 7 7 . . . . . 
                            . . . . 7 7 7 7 7 7 7 . . . . . 
                            . . . 7 7 7 7 7 7 7 7 7 . . . . 
                            . . . 7 7 f 7 7 7 f 7 7 . . . . 
                            . . . 7 7 f 7 7 7 f 7 7 . . . . 
                            . . 7 7 7 7 7 7 7 7 7 7 7 . . . 
                            . . 7 7 7 7 7 7 7 7 7 7 7 . . . 
                            . 7 7 7 7 7 7 7 7 7 7 7 7 . . . 
                            . 7 7 7 7 7 7 7 7 7 7 7 7 . . . 
                            . 7 7 7 7 7 7 7 7 7 7 7 7 7 . . 
                            . 7 . 7 7 . 7 7 . 7 7 . 7 7 . . 
                            . 7 . 7 . . 7 . . . 7 . . 7 . . 
                            . . . . . . . . . . . . . . . .
            """),
            SpriteKind.enemy)
        ghost2.set_position(148, 6)
        ghost2.set_kind(SpriteKind.enemy)
        ghost2.follow(PacNerd, 40)
    info.change_score_by(10)
    otherSprite.destroy(effects.fire, 500)
sprites.on_overlap(SpriteKind.player, SpriteKind.Victim, on_on_overlap)

def on_on_overlap2(sprite2, otherSprite2):
    otherSprite2.destroy(effects.spray, 500)
    ghost1.set_kind(SpriteKind.Victim)
    ghost1.follow(PacNerd, 0)
    ghost1.start_effect(effects.spray, 10000)
    ghost2.set_kind(SpriteKind.Victim)
    ghost2.follow(PacNerd, 0)
    ghost2.start_effect(effects.spray, 10000)
    pause(10000)
    ghost1.set_kind(SpriteKind.enemy)
    ghost1.follow(PacNerd, 30)
    ghost2.set_kind(SpriteKind.enemy)
    ghost2.follow(PacNerd, 40)
sprites.on_overlap(SpriteKind.player, SpriteKind.BigDots, on_on_overlap2)

def createDots():
    global dot1
    for value in tiles.get_tiles_by_type(assets.tile("""
        myTile1
    """)):
        dot1 = sprites.create(img("""
                . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . 1 1 . . . . . . . 
                            . . . . . . . 1 1 . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . .
            """),
            SpriteKind.food)
        tiles.place_on_tile(dot1, value)
    for value2 in tiles.get_tiles_by_type(assets.tile("""
        myTile2
    """)):
        dot1 = sprites.create(img("""
                . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . 1 1 . . . . . . . 
                            . . . . . . . 1 1 . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . .
            """),
            SpriteKind.food)
        tiles.place_on_tile(dot1, value2)
    for value3 in tiles.get_tiles_by_type(assets.tile("""
        myTile3
    """)):
        dot1 = sprites.create(img("""
                . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . 1 1 . . . . . . . 
                            . . . . . . . 1 1 . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . .
            """),
            SpriteKind.food)
        tiles.place_on_tile(dot1, value3)
    for value4 in tiles.get_tiles_by_type(assets.tile("""
        myTile4
    """)):
        dot1 = sprites.create(img("""
                . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . 1 1 . . . . . . . 
                            . . . . . . . 1 1 . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . .
            """),
            SpriteKind.food)
        tiles.place_on_tile(dot1, value4)
    for value5 in tiles.get_tiles_by_type(assets.tile("""
        myTile
    """)):
        dot1 = sprites.create(img("""
                . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . 1 1 . . . . . . . 
                            . . . . . . . 1 1 . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . .
            """),
            SpriteKind.food)
        tiles.place_on_tile(dot1, value5)
    for value6 in tiles.get_tiles_by_type(assets.tile("""
        myTile0
    """)):
        dot1 = sprites.create(img("""
                . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . 1 1 . . . . . . . 
                            . . . . . . . 1 1 . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . .
            """),
            SpriteKind.food)
        tiles.place_on_tile(dot1, value6)
    for value7 in tiles.get_tiles_by_type(assets.tile("""
        myTile5
    """)):
        dot1 = sprites.create(img("""
                . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . 1 1 . . . . . . . 
                            . . . . . . . 1 1 . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . .
            """),
            SpriteKind.food)
        tiles.place_on_tile(dot1, value7)
    for value8 in tiles.get_tiles_by_type(assets.tile("""
        transparency16
    """)):
        dot1 = sprites.create(img("""
                . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . 1 1 . . . . . . . 
                            . . . . . . . 1 1 . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . .
            """),
            SpriteKind.food)
        tiles.place_on_tile(dot1, value8)
def createMonsters():
    global ghost1, ghost2
    ghost1 = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . 5 5 5 5 . . . . . . . 
                    . . . . . 5 5 5 5 5 5 . . . . . 
                    . . . . 5 5 5 5 5 5 5 . . . . . 
                    . . . 5 5 5 5 5 5 5 5 5 . . . . 
                    . . . 5 5 f 5 5 5 f 5 5 . . . . 
                    . . . 5 5 f 5 5 5 f 5 5 . . . . 
                    . . 5 5 5 5 5 5 5 5 5 5 5 . . . 
                    . . 5 5 5 5 5 5 5 5 5 5 5 . . . 
                    . 5 5 5 5 5 5 5 5 5 5 5 5 . . . 
                    . 5 5 5 5 5 5 5 5 5 5 5 5 . . . 
                    . 5 5 5 5 5 5 5 5 5 5 5 5 5 . . 
                    . 5 . 5 5 . 5 5 . 5 5 . 5 5 . . 
                    . 5 . 5 . . 5 . . . 5 . 5 5 . . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKind.enemy)
    ghost1.set_position(148, 6)
    ghost1.set_kind(SpriteKind.enemy)
    ghost1.follow(PacNerd, 30)
    ghost2 = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . 7 7 7 7 . . . . . . . 
                    . . . . . 7 7 7 7 7 7 . . . . . 
                    . . . . 7 7 7 7 7 7 7 . . . . . 
                    . . . 7 7 7 7 7 7 7 7 7 . . . . 
                    . . . 7 7 f 7 7 7 f 7 7 . . . . 
                    . . . 7 7 f 7 7 7 f 7 7 . . . . 
                    . . 7 7 7 7 7 7 7 7 7 7 7 . . . 
                    . . 7 7 7 7 7 7 7 7 7 7 7 . . . 
                    . 7 7 7 7 7 7 7 7 7 7 7 7 . . . 
                    . 7 7 7 7 7 7 7 7 7 7 7 7 . . . 
                    . 7 7 7 7 7 7 7 7 7 7 7 7 7 . . 
                    . 7 . 7 7 . 7 7 . 7 7 . 7 7 . . 
                    . 7 . 7 . . 7 . . . 7 . . 7 . . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKind.enemy)
    ghost2.set_position(148, 6)
    ghost2.set_kind(SpriteKind.enemy)
    ghost2.follow(PacNerd, 40)

def on_on_overlap3(sprite3, otherSprite3):
    global dotCount
    otherSprite3.destroy()
    dotCount += 1
    info.change_score_by(1)
    if dotCount == 49:
        game.over(True)
sprites.on_overlap(SpriteKind.player, SpriteKind.food, on_on_overlap3)

def createBigDots():
    global dot2
    dot2 = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . 1 1 . . . . . . . 
                    . . . . . . 1 1 1 1 . . . . . . 
                    . . . . . 1 1 1 1 1 1 . . . . . 
                    . . . . . 1 1 1 1 1 1 . . . . . 
                    . . . . . . 1 1 1 1 . . . . . . 
                    . . . . . . . 1 1 . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKind.BigDots)
    dot2.set_position(8, 40)
    dot2 = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . 1 1 . . . . . . . 
                    . . . . . . 1 1 1 1 . . . . . . 
                    . . . . . 1 1 1 1 1 1 . . . . . 
                    . . . . . 1 1 1 1 1 1 . . . . . 
                    . . . . . . 1 1 1 1 . . . . . . 
                    . . . . . . . 1 1 . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKind.BigDots)
    dot2.set_position(152, 40)

def on_on_overlap4(sprite4, otherSprite4):
    game.over(False)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap4)

dot2: Sprite = None
dot1: Sprite = None
ghost2: Sprite = None
ghost1: Sprite = None
PacNerd: Sprite = None
dotCount = 0
tiles.set_tilemap(tilemap("""
    level1
"""))
createPacNerd()
createMonsters()
createDots()
createBigDots()
dotCount = 0
info.set_score(0)