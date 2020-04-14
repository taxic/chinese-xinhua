import json
with open('../data/idiom-basic.json') as f:
    data = json.load(f)

with open('../data/idiom-graph.json') as gf:
    graph_data = json.load(gf)

n = len(graph_data)

hard_map = dict()
easy_map = dict()
def give_hints(start_str, easy=False):
    if start_str not in hard_map.keys():
        hard_map[start_str] = 0
    if start_str not in easy_map.keys():
        easy_map[start_str] = n - 1
    si = hard_map[start_str]
    ei = n
    step = 1
    if easy:
        step = -1
        si = easy_map[start_str]
        ei = -1

    for i in range(si, ei, step):
        split_str = graph_data[i]["english"].split()
        if(start_str == split_str[0]):
            data_no = int(graph_data[i]["no"])
            print(data[data_no], int(graph_data[i]["next_num"]))
            for k in range(min(int(graph_data[i]["next_num"]), 5)):
                print("can be followed by:", data[int(graph_data[i]["next"][k])])
            if easy:
                easy_map[start_str] = i - 1
            else:
                hard_map[start_str] = i + 1
            break

while(1):
    start_chars = input("start chars:\n")
    give_hints(start_chars)
    give_hints(start_chars, True)
