import mcpi.minecraft as minecraft
import mcpi.block as block
import time
import datetime

mc = minecraft.Minecraft.create()
while True:
    time.sleep(1)
    timeNow = datetime.datetime.now()
    pos = mc.player.getTilePos()
    hours = timeNow.hour
    minutes = timeNow.minute
    seconds = timeNow.second

    mc.postToChat("DebugChat                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            position: x = "+str(pos.x) +"  y = "+str(pos.y) +"  z = "+str(pos.z) + "                                realtime: hours = "+str(hours) + "  minutes = "+str(minutes) +"  secends = "+str(seconds))
