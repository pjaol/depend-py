import argparse
from depend_py.resolve import project_dependencies
from pprint import pprint as pp

if __name__ == "__main__" :
    parser = argparse.ArgumentParser("depend.py dependency management across projects")
    parser.add_argument("--path", required=True, help="Path to project")
    parser.add_argument("--section", required=False, default="all", choices=["all","active","installed", "source_deps", "source_pkgs", "missing"])
    args = parser.parse_args()
    
    pp(project_dependencies(args.path, args.section))
    
    
    