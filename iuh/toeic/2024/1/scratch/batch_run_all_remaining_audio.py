import sys
import time
BASE_DIR = r"d:\folder\rac\iuh\toeic\2024\1"
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from faster_whisper import WhisperModel
from scratch.batch_process_audio_test import process_test

def main():
    print("Initializing Whisper model (tiny, int8, cpu_threads=2)...", flush=True)
    model = WhisperModel('tiny', device='cpu', compute_type='int8', cpu_threads=2)
    
    tests_to_process = [5, 6, 7, 8, 9, 10]
    total = len(tests_to_process)
    
    for idx, t in enumerate(tests_to_process, 1):
        print(f"\n==========================================", flush=True)
        print(f"   [{idx}/{total}] STARTING TEST {t} AUDIO   ", flush=True)
        print(f"==========================================", flush=True)
        t0 = time.time()
        process_test(t, model)
        elapsed = time.time() - t0
        print(f"Completed Test {t} in {elapsed:.1f}s!", flush=True)
        time.sleep(2) # Cool down CPU slightly
        
    print("\nALL REMAINING TESTS (4 to 10) AUDIO CLIPS PROCESSED SUCCESSFULLY!", flush=True)

if __name__ == "__main__":
    main()
