XOFF = 32       # \ Screen boundaries (osupixels)
YOFF = 32       # |
WIDTH = 448    # |
HEIGHT = 320   # /

def bpm_to_beatlength(bpm):
	return (1 / (bpm / 60)) * 1000

def make_timingpoint(time:int, beatLength:float, meter:int=1, sampleSet:int=0b0000, sampleIndex:int=0, volume:int=100, uninherited:bool=True, effects:int=0b0000):
	return "{},{},{},{},{},{},{},{}".format(int(time),float(beatLength),int(meter),int(sampleSet),int(sampleIndex),int(volume),int(uninherited),int(effects))

def make_hitobject(x:int, y:int, time:int, type:int=0b00000001, hitSound:int=0b0001, objectParams:list=[]):
	out=[int(x),int(y),int(time),int(type),int(hitSound)]
	out+=objectParams
	outstr=[]
	for i in out:
		outstr.append(str(i))
	return ",".join(outstr)
