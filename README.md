# Depend-py
- [Depend-py](#depend-py)
  - [Background](#background)
  - [Installation](#installation)
  - [Running](#running)
    - [Path](#path)
    - [Sections](#sections)
    - [Output](#output)
  - [TODO](#todo)

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
python depend.py --path ../my-software-project/ --section all

```
### Sections
The sections parameter gives you the ability to filter the output of the scan

* all - all sections combined 
* active - 3rd party packages installed through a package manage & modules provided by the project code
* installed - locally installed in your virtualenv
* source_deps - dependencies from your source code 
* source_pkgs - modules provided from your source code
* missing - modules not installed 

### Output
Here's an example from an old project I did a while back

```sh
10:45 $ python depend.py --path ../alexa_tolls/
```

```python
{'active': {'project_pkgs': {},
            'vendor_pkgs': {'chalice': [('chalice', '1.12.0', ['attrs', 'botocore', 'click', 'enum-compat', 'jmespath', 'pip', 'setuptools', 'six', 'wheel', 'typing', 'watchdog'])],
                            'simple_rest_client': [('simple-rest-client', '1.0.4', ['python-status', 'httpx', 'python-slugify'])]}},
 'installed': {'IPython': [('ipython', '7.12.0', ['setuptools', 'jedi', 'decorator', 'pickleshare', 'traitlets', 'prompt-toolkit', 'pygments', 'backcall', 'pexpect', 'appnope', 'colorama', 'ipyparallel', 'requests', 'notebook', 'qtconsole', 'ipywidgets', 'pygments', 'nbconvert', 'testpath', 'Sphinx', 'nbformat', 'numpy', 'ipykernel', 'nose', 'Sphinx', 'ipykernel', 'nbconvert', 'nbformat', 'notebook', 'ipywidgets', 'ipyparallel', 'qtconsole', 'nose', 'requests', 'testpath', 'pygments', 'nbformat', 'ipykernel', 'numpy'])],
               '_ast27': [('typed-ast', '1.4.1', [])],
               '_ast3': [('typed-ast', '1.4.1', [])],
               'appnope': [('appnope', '0.1.0', [])],
               'astroid': [('astroid', '2.3.3', ['lazy-object-proxy', 'six', 'wrapt', 'typed-ast'])],
               'attr': [('attrs', '19.3.0', ['coverage', 'hypothesis', 'pympler', 'pytest', 'six', 'zope.interface', 'pytest-azurepipelines', 'coverage', 'hypothesis', 'pympler', 'pytest', 'six', 'zope.interface', 'sphinx', 'pre-commit', 'sphinx', 'zope.interface', 'coverage', 'hypothesis', 'pympler', 'pytest', 'six', 'zope.interface'])],
               'backcall': [('backcall', '0.1.0', [])],
               'boto3': [('boto3', '1.12.8', ['botocore', 'jmespath', 's3transfer'])],
               'botocore': [('botocore', '1.15.8', ['python-dateutil', 'jmespath', 'docutils', 'urllib3', 'urllib3'])],
               'certifi': [('certifi', '2019.11.28', [])],
               'chalice': [('chalice', '1.12.0', ['attrs', 'botocore', 'click', 'enum-compat', 'jmespath', 'pip', 'setuptools', 'six', 'wheel', 'typing', 'watchdog'])],
               'chardet': [('chardet', '3.0.4', [])],
               'click': [('Click', '7.0', [])],
               'dateutil': [('python-dateutil', '2.8.1', ['six'])],
               'decorator': [('decorator', '4.4.1', [])],
               'docutils': [('docutils', '0.15.2', [])],
               'easy_install': [('setuptools', '45.2.0', ['certifi', 'sphinx', 'jaraco.packaging', 'rst.linker', 'wincertstore', 'mock', 'pytest-flake8', 'virtualenv', 'pytest-virtualenv', 'pytest', 'wheel', 'coverage', 'pytest-cov', 'pip', 'futures', 'flake8-2020', 'paver'])],
               'h11': [('h11', '0.9.0', [])],
               'h2': [('h2', '3.2.0', ['hyperframe', 'hpack', 'enum34'])],
               'hpack': [('hpack', '3.0.0', [])],
               'hstspreload': [('hstspreload', '2020.2.25', [])],
               'httpx': [('httpx', '0.11.1', ['certifi', 'hstspreload', 'chardet', 'h11', 'h2', 'idna', 'rfc3986', 'sniffio', 'urllib3'])],
               'httpx/backends': [('httpx', '0.11.1', ['certifi', 'hstspreload', 'chardet', 'h11', 'h2', 'idna', 'rfc3986', 'sniffio', 'urllib3'])],
               'httpx/dispatch': [('httpx', '0.11.1', ['certifi', 'hstspreload', 'chardet', 'h11', 'h2', 'idna', 'rfc3986', 'sniffio', 'urllib3'])],
               'hyperframe': [('hyperframe', '5.2.0', [])],
               'idna': [('idna', '2.9', [])],
               'ipython_genutils': [('ipython-genutils', '0.2.0', [])],
               'isort': [('isort', '4.3.21', ['futures', 'backports.functools-lru-cache', 'pipreqs', 'requirementslib', 'toml', 'pipreqs', 'pip-api', 'appdirs'])],
               'jedi': [('jedi', '0.16.0', ['parso', 'flake8', 'colorama', 'docopt', 'pytest'])],
               'jmespath': [('jmespath', '0.9.5', [])],
               'lazy_object_proxy': [('lazy-object-proxy', '1.4.3', [])],
               'mccabe': [('mccabe', '0.6.1', [])],
               'parso': [('parso', '0.6.1', ['docopt', 'pytest'])],
               'pexpect': [('pexpect', '4.8.0', ['ptyprocess'])],
               'pickleshare': [('pickleshare', '0.7.5', ['pathlib2'])],
               'pip': [('pip', '19.3.1', [])],
               'pkg_resources': [('setuptools', '45.2.0', ['certifi', 'sphinx', 'jaraco.packaging', 'rst.linker', 'wincertstore', 'mock', 'pytest-flake8', 'virtualenv', 'pytest-virtualenv', 'pytest', 'wheel', 'coverage', 'pytest-cov', 'pip', 'futures', 'flake8-2020', 'paver'])],
               'prompt_toolkit': [('prompt-toolkit', '3.0.3', ['wcwidth'])],
               'ptyprocess': [('ptyprocess', '0.6.0', [])],
               'pygments': [('Pygments', '2.5.2', [])],
               'pylint': [('pylint', '2.4.4', ['astroid', 'isort', 'mccabe', 'colorama'])],
               'rfc3986': [('rfc3986', '1.3.2', ['idna'])],
               's3transfer': [('s3transfer', '0.3.3', ['botocore', 'futures'])],
               'setuptools': [('setuptools', '45.2.0', ['certifi', 'sphinx', 'jaraco.packaging', 'rst.linker', 'wincertstore', 'mock', 'pytest-flake8', 'virtualenv', 'pytest-virtualenv', 'pytest', 'wheel', 'coverage', 'pytest-cov', 'pip', 'futures', 'flake8-2020', 'paver'])],
               'simple_rest_client': [('simple-rest-client', '1.0.4', ['python-status', 'httpx', 'python-slugify'])],
               'six': [('six', '1.14.0', [])],
               'slugify': [('python-slugify', '4.0.0', ['text-unidecode', 'Unidecode'])],
               'sniffio': [('sniffio', '1.1.0', ['contextvars'])],
               'status': [('python-status', '1.0.1', [])],
               'tests': [('chalice', '1.12.0', ['attrs', 'botocore', 'click', 'enum-compat', 'jmespath', 'pip', 'setuptools', 'six', 'wheel', 'typing', 'watchdog'])],
               'text_unidecode': [('text-unidecode', '1.3', [])],
               'traitlets': [('traitlets', '4.3.3', ['ipython-genutils', 'six', 'decorator', 'enum34', 'enum34', 'pytest', 'mock'])],
               'typed_ast': [('typed-ast', '1.4.1', [])],
               'urllib3': [('urllib3', '1.25.8', ['brotlipy', 'pyOpenSSL', 'cryptography', 'idna', 'certifi', 'ipaddress', 'PySocks'])],
               'wcwidth': [('wcwidth', '0.1.8', [])],
               'wheel': [('wheel', '0.34.2', ['pytest', 'pytest-cov'])],
               'wrapt': [('wrapt', '1.11.2', [])]},
 'missing': ['chalicelib', 'chalicelib', 'chalicelib'],
 'path': '../alexa_tolls/',
 'python_paths': ['../alexa_tolls/.env/lib/python3.7/site-packages'],
 'source_deps': {'chalice': ['Chalice'],
                 'chalicelib.alexa_response': ['AlexaResponse'],
                 'chalicelib.mapquest': ['geocode'],
                 'chalicelib.tollsmart': ['TollSmart'],
                 'pprint': ['pprint'],
                 'simple_rest_client.api': ['API']},
 'source_pkgs': {},
 'system': ['pprint']}

```


## TODO

- [ ] Better output format
  - support generation of requirements.txt? 
  - support reports
- [ ] Design to parse multiple projects
- [ ] Version comparitors - identify collisions





