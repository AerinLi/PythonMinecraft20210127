from mcpi.minecraft import Minecraft
import random,time
Aerin = Minecraft.create()
while True:
    x,y,z = Aerin.player.getTilePos()
    color = random.randrange(0,9)
    Aerin.setBlock(x,y,z,38,color)
    time.sleep(1)
    