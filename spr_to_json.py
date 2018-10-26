import json

SCORE_ID = "midi_cleaned"
PERFORM_ID = 'Ali01'

SPR_FILE_SCORE = 'examples/{}_spr.txt'.format(SCORE_ID)
OUT_FILE_SCORE = '{}_spr.json'.format(SCORE_ID)

SPR_FILE_PER = 'examples/{}_spr.txt'.format(PERFORM_ID)
OUT_FILE_PER = '{}_spr.json'.format(PERFORM_ID)

CORR_FILE = 'examples/{}_corresp.txt'.format(PERFORM_ID)


def time_to_tick(time, tempo=216):
  return round(time*tempo)

def pitch_to_midi_pitch(step, alter, octave):
  """Convert MusicXML pitch representation to MIDI pitch number."""
  pitch_class = 0
  if step == 'C':
    pitch_class = 0
  elif step == 'D':
    pitch_class = 2
  elif step == 'E':
    pitch_class = 4
  elif step == 'F':
    pitch_class = 5
  elif step == 'G':
    pitch_class = 7
  elif step == 'A':
    pitch_class = 9
  elif step == 'B':
    pitch_class = 11
  else:
    pass
  pitch_class = (pitch_class + int(alter))
  midi_pitch = (12 + pitch_class) + (int(octave) * 12)
  return midi_pitch


def midi_pitch_to_pitch(midi_pitch):
  octave = (midi_pitch - 12) // 12
  step = midi_pitch % 12
  pitch = None
  if step == 0:
    pitch = 'C'
  elif step == 1:
    pitch = 'C#'
  elif step == 2:
    pitch = 'D'
  elif step == 3:
    pitch = 'D#'
  elif step == 4:
    pitch = 'E'
  elif step == 5:
    pitch = 'F'
  elif step == 6:
    pitch = 'F#'
  elif step == 7:
    pitch = 'G'
  elif step == 8:
    pitch = 'G#'
  elif step == 9:
    pitch = 'A'
  elif step == 10:
    pitch = 'A#'
  elif step == 11:
    pitch = 'B'
  return pitch + str(octave)


match = open(CORR_FILE, 'r')
f = match.readlines()
match.close()

match_list = []

for n in range(1, len(f)):
  line = f[n]
  elements = line.split()

  perform_id = elements[0]
  if perform_id == '*':
    continue

  score_id = elements[5]
  match_list.append((perform_id, score_id))

################################

spr_file_perform = open(SPR_FILE_PER, 'r')
f = spr_file_perform.readlines()
spr_file_perform.close()

j_data = {}
j_data["header"] = {"name":  "{}_spr".format(SCORE_ID)}

notes = []

for n in range(1, len(f)):
  line = f[n]
  elements = line.split()
  if len(elements) != 7:
    continue
  id = elements[0]
  midiNote = elements[3]
  if len(midiNote) == 3:
    if midiNote[1] == 'b':
      alter = -1
    else:
      alter = 1
  else:
    alter = 0
  midi_pitch = pitch_to_midi_pitch(midiNote[0], alter, midiNote[-1])
  note = midi_pitch_to_pitch(midi_pitch)
  duration = "{:.3f}".format(float(elements[2]) - float(elements[1]))
  note_dict = {}
  note_dict["id"] = id
  note_dict["matchID"] = match_list[n-1][1]
  note_dict["time"] = elements[2]
  note_dict["midiNote"] = midi_pitch
  note_dict["note"] = note
  note_dict["duration"] = duration
  note_dict["velocity"] = elements[4]
  notes.append(note_dict)

j_data["notes"] = notes

with open(OUT_FILE_PER, 'w') as outfile:
  json.dump(j_data, outfile)

#####################################

spr_file_score = open(SPR_FILE_SCORE, 'r')
f = spr_file_score.readlines()
spr_file_score.close()

j_data = {}
j_data["header"] = {"name":  "{}_spr".format(SCORE_ID)}

notes = []

out_file = open(OUT_FILE_SCORE, 'w')

for n in range(1, len(f)):
  line = f[n]
  elements = line.split()
  if len(elements) != 7:
    continue
  id = elements[0]
  midiNote = elements[3]
  if len(midiNote) == 3:
    if midiNote[1] == 'b':
      alter = -1
    else:
      alter = 1
  else:
    alter = 0
  midi_pitch = pitch_to_midi_pitch(midiNote[0], alter, midiNote[-1])
  note = midi_pitch_to_pitch(midi_pitch)
  duration = "{:.3f}".format(float(elements[2]) - float(elements[1]))
  note_dict = {}
  note_dict["id"] = id
  note_dict["time"] = elements[2]
  note_dict["midiNote"] = midi_pitch
  note_dict["note"] = note
  note_dict["duration"] = duration
  note_dict["velocity"] = elements[4]
  notes.append(note_dict)

# notes = sorted(notes, key=lambda x: int(x["time"][:-1]))
j_data["notes"] = notes

with open(OUT_FILE_SCORE, 'w') as outfile:
  json.dump(j_data, outfile)




# "time":"0i","midiNote":43,"note":"G2","velocity":1,"duration":"24i"}