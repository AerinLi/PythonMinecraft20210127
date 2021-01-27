from mcpi.minecraft import Minecraft
Aerin = Minecraft.create()
while True:
    hits = Aerin.events.pollBlockHits()
    if len(hits)>0:
        a = hits[0]
        x,y,z = a.pos.x,a.pos.y,a.pos.z
        block = Aerin.getBlock(x,y,z)
        Aerin.postToChat("你打到了"+str(block))
        if block == 1:
            Aerin.setBlock(x,y,z,41)