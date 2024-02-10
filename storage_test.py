#!/usr/bin/env python3
import json 

# with open('db.json', 'r') as f:
#     for line in f:
#      print(line)
#      print('*' * 20)
#      print('')
#      json_obj = json.loads(line)
#      print(json_obj)

with open('db.json', 'r', encoding = 'utf8') as f:
    al = json.load(f)

print(al)
print(type(al))
print(al.keys())
for k in al.keys():
    print(type(k))
    print(k)