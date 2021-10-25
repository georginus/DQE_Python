import json

json_post = json.load(open('./my_json.json'))
print(json_post)

for i in range(len(json_post)):
    print(json_post[i]["post_text"])
