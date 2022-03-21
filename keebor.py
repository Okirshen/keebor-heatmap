import keyboard
import csv

keys = {}
last_key = ''

try:
    while True:
        key = keyboard.read_key()
        if key in keys and last_key != key:
            print(keys)
            keys[key] += 1
        else:
            keys[key] = 1
        last_key = key
except KeyboardInterrupt:
    keys = {key: val for key, val in sorted(keys.items(), key = lambda ele: ele[1], reverse = True)}
    with open('keebor-log.csv', 'w') as file:
        writer = csv.writer(file)
        for key in keys:
            writer.writerow([key, keys[key]])
        print('goodbye')

