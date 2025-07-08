player.onChat("Hi", function () {
    castles.buildCastleTower(
    1000,
    1000,
    TNT,
    player.position()
    )
})
player.onChat("Now", function () {
    castles.buildCastleTower(
    1000,
    1000,
    FIRE,
    player.position()
    )
})
