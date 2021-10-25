### JSON

# dict to json

# qqq = {
#      "key1": "value1"
#      , "key2": "value2"
# }
# #
# # with open('my_json_test1.json', 'w') as myfile:
# #     myfile.write(str(qqq))
# n = 'George'
# #print(eval("f'My name is {n}'"))
# a = eval("[1, 2, 3]")
#
# b = eval(str(qqq))
# print(type(b))
# print(b)


### dump - from dict to json
import json

qqq = {
    "key1": "value1",
    "key2": "value2",
    "key3": True,
    "key4": None
    }


json.dump(qqq, open('my_dump_to_json.json', 'w'))


### load - from json to dict
qqq_load = json.load(open('my_dump_to_json.json'))

#print(type(qqq_load))
#print(qqq_load)

### dumps and loads

astr = json.dumps(qqq)
#print(astr)

json_loads = json.loads(astr)
#print(json_loads)

### indent - output as json structure
#print(json.dumps(json_loads, indent=2))


