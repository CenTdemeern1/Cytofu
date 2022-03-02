import json
import processcytus
import makeosu

with open("map.json","r") as mapfile:
	beatmap = json.load(mapfile)

print("[TimingPoints]")
for timingpoint in beatmap["tempo_list"]:
	print(makeosu.make_timingpoint(
		processcytus.tick_timestamp_to_ms(beatmap,timingpoint["tick"]),
		makeosu.bpm_to_beatlength(processcytus.tempo_to_bpm(timingpoint["value"]))
		))

print("[HitObjects]")
last_page=-1
for hitobject in beatmap["note_list"]:
	new_combo=False
	if last_page != hitobject["page_index"]:
		last_page = hitobject["page_index"]
		new_combo=True
	if hitobject["type"] in (1,2):
		x=(hitobject["x"]*makeosu.WIDTH)+makeosu.XOFF
		y=((1-processcytus.get_y_at_tick(beatmap, hitobject["tick"]))*makeosu.HEIGHT)+makeosu.YOFF
		time=processcytus.tick_timestamp_to_ms(beatmap,hitobject["tick"])
		length=processcytus.tick_timestamp_to_ms(beatmap,hitobject["tick"]+hitobject["hold_tick"])-time
		bpm=processcytus.tempo_to_bpm(processcytus.get_tempo_at_tick(beatmap,hitobject["tick"]))
		print(makeosu.make_holdcircle(
			x,
			y,
			time,
			length,
			bpm,
			new_combo
			))
	else:
		x=(hitobject["x"]*makeosu.WIDTH)+makeosu.XOFF
		y=((1-processcytus.get_y_at_tick(beatmap, hitobject["tick"]))*makeosu.HEIGHT)+makeosu.YOFF
		time=processcytus.tick_timestamp_to_ms(beatmap,hitobject["tick"])
		hotype=0b00000001
		if new_combo:
			hotype|=0b00000100
		print(makeosu.make_hitobject(
			x,
			y,
			time,
			hotype
			))
