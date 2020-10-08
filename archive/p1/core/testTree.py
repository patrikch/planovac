class Node:
    def __init__(self,id,name):        
        self.id = id
        self.name = name
        self.children = []

    def __repr__(self):
        return "Node({0} - {1})".format(str(self.id),self.name)

def create_tree(recs):
    tree = []
    sortedRecs = sorted(recs, key=lambda x: 0 if x["parent"]==None else int(x["parent"]), reverse=False)
    node = Node(0,"root")
    tree.append(node)
    for r in sortedRecs:
        if r["parent"] == None:
            id = 0            
        else:
            id = int(r["parent"])
            
        n = find_in_nodes2(tree,id)

        if n: 
            n.children.append(Node(int(r["id"]),r["name"]))
        else:
            raise Exception("Uzel id=" + str(id) + " nenalezen.")
                    
    return tree

def find_in_nodes2(nodes,id):
    for n in nodes:
        if n.id == id:
            return n
        else:
            sn = find_in_nodes2(n.children,id)
            if sn:
                return sn

def find_in_nodes(nodes,rec):
    parent = rec["parent"]
    if parent == None:
        parent = 0

    for n in nodes:
        if n.id == int(parent):
            return n
        else:
            return find_in_nodes(n.children,rec)
    #nenalezeno
       



if __name__ == "__main__":
    recs = []    
    recs.append({"id":1,"name":"2013","parent":None})
    recs.append({"id":2,"name":"2014","parent":None})
    recs.append({"id":3,"name":"2015","parent":None})
    recs.append({"id":4,"name":"1.2015","parent":3})
    recs.append({"id":5,"name":"2.2015","parent":3})
    recs.append({"id":6,"name":"3.2015","parent":3})
    recs.append({"id":7,"name":"1.1.2015","parent":4})
    recs.append({"id":8,"name":"2.1.2015","parent":4})
    #sortedRecs = sorted(recs, key=lambda x: 0 if x["parent"]==None else int(x["parent"]), reverse=False)    
    #for r in sortedRecs:
    #    print(r)    
    #print(str(len(recs)))
    
    tree = create_tree(recs)
    for n in tree:
        print(str(n))
        for sn in n.children:
            print("\t" + str(sn))
            for ssn in sn.children:
                print("\t\t" + str(ssn))
                for sssn in ssn.children:
                    print("\t\t\t" + str(sssn))
    print("done")
    
