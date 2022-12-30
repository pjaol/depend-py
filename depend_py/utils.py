from genericpath import isdir
from pathlib import Path, PosixPath
import os
import re
from tokenize import Triple
from typing import List 


default_ignore = [".env", ".venv", ".git", "__pycache__", ".vscode"]

default_distribution_paths = [".env", ".venv", "venv"]


def recurse_directory(path, ignore=default_ignore, extension=".py"): 
    for root, dirs, files in os.walk(path, topdown=True) : 
        [dirs.remove(d) for d in list(dirs) if d in ignore]
        for file in files : 
            if file.endswith(extension) : 
                yield os.path.join(root, file)

def read_file(filename): 
    content = Path(filename).read_text()
    return content

def _merge_results (res1, res2) :
    res = res2.update(res1)
    return res

def _concat_new_list(list1, list2) : 
    return [y for x in [list1, list2] for y in x]


# venv/lib/pythonx.x/site-packages
# .env/lib/site-packages
# .env/src

def find_python_paths(path :str, distribution_paths :List[str] = default_distribution_paths) -> List[str]: 
    """
    Find common python virtual environment distributions based on a base path
    searches for :
        - (venv or .env or .venv) and 
        - lib/pythonM.M/site-packages,
        - lib/site-packages,
        - src

    Args:
        path (str): A base path to search for common python virtualenv installs
        distribution_paths (List[str], optional): List of paths to search for a virtualenv install. Defaults to default_distribution_paths.

    Returns:
        List[str]: returns a list of base directories that may contain package installs
    """    

    possible_path=[]
    for d in distribution_paths : 
        
        lib_dir = os.path.join(path, d, "lib")
        src_dir = os.path.join(path, d, "src")
        #print(lib_dir)
        #print(src_dir)
        
        # Is this a lib path?
        # Check sub directories for either a src folder, site-packages folder 
        # or a python version folder
        if os.path.isdir(lib_dir) :
            #print(f"Lib dir {lib_dir}")
            sub_dirs = [f for f in Path(lib_dir).iterdir() if f.is_dir()]
            
            for sub_dir in sub_dirs :
                
                sub_dir : PosixPath = sub_dir
                #print(sub_dir.name)
                patterns = [r"site-packages", r'src']
                
                if _is_a_match(sub_dir.name, patterns=patterns): 
                    #print("Found {}".format(sub_dir))
                    possible_path.append(str(sub_dir))
                
                if _is_a_match(sub_dir.name, patterns=[ r'python\d\.\d']) : 
                    site = Path(sub_dir).joinpath("site-packages")
                    if os.path.isdir(site) : 
                        #print(f"Found {site}")
                        possible_path.append(str(site))
                    
        # is this a src folder?
        # src folders come from editable installs of packages        
        if os.path.isdir(src_dir) :
            #print(f"Found {src_dir}")
            possible_path.append(src_dir)
    
    return possible_path

def _is_a_match(comp, patterns) :
    for p in patterns : 
        if re.match(p, comp) : 
            return True
    
    return False

def modules_to_base_pkg(modules) :
    results = []
    for m in modules.keys() : 
        results.append(m.split(".")[0])
    
    return results


def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3

def exclusive(lst1, lst2) :
    lst3 = [value for value in lst1 if value not in lst2]
    return lst3