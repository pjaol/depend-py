import ast, _ast
import collections
from importlib.metadata import DistributionFinder

import importlib

from typing import Dict, List, Mapping, Tuple
from importlib_metadata import distributions, _top_level_declared, _top_level_inferred
from depend_py.package import Package

from depend_py.utils import _merge_results, read_file, recurse_directory



def system_module (module) : 
    base = module.split(".")[0]
    spam_spec = importlib.util.find_spec(base)
    found = spam_spec is not None
    return found


def parse(source) :
    all_imports = {}
    
    mod :ast.Module = ast.parse(source=source)
    
    for i  in mod.body: 
        if isinstance(i, _ast.ImportFrom) or isinstance(i, _ast.Import): 
            _depend_map(i, all_imports)

    return all_imports



def _aliases(alias) : 
    result = [name.name for name in alias]
    return result

def _depend_map(import_item, all_imports) : 
    
    if isinstance(import_item, _ast.ImportFrom) :
        if import_item.module in all_imports : 
            all_imports[import_item.module].extend(_aliases(import_item.names))
        else :
            all_imports[import_item.module] = _aliases(import_item.names)
    if isinstance(import_item, _ast.Import) :
        for name in import_item.names :
            name :_ast.alias = name 
            #print(name.name)
            if name.name not in all_imports : 
                all_imports[name.name] = []
    
    return all_imports


def project_imports(path : str) -> Dict[str, List[str]]: 
    """
    Return a dictionary of modules and imports used in python code
    
    Args:
        path (str): _description_

    Returns:
        Dict[str, List[str]]: module name and classes
    """    
    result = {}
    for f in recurse_directory(path=path) : 
        source = read_file(f)
        _merge_results(parse(source), result) 
    
    return result

def packages_distributions(paths :List[str]) -> Dict[str, List[Package]]:
    """    
    Return a mapping of top-level packages to their
    distributions.
    Based on importlib_metadata.packages_distributions() modified slightly to handle a custom path
    This allows packages to be listed without being in the run time for the virtualenv
    
    >>> import collections.abc
    >>> pkgs = packages_distributions(paths)
    >>> all(isinstance(dist, collections.abc.Sequence) for dist in pkgs.values())
    True
    
    Args:
        paths (List[str]): list of paths that packages and modules exist
                            use with depend_py.utils.find_python_paths to get a list of pip install packages

                            Can also find module names from editable paths as well
    Returns:
        Dict[str, List[str]]: _description_
    """    
    context = DistributionFinder.Context(path=paths)
    pkg_to_dist = collections.defaultdict(list)
    for dist in distributions(context=context):
        for pkg in _top_level_declared(dist) or _top_level_inferred(dist):
            pkg_to_dist[pkg].append(Package(dist.metadata['Name'], dist.metadata['Version'], dist.requires))
    return dict(pkg_to_dist)