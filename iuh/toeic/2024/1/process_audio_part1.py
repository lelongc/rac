# process_audio_part1.py: Transcribe Part 1 and extract question timestamps
from faster_whisper import WhisperModel
import subprocess
import os

model = WhisperModel('tiny', device='cpu', compute_type='int8')
segments, info = model.transcribe('web/assets/audio/part1.mp3')

segs = list(segments)
print(f"Total segments: {len(segs)}")

for s in segs:
    print(f"{s.start:6.2f} - {s.end:6.2f}: {s.text}")
