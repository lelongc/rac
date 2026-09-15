import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

snippet = """
7
M-Au
Have the machines on the factory floor been
cleaned?
w-Am
(A) No, not yet.
(B) It’s in the shipping container.
(C) I just put it in the trash bin.
41444 7|7»5 427|44 442?
(A) 0LL|£, 0L40I2.
(B) 22^ 44 44014011142.
(C) 42E1|7|#0||^40|O _
"""

# Extract prompt: lines between question number and (A)
lines = [l.strip() for l in snippet.split("\n") if l.strip()]
prompt_lines = []
for l in lines[1:]:
    if l.startswith("(A)"):
        break
    if not re.match(r"^[MW]-[A-Za-z]+$", l):
        prompt_lines.append(l)

prompt = " ".join(prompt_lines)
print("Prompt:", prompt)

# Extract options (A), (B), (C) - FIRST match only, ASCII only
opts = {}
for l in lines:
    m = re.match(r"^\(([ABC])\)\s*([A-Za-z][^\n\r]+)", l)
    if m:
        letter = m.group(1)
        if letter not in opts:
            # Check ASCII
            t = m.group(2).strip()
            if sum(1 for c in t if c.isascii()) / len(t) > 0.8:
                opts[letter] = t

print("Opts:", opts)
