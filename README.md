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