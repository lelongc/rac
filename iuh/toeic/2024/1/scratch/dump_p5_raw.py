import json, sys
sys.stdout.reconfigure(encoding='utf-8')

for t in [4, 5]:
    cols = json.load(open(f'scratch/p5_columns_test{t}.json', encoding='utf-8'))
    print(f'=== Test {t} Raw Text in Columns ===')
    for i, c in enumerate(cols):
        print(f'-- Col {i}:')
        for line in c['text'].splitlines():
            if line.strip():
                print('  ', line.strip())
