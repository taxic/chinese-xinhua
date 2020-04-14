import json
with open('../data/idiom-basic.json') as f:
    data = json.load(f)

with open('../data/idiom-graph.json') as gf:
    graph_data = json.load(gf)

n = len(graph_data)

hard = dict()
def give_hints(start_str):
    if start_str not in hard.keys():
        hard[start_str] = 0
    si = hard[start_str]
    for i in range(si, n):
        split_str = graph_data[i]["english"].split()
        if(start_str == split_str[0]):
            data_no = int(graph_data[i]["no"])
            print(data[data_no], int(graph_data[i]["next_num"]))
            for k in range(min(int(graph_data[i]["next_num"]), 5)):
                print("can be followed by:", data[int(graph_data[i]["next"][k])])
            hard[start_str] = i + 1
            break

while(1):
    start_chars = input("start chars:\n")
    give_hints(start_chars)
