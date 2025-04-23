import json

code = ''

d = {}
with open('default.json', 'r') as f:
    d = json.load(f)

file_found = False
file_ran = False
try:
    with open('./main.py', 'r') as f:
        code = f.read()
        file_found = True
except FileNotFoundError:
    pass

try:
    exec(code)
    file_ran = file_found
except:
    pass

d['tests'][0]['score'] = float(file_found)
d['tests'][1]['score'] = float(file_ran) 
if file_found and file_ran: d['stdout_visibility'] = 'visible'

with open('results.json', 'w') as f:
    json.dump(d, f)
