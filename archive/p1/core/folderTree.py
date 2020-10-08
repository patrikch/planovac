from db.sqliteDatabase import Database

class Node:
    def __init__(self,id,name,type):
        self.id = id
        self.name = name
        self.type = type
        self.children = []
        self.extra_properties = {}
        
    @property
    def is_it_dir(self):
        return self.type == "d"

    def __repr__(self):
        return "Node({0}-{1}-{2})".format(self.name,str(self.id),str(self.type))

class FolderTree:
    def __init__(self,userId):
        self.userId = userId
        self.tree = []

    @property
    def get_tree(self):
        if len(self.tree) == 0:
            self._create_project_tree()
        return self.tree
    
    def remove_folder(self,node,recursive=False):
        if len(node.children) > 0 and not recursive:
            raise Exception("Folder: " + str(node) + " has " + str(len(node.children)) +
                            " children and it is not possible remove folder with children.")
        #TODO :nemazat folder, v kterem je projekt
        #jinak - najit ten bez children a smazat
            
    
    def add_node(self,node,parentId):
        sql = ""
        params = []
        db = Database()
        if node.is_it_dir:
            sql = "insert into folder(name,parent,userId) values(?,?,?)"
            params = [node.name,parentId,self.userId]
        else:
            sql = "insert into project(name,ownerId,folderId,dtFrom,dtTo)" \
                  " values(?,?,?,?,?)"
            params = [node.name,self.userId,parentId,
                      node.extra_properties["dtFrom"],node.extra_properties["dtTo"]]
            
        db.run(sql,params)        

    def rename_node(self,node,new_name):
        sql = ""
        db = Database()
        if node.is_it_dir:
            sql = "update folder set name=? where id=?"
        else:
            sql = "update project set name=? where id=?"
        
        db.run(sql,[new_name,node.id])                        

    def _create_project_tree(self):
        tree = []
        sql = "select * from folder where userId=? order by parent,id"
        db = Database()
        dirs = db.get_records(sql,[self.userId,])        
        tree.append(Node(0,"root","d"))
        for d in dirs:
            if d["parent"] == None:
                id = 0
            else:
                id = int(d["parent"])

            n = self._find_in_nodes(tree,id,"d")
            if n:
                n.children.append(Node(int(d["id"]),d["name"],"d"))
            else:
                raise Exception("Uzel id=" + str(id) + " nenalezen.")

        sql = "select id,name,folderId from project where ownerId=? order by folderId"                        
        rows = db.get_records(sql,[self.userId,])            
        for r in rows:
            folder = r["folderId"]
            if not folder:
                folder = "0"
            n = self._find_in_nodes(tree,int(folder),"d")
            if n:
                n.children.append(Node(int(r["id"]),r["name"],"p"))
            else:
                raise Exception("Uzel id=" + str(folder) + " nenalezen.")

        self.tree = tree
        

    def _find_in_nodes(self,nodes,id,type):
        for n in nodes:
            if n.id == id and n.type == type:
                return n
            else:
                sn = self._find_in_nodes(n.children,id,type)
            if sn:
                return sn
