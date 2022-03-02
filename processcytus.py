import json

TIME_BASE = "time_base"
START_TICK = "start_tick"
END_TICK = "end_tick"
SCAN_LINE_DIRECTION = "scan_line_direction"
DOWN = -1
TEMPO_LIST = "tempo_list"
TICK = "tick"
VALUE = "value"

def is_tick_in_page(tick, page):
	return page[START_TICK]<=tick<=page[END_TICK]

def get_page_at_tick(beatmap, tick):
	for page in beatmap["page_list"]:
		if is_tick_in_page(tick, page):
			return page

def get_y_at_tick(beatmap, tick):
	page = get_page_at_tick(beatmap, tick)
	fraction = (tick - page[START_TICK])/(page[END_TICK]-page[START_TICK])
	if page[SCAN_LINE_DIRECTION] == DOWN:
		fraction=1-fraction
	return fraction

def tempo_to_bpm(tempo):
	return 60000000 / tempo

def ticks_to_ms(tick, time_base, tempo):
	return (tick / time_base) * tempo / 1000

def tick_timestamp_to_ms(beatmap, tick):
	i = -2
	total_ms = 0
	ticks_passed = 0
	for temposet in beatmap[TEMPO_LIST]+[{"tick":tick}]:
		i+=1
		if i==-1:
			continue
		if temposet[TICK]>=tick:
			rel = tick-ticks_passed
			ticks_passed = tick
		else:
			rel = temposet[TICK]-ticks_passed
			ticks_passed = temposet[TICK]
		total_ms+=ticks_to_ms(rel,beatmap[TIME_BASE], beatmap[TEMPO_LIST][i][VALUE])
		if temposet[TICK]>=tick:
			return total_ms
