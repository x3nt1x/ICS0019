# How to use

1. Clone the repository
2. Open terminal in project directory
3. Install virtualenv
   ~~~
   > python -m pip install virtualenv
   ~~~
4. Create and activate new virtual environment
   ~~~
   > python -m venv env
   > env\Scripts\activate
   ~~~
5. Install requirements
   ~~~
   > python -m pip install -r requirements.txt
   ~~~
6. Run
   * SQLite
     ~~~
     > python sqlite.py
     ~~~
   * SQLAlchemy
     ~~~
     > python orm.py
     ~~~