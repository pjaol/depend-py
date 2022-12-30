from packaging.requirements import Requirement

class Package :
    def __init__(self, name, version, requires) -> None:
        self.name = name
        self.version = version
        self._requires = []    
        self.requires = requires

    @property
    def requires(self): 
        return self._requires
    
    @requires.setter
    def requires(self, requires) :        
        if requires is None: 
            return
        
        for r in requires : 
            self._requires.append(Requirement(r))


            
    def __str__(self) -> str:
        """Print summary of Package

        Returns:
            str: prints name, version and just the name requirements for brevity
        """        
        return str(tuple([   self.name, 
                        self.version, 
                        [x.name for x in self._requires ]] )) 
        
        
    def __repr__(self) -> str:
        return str(self)