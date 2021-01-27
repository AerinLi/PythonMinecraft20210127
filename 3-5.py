from mcpi.minecraft import Minecraft
Aerin = Minecraft.create()
x,y,z = Aerin.player.getTilePos()
for i in range(0,20):
    Aerin.setBlock(x,y-1,z+i,95)
    