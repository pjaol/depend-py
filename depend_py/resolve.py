from typing import Any, Dict
from depend_py import deepman , utils



def project_dependencies(path, section = "all") -> Dict[str, Any] :
    
    results = {}
    
    # Find the source code dependencies
    source_dep = deepman.project_imports(path=path)
    
    # Find python installs
    python_paths = utils.find_python_paths(path=path)
    
    # Find packages installed in python paths
    installed_packages = deepman.packages_distributions(paths=python_paths)
    
    # Find modules provided by the project
    project_modules = deepman.packages_distributions(paths=[path])
    
    results = { "path" : path,
                "source_deps" : source_dep, 
                "python_paths": python_paths, 
                "installed" : installed_packages, 
                "source_pkgs" : project_modules}
    
    base_pkgs = utils.modules_to_base_pkg(source_dep) 
    code_pkgs = utils.intersection(installed_packages.keys(), base_pkgs)
    local_project_pkg = utils.intersection(project_modules.keys(), base_pkgs)
    
    vendor_pkgs = dict(zip(code_pkgs, map(lambda x : installed_packages[x],  code_pkgs)))
    project_pkgs = dict(zip(local_project_pkg, map(lambda x : project_modules[x],  local_project_pkg)))
    tbd_modules = utils.exclusive(base_pkgs, utils._concat_new_list(vendor_pkgs.keys(),  project_pkgs.keys()))
    
    # Is this module installed with python?
    missing = []
    system_module = []
    for tbd_module in tbd_modules : 
        if deepman.system_module(tbd_module) :
            system_module.append(tbd_module)
        else :
            missing.append(tbd_module)
            
        
    results["active"] = {}
    results["active"]["vendor_pkgs"] = vendor_pkgs
    results["active"]["project_pkgs"] = project_pkgs
    results["missing"] = missing
    results["system"] = system_module
    #pp()
    #pp(not_installed)
    
    if section == "all" :
        return results
    else : 
        section_result= {"path" : path, 
                         section : results[section]}
        return section_result
    
    