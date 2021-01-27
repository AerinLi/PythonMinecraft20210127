from mcpi.minecraft import Minecraft
Aerin = Minecraft.create()
x,y,z = Aerin.player.getTilePos()
for i in range(0,20):
    Aerin.setBlock(x+i+1,y-1,z+i,95,10)
    Aerin.setBlock(x+i+2,y-1,z+i,95,10)
    Aerin.setBlock(x+i+3,y-1,z+i,95,10)