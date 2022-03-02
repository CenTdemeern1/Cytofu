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
for hitobject in beatmap["note_list"]:
	print(makeosu.make_hitobject(
		(hitobject["x"]*makeosu.WIDTH)+makeosu.XOFF,
		((1-processcytus.get_y_at_tick(beatmap, hitobject["tick"]))*makeosu.HEIGHT)+makeosu.YOFF,
		processcytus.tick_timestamp_to_ms(beatmap,hitobject["tick"])
		))
