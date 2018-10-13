import time
import datetime
from pythonosc import osc_message_builder
from pythonosc import udp_client
import argparse

candySize=15

def videoPaths(x):
    return {
       0: [globalVideoPath+"/00_0.mov", candySize ],
       1: [globalVideoPath+"/00_1.mov", candySize ],
       2: [globalVideoPath+"/00_2.mov", candySize ],
       3: [globalVideoPath+"/00_3.mov", candySize ],
       4: [globalVideoPath+"/01_0.mov", candySize ],
       5: [globalVideoPath+"/01_1.mov", candySize ],
       6: [globalVideoPath+"/01_2.mov", candySize ],
       7: [globalVideoPath+"/01_3.mov", candySize ],
       8: [globalVideoPath+"/02_0.mov", candySize ],
       9: [globalVideoPath+"/02_1.mov", candySize ],
       10: [globalVideoPath+"/02_2.mov", candySize ],
       11: [globalVideoPath+"/02_3.mov", candySize ],
       12: [globalVideoPath+"/03_0.mov", candySize ],
       13: [globalVideoPath+"/03_1.mov", candySize ],
       14: [globalVideoPath+"/03_2.mov", candySize ],
       15: [globalVideoPath+"/03_3.mov", candySize ],
       16: [globalVideoPath+"/04_0.mov", candySize ],
       17: [globalVideoPath+"/04_1.mov", candySize ],
       18: [globalVideoPath+"/04_2.mov", candySize ],
       19: [globalVideoPath+"/04_3.mov", candySize ],
       20: [globalVideoPath+"/05_0.mov", candySize ],
       21: [globalVideoPath+"/05_1.mov", candySize ],
       22: [globalVideoPath+"/05_2.mov", candySize ],
       23: [globalVideoPath+"/05_3.mov", candySize ],
       24: [globalVideoPath+"/06_0.mov", candySize ],
       25: [globalVideoPath+"/06_1.mov", candySize ],
       26: [globalVideoPath+"/06_2.mov", candySize ],
       27: [globalVideoPath+"/06_3.mov", candySize ],
       28: [globalVideoPath+"/07_0.mov", candySize ],
       29: [globalVideoPath+"/07_1.mov", candySize ],
       30: [globalVideoPath+"/07_2.mov", candySize ],
       31: [globalVideoPath+"/07_3.mov", candySize ],
       32: [globalVideoPath+"/08_0.mov", candySize ],
       33: [globalVideoPath+"/08_1.mov", candySize ],
       34: [globalVideoPath+"/08_2.mov", candySize ],
       35: [globalVideoPath+"/08_3.mov", candySize ],
       36: [globalVideoPath+"/09_0.mov", candySize ],
       37: [globalVideoPath+"/09_1.mov", candySize ],
       38: [globalVideoPath+"/09_2.mov", candySize ],
       39: [globalVideoPath+"/09_3.mov", candySize ],
       40: [globalVideoPath+"/10_0.mov", candySize ],
       41: [globalVideoPath+"/10_1.mov", candySize ],
       42: [globalVideoPath+"/10_2.mov", candySize ],
       43: [globalVideoPath+"/10_3.mov", candySize ],
       44: [globalVideoPath+"/11_0.mov", candySize ],
       45: [globalVideoPath+"/11_1.mov", candySize ],
       46: [globalVideoPath+"/11_2.mov", candySize ],
       47: [globalVideoPath+"/11_3.mov", candySize ],
       48: [globalVideoPath+"/12_0.mov", candySize ],
       49: [globalVideoPath+"/12_1.mov", candySize ],
       50: [globalVideoPath+"/12_2.mov", candySize ],
       51: [globalVideoPath+"/12_3.mov", candySize ],
    }.get(x, [globalVideoPath+"/00_0.mp4", 10 ])    # 9 is default if x not found

def playVideo(localtime):
    print(time.asctime(localtime))
    hour = localtime[3]%12
    if localtime[4] == 0:
        return videoPaths(4*hour)
    elif localtime[4] == 15:
        return videoPaths((4*hour)+1)
    elif localtime[4] == 30:
        return videoPaths((4*hour)+2)
    elif localtime[4] == 45:
        return videoPaths((4*hour)+3)
    else:
        return ["/LOOP.mov",10]
    
print("Shanghai Clock")
startTime = time.time()
localStartTime = time.localtime( startTime )
print("Started at: "+time.asctime(localStartTime))

globalVideoPath = "/home/pi/media"
isPlaying = False

parser = argparse.ArgumentParser()
parser.add_argument("--ip", default="127.0.0.1",  help="The ip of the OSC server")
parser.add_argument("--port", type=int, default=9000,  help="The port the OSC server is listening on")
args = parser.parse_args()
client = udp_client.SimpleUDPClient(args.ip, args.port)
client.send_message("/load", globalVideoPath )

currentPath=""
while True :
    path = playVideo(time.localtime( time.time() ))
    if( currentPath != path[0] ):
        currentPath = path[0]
        print("PLAY: "+globalVideoPath+path[0])
        client.send_message("/play", globalVideoPath+path[0] )
    time.sleep(15)