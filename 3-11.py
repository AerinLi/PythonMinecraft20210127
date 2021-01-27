from mcpi.minecraft import Minecraft
Aerin = Minecraft.create()
x,y,z = Aerin.player.getPos()
number = 1
for i in range(8):
    for j in range(number):
        Aerin.spawnEntity(x,y,z,60)
    number = number*2
    Aerin.postToChat("這次生成了"+str(number)+" 隻蠹魚 ")
