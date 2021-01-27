from mcpi.minecraft import Minecraft
Aerin = Minecraft.create()
import random,time
while True:
    x,y,z = Aerin.player.getPos()
    a = random.uniform(-20,20)
    b = random.uniform(-20,20)
    y = y+3
    Aerin.spawnEntity(x+a,y,z+b,93)
    time.sleep(0.1)
    #/kill @e[type=chicken]


