XOFF = 32		# \ Screen boundaries (osupixels)
YOFF = 32		# |
WIDTH = 448		# |
HEIGHT = 320	# /
SLIDER_MULTIPLIER = 1.4 #SliderMultiplier value as specified in the .osu file, can be found in the editor as "Slider Velocity"

HOLDCIRCLE_CHUNK = [[ 0, -4], [ 0, -4], [ 4,  0], [ 4,  0], [ 0,  4], [ 0,  4], [-4,  0], [-4,  0]]
HOLDCIRCLE_CHUNK_LENGTH = 17.5

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

def generate_chunk(x:int, y:int):
	return "|"+("|".join(list(":".join([str(point[0]+x),str(point[1]+y)]) for point in HOLDCIRCLE_CHUNK)))

def make_holdcircle(x:int, y:int, time:int, length:float, bpm: float, new_combo:bool = False):
	osupixels_per_beat = SLIDER_MULTIPLIER*100
	bpms = bpm/60000 #Beats per millisecond
	osupixel_length = length*bpms*osupixels_per_beat
	div = osupixel_length/HOLDCIRCLE_CHUNK_LENGTH
	chunks = "B"+(generate_chunk(x,y)*round(div+0.5)) #round(X+0.5) is equal to ceil(X)
	hotype = 0b00000010
	if new_combo:
		hotype|=0b00000100
	return make_hitobject(x,y,time,hotype,0,[chunks,1,osupixel_length])
