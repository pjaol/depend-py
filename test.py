from depend_py.deepman import project_imports, parse, packages_distributions
from depend_py.utils import find_python_paths, exclusive, intersection, modules_to_base_pkg, recurse_directory, read_file, _merge_results
from pprint import pprint as pp

data = """
from pprint import pprint as pp
from sqlalchmey.orm import TEXT
import pandas as pd
import sys, _sys

class Foo :
    def __init__(self) :
        pass
        
    def foo(self) :
        print("lala")

def wee(bbb) :
    print(bbb)
    return bbb

"""


if __name__ == "__main__" : 
    
    #all_imports = parse(source=data)        
    #pp(all_imports)
    p = "/Users/patrick/Projects/Preftech/DataWarehouse/"
    
    #result = project_imports(p)
    result1 = find_python_paths(path=p)
    result2 = find_python_paths(path="/Users/patrick/Projects/Preftech/SearchIndexer")
    
    #pp(packages_distributions(result2))
    pp(packages_distributions([p]))
    
    #pp(result)
    #base_pks = modules_to_base_pkg(result) 
    #pp(base_pks)
    #installed = packages_distributions(["/Users/patrick/Projects/Preftech/DataWarehouse/.venv/lib/python3.8/site-packages"])
    #pp(installed.keys())
    #code_pkgs = intersection(installed.keys(), base_pks)
    #not_installed = exclusive(base_pks, installed.keys())
    
    #pp(dict(zip(code_pkgs, map(lambda x : installed[x],  code_pkgs))))
    #pp(not_installed)