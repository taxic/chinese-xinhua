import json
with open('../data/idiom-basic.json') as f:
    data = json.load(f)

with open('../data/idiom-graph.json') as gf:
    graph_data = json.load(gf)

n = len(graph_data)

def find_from_start_with(si, start_str):
    for i in range(si, n):
        split_str = graph_data[i]["english"].split()
        if(start_str == split_str[0]):
            data_no = int(graph_data[i]["no"])
            print(data[data_no], int(graph_data[i]["next_num"]))
            for k in range(min(int(graph_data[i]["next_num"]), 5)):
                print("can be followed by:", data[int(graph_data[i]["next"][k])])
            return i + 1

remember = dict()
while(1):
    start_chars = input("start chars:\n")
    if start_chars not in remember.keys():
        remember[start_chars] = 0
    remember[start_chars] = find_from_start_with(remember[start_chars], start_chars)
