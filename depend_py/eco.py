

class Network : 
    def __init__(self, name) -> None:
        self.name = name
        self.nodes = []
        
    def add_tree(self, tree) -> None: 
        active = tree["active"]
        for subsection in active.keys(): 
            for module in active[subsection].keys() : 
                #print(module)
                for pkg in active[subsection][module] : 
                    node = self.get_node(pkg.name) or Node(pkg)
                    self.add_node(node)
                    for requirement in pkg.requires : 
                        #print(f"{pkg.name} , {requirement.name}")
                        n2 = self.get_node(requirement.name) or Node(requirement)
                        self.add_node(n2)
                        node.add_connection(n2)
        
    def add_node(self, node): 
        if node not in self.nodes : 
            self.nodes.append(node)
            
    def get_node(self, node_name) : 
        if node_name in self.nodes : 
            idx = self.nodes.index(node_name)
            return self.nodes[idx]
        
        return None
    
    def depends_on(self, pkg_name): 
        n = self.get_node(pkg_name)
        if n is not None : 
            return [x.package.name for x in n.outgoing]
        print(f"Not an active dependency {pkg_name}")
        
class Node :
    def __init__(self, package) -> None:
        self.package = package
        self.incoming = []
        self.outgoing = []
    
    
    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, str) : 
            return self.package.name == str(__o)
        
        if isinstance(__o, Node): 
            return self.package.name == __o.package.name
        
        return False
    
    def add_connection(self, node ) : 
        if node not in self.incoming : 
            self.incoming.append(node)
        if self not in node.outgoing :
            node.outgoing.append(self)

    def __repr__(self) -> str:
        return self.package.name