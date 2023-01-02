# Depend-py

![XKDC Python Environment](https://imgs.xkcd.com/comics/python_environment.png)

## Background
Pythons dependency management is both a quagmire and simple at the same time. 
Dependencies are stored in pre-defined paths, pip or pip like tools download, 
compile, install those dependencies. 

However nothing manages those dependencies once they are on disk. 
Generally engineers will run 

```
pip install SOME-MODULE
pip freeze > requirements.txt
```

To generate the dependency list, pip freeze analyzes packages that have been installed
and produces the dependency list from there. 
However as software matures, architecture changes, dependencies change resulting in outdated
and bloated requirements list. 

The objective of depend-py is to scan the actual software and determine the dependencies of the written code. 

The software is also written to be independent of the project being scanned, and 
does not need to be installed as part of the target project. 

## Installation

Requires a valid python installation 3+ 
```
git clone https://github.com/pjaol/depend-py.git
```
No additional dependencies are required

## Running

```sh
python depend.py -h
usage: depend.py dependency management across projects [-h] --path PATH
                                                       [--section {all,active,installed,source_deps,source_pkgs,missing}]

optional arguments:
  -h, --help            show this help message and exit
  --path PATH           Path to project
  --section {all,active,installed,source_deps,source_pkgs,missing}
```

### Path
Represents the root path to the project you want to scan, the code is designed to skip known virtualenv paths

e.g.
```
python depend.py --path ../my-software-project/

```
### Sections
The sections parameter gives you the ability to filter the output of the scan

* all - all sections combined 
* active - 3rd party packages installed through a package manage & modules provided by the project code
* installed - locally installed in your virtualenv
* source_deps - dependencies from your source code 
* source_pkgs - modules provided from your source code
* missing - modules not installed 

 



