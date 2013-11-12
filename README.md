### Untangled: Social Network Analysis for Journalism

This repository is a microsite collecting research done at the Northwestern University Knight Lab on the application of social network analysis to journalism.

To read the current version of this research, visit [http://untangled.knightlab.com](http://untangled.knightlab.com).

##REQUIREMENTS

You need to have `gcc` installed. 

* For Mac OSX 10.9 (Mavericks), you can do this directly from the terminal. Open a shell and type `xcode-select --install` See [this page](http://www.computersnyou.com/2025/2013/06/install-command-line-tools-in-osx-10-9-mavericks-how-to/) if you want a preview of what to expect.

* For Mac OSX 10.7 (Lion) and Mac OSX 10.8 (Mountain Lion), these can be retrieved from [Apple's Developer site](https://developer.apple.com/downloads/index.action). You must have an Apple ID to log in. Then search for 'command line tools' and install the appropriate version for your OS.

* For Mac OSX 10.6 (and as an alternative to the above for 10.7), you can download installers from [Kenneth Reitz's Github page](https://github.com/kennethreitz/osx-gcc-installer/downloads).

[virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/en/latest/install.html)



###DEVELOPMENT

    # Clone secrets and fablib repositories
    git clone git@github.com:NUKnightLab/fablib.git
    
    # Change into project directory
    cd <project_name>
    
    # Make virtual environment
    mkvirtualenv <project_name>
    
    # Activate virtual environment
    workon <project_name>
    
    # Install requirements
    pip install -r requirements.txt
    
    # Setup (if necessary)
    fab loc setup

    # Start the development server
    python api.py
    

## Deploying to S3 (untangled.knightlab.com)

You need the `secrets` repository to deploy to S3.  If you haven't yet, check out that Git repository to the same directory that contains your untangled-research respository.

```
    git clone git@github.com:NUKnightLab/secrets.git
```

To update S3, type `fab deploy`.  This runs a build using the latest version tag and synchronizes the files in the build directory with S3.
