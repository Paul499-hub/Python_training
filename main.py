
class Graph:
    def __init__(self, edges):
        self.edges = edges


routes = [
    ("Kaunas", "Vilnius"),
    ("Kaunas", "Kapciamiestis"),
    ("Vilnius", "Kaunas"),
    ("Vilnius", "Kapciamiestis"),
    ("Kapciamiestis", "Kaunas"),
    ("Kapciamiestis", "Vilnius"),
] # < ---------------------------------- THIS STUPID CUZ TRAVERSING A LIST EVERYTIME IS A BAD IDEA 


dict = {
    "Mumbai" : ["Paris", "Dubai", "Gotham"],
    "Paris" : ["Mumbai", "New York", "London"],
    "Gotham": ["Toronto"],
    "Dubai" : ["New York"],
    "New York" : ["Toronto", "Gotham"],
}

def get_all_paths_m(start, end, path=[]):
    path = path+[start]
    if start in dict:
        for node in dict[start]:
            if node not in path:
                if node == end:
                    print(f'END node found. {path + [node]}')
                else:
                    get_all_paths_m(start=node, end=end, path=path)

global_list = []
def get_all_paths(start,end, path=[]): # RETURSN ALL POSSIbLE PATHS FROM START TO END 
    global global_list
    print(f' current node : {start}                    previous path : {path}')
    path=path+[start]
    
    for node in dict[start]:
        if node not in path:
            if node==end:
                print(f'=================== Path found to {end}')
                global_list.append( path + [node])
            else:
                new_paths = get_all_paths(node, end, path=path)

    # CORNER CASES
    if start == end:
        return path
    if start not in dict:
        return []

temp_dict = {} # GRAH Dict{ n1 : [n2,n3] }
for  (f,t) in routes:
    if f in temp_dict:
        temp_dict[f].append(t)
    else:
        temp_dict[f] = [t]
    
route_graph = Graph(edges=routes)

start,end = "Mumbai","Toronto"
print(get_all_paths_m(start,end,))
print(f' GLOBAL LIST: {global_list}')