import json


text = '''{
   "demo": "Processing JSON in Python",
"instructor": "Michael",
   "duration": 5.0
}'''


data = json.loads(text)
print(data)

#instuctor = data['instructor']
inst = data.get('instructor', 'SUB')
print(inst)

data['instructor'] = 'Jeff'
print(data)