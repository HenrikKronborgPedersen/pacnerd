namespace SpriteKind {
    export const BigDots = SpriteKind.create()
    export const Victim = SpriteKind.create()
}
function createPacNerd () {
    PacNerd = sprites.create(img`
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
        `, SpriteKind.Player)
    PacNerd.setPosition(10, 105)
    controller.moveSprite(PacNerd)
}
sprites.onOverlap(SpriteKind.Player, SpriteKind.Victim, function (sprite, otherSprite) {
    if (otherSprite == ghost1) {
        ghost1 = sprites.create(img`
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
            `, SpriteKind.Enemy)
        ghost1.setPosition(148, 6)
        ghost1.setKind(SpriteKind.Enemy)
        ghost1.follow(PacNerd, 30)
    }
    if (otherSprite == ghost2) {
        ghost2 = sprites.create(img`
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
            `, SpriteKind.Enemy)
        ghost2.setPosition(148, 6)
        ghost2.setKind(SpriteKind.Enemy)
        ghost2.follow(PacNerd, 40)
    }
    info.changeScoreBy(10)
    otherSprite.destroy(effects.fire, 500)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.BigDots, function (sprite, otherSprite) {
    otherSprite.destroy(effects.spray, 500)
    ghost1.setKind(SpriteKind.Victim)
    ghost1.follow(PacNerd, 0)
    ghost1.startEffect(effects.spray, 10000)
    ghost2.setKind(SpriteKind.Victim)
    ghost2.follow(PacNerd, 0)
    ghost2.startEffect(effects.spray, 10000)
    pause(10000)
    ghost1.setKind(SpriteKind.Enemy)
    ghost1.follow(PacNerd, 30)
    ghost2.setKind(SpriteKind.Enemy)
    ghost2.follow(PacNerd, 40)
})
function createDots () {
    for (let value of tiles.getTilesByType(assets.tile`myTile1`)) {
        dot1 = sprites.create(img`
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
            `, SpriteKind.Food)
        tiles.placeOnTile(dot1, value)
    }
    for (let value of tiles.getTilesByType(assets.tile`myTile2`)) {
        dot1 = sprites.create(img`
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
            `, SpriteKind.Food)
        tiles.placeOnTile(dot1, value)
    }
    for (let value of tiles.getTilesByType(assets.tile`myTile3`)) {
        dot1 = sprites.create(img`
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
            `, SpriteKind.Food)
        tiles.placeOnTile(dot1, value)
    }
    for (let value of tiles.getTilesByType(assets.tile`myTile4`)) {
        dot1 = sprites.create(img`
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
            `, SpriteKind.Food)
        tiles.placeOnTile(dot1, value)
    }
    for (let value of tiles.getTilesByType(assets.tile`myTile`)) {
        dot1 = sprites.create(img`
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
            `, SpriteKind.Food)
        tiles.placeOnTile(dot1, value)
    }
    for (let value of tiles.getTilesByType(assets.tile`myTile0`)) {
        dot1 = sprites.create(img`
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
            `, SpriteKind.Food)
        tiles.placeOnTile(dot1, value)
    }
    for (let value of tiles.getTilesByType(assets.tile`myTile5`)) {
        dot1 = sprites.create(img`
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
            `, SpriteKind.Food)
        tiles.placeOnTile(dot1, value)
    }
    for (let value of tiles.getTilesByType(assets.tile`transparency16`)) {
        dot1 = sprites.create(img`
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
            `, SpriteKind.Food)
        tiles.placeOnTile(dot1, value)
    }
}
function createMonsters () {
    ghost1 = sprites.create(img`
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
        `, SpriteKind.Enemy)
    ghost1.setPosition(148, 6)
    ghost1.setKind(SpriteKind.Enemy)
    ghost1.follow(PacNerd, 30)
    ghost2 = sprites.create(img`
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
        `, SpriteKind.Enemy)
    ghost2.setPosition(148, 6)
    ghost2.setKind(SpriteKind.Enemy)
    ghost2.follow(PacNerd, 40)
}
sprites.onOverlap(SpriteKind.Player, SpriteKind.Food, function (sprite, otherSprite) {
    otherSprite.destroy()
    dotCount += 1
    info.changeScoreBy(1)
    if (dotCount == 49) {
        game.over(true)
    }
})
function createBigDots () {
    dot2 = sprites.create(img`
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
        `, SpriteKind.BigDots)
    dot2.setPosition(8, 40)
    dot2 = sprites.create(img`
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
        `, SpriteKind.BigDots)
    dot2.setPosition(152, 40)
}
sprites.onOverlap(SpriteKind.Player, SpriteKind.Enemy, function (sprite, otherSprite) {
    game.over(false)
})
let dot2: Sprite = null
let dot1: Sprite = null
let ghost2: Sprite = null
let ghost1: Sprite = null
let PacNerd: Sprite = null
let dotCount = 0
tiles.setTilemap(tilemap`level1`)
createPacNerd()
createMonsters()
createDots()
createBigDots()
dotCount = 0
info.setScore(0)
