from mcpi.minecraft import Minecraft
Aerin = Minecraft.create()
while True:
    hits = Aerin.events.pollProjectileHits()
    if len(hits) > 0 :
        a = hits[0]
        x,y,z = a.pos.x,a.pos.y,a.pos.z
        
        Aerin.player.setTilePos(x,y,z)
        Aerin.spawnEntity(x,y,z,99)