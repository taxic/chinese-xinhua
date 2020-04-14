import json
with open('../data/idiom-basic.json') as f:
    data = json.load(f)

try:
    with open('../data/idiom-graph.json') as gf:
        graph_data = json.load(gf)
        print("Now we already have", len(graph_data), "idioms in the graph.")
except:
    print("no graph data.")

if(len(graph_data) == len(data)):
    exit()

n = len(data)
def next_idiom_list(strx):
    """ string to int list """
    ret_list = list()
    strxs = strx.split()
    for i in range(len(data)):
        stri = data[i]["english"]
        stris = stri.split()
        if strxs[-1] == stris[0]:
            ret_list.append(i)
    return ret_list

new_list = list()
for i in range(n):
    if (i % 1000) == 0:
        print(i, "idioms finished.")
    idiom = data[i]
    new_data = dict()
    new_data["next"] = next_idiom_list(idiom["english"])
    new_data["next_num"] = len(new_data["next"])
    new_data["word"] = idiom["word"]
    new_data["english"] = idiom["english"]
    new_data["no"] = i
    new_list.append(new_data)

# sorting
sorted_d = sorted(new_list, key=lambda x: x['next_num'])
with open('../data/idiom-graph.json', 'w+') as outfile:
    json.dump(sorted_d, outfile)
