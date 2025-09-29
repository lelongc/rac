# -*- coding: utf-8 -*-
"""
Module 6 — Analog Video: NTSC vs PAL (quick facts).
Spyder: press F5 to print notes to the console.
"""
def main():
    print("[M6] Analog Video (NTSC vs PAL) — Quick Facts")
    print("  NTSC: 525 lines, ~29.97 fps, color subcarrier 3.579545 MHz.")
    print("  PAL : 625 lines, 25 fps, color subcarrier 4.43361875 MHz.")
    print("  Both historically interlaced; Y (luma) had higher bandwidth than chroma.")
    print("  YIQ used by NTSC (I,Q); PAL typically YUV.")
    print("[M6] Tip: Try Module 5 to *feel* interlaced fields.")

if __name__ == "__main__":
    main()
