import re
import json
from faster_whisper import WhisperModel

model = WhisperModel('tiny', device='cpu', compute_type='int8', cpu_threads=2)

print("Transcribing Test 3 Part 1...")
segs, _ = model.transcribe('web/assets/audio/test3/part1.mp3')
p1_segs = [{'start': round(s.start, 2), 'end': round(s.end, 2), 'text': s.text.strip()} for s in segs]

for s in p1_segs:
    if 'number' in s['text'].lower() or 'part 1' in s['text'].lower() or 'begin' in s['text'].lower():
        print(f"{s['start']} - {s['end']}: {s['text']}")
