from argparse import ArgumentParser
from tkinter import NO
from depend_py import eco, resolve
from pprint import pprint as pp


if __name__ == "__main__" : 
    parser = ArgumentParser("Deep Resolve creates a network of dependencies")
    parser.add_argument("--path", required=True, help="Path to project")
    parser.add_argument("--section", required=False, choices=["all","active","installed", "source_deps", "source_pkgs", "missing"])
    parser.add_argument("--depends-on")
    args = parser.parse_args()
    
    path = args.path
    depends_on = args.depends_on
    section = args.section
    
    tree = resolve.project_dependencies(args.path, "all")
    if section is not None : 
        if section != "all" : 
            pp(tree[args.section], depth=2, compact=True)
        else : 
            pp(tree, depth=3, compact=True) 
        
    network = eco.Network("Test")
    network.add_tree(tree)
    if depends_on is not None : 
        dependents = network.depends_on(depends_on)
        print(f"{depends_on} is required by {dependents}")
        if depends_on in tree["system"] : 
            print(f"{depends_on} is a system module")
        
        #pp(tree)
        if dependents is not None and any(item in tree["source_pkgs"] for item in dependents  ) : 
            print(f"List of {dependents} has a source package")
        if depends_on in tree["source_deps"] : 
            print(f"{depends_on} is a source dependency") 
        else : 
            print(f"{depends_on} is NOT a source dependency")  
                        
    else :     
        pp(network.nodes)
    
    