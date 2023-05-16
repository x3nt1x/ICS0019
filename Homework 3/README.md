# How to use

1. Clone the repository
2. Download & install Miniconda  
   https://docs.conda.io/en/latest/miniconda.html
3. Open Anaconda Prompt in project directory
4. Create new Conda virtual environment
    ~~~
    > conda create --name <environment name>
    ~~~
5. Activate created environment
   ~~~
   # (optional) list environments
   > conda env list
        
   # activate created environment
   > conda activate <environment name>
   ~~~
6. Install packages
    ~~~      
    # install cartopy
    > conda install -c conda-forge cartopy
        
    # reinstall pyproj
    > pip uninstall pyproj && pip install pyproj
        
    # reinstall pillow
    > pip uninstall pillow && pip install pillow
        
    # install scipy
    > pip install scipy
        
    # install pandas
    > pip install pandas
    ~~~
7. Run
    ~~~
    > python app.py
    ~~~