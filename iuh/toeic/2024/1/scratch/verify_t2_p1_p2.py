import whisper

model = whisper.load_model('tiny')
print("--- TEST 2 PART 1 ---")
res1 = model.transcribe('web/assets/audio/test2/part1.mp3')
for s in res1['segments']:
    print(f"{s['start']:.2f} - {s['end']:.2f}: {s['text']}")

print("\n--- TEST 2 PART 2 ---")
res2 = model.transcribe('web/assets/audio/test2/part2.mp3')
for s in res2['segments']:
    print(f"{s['start']:.2f} - {s['end']:.2f}: {s['text']}")
