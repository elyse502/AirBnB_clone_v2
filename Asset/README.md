# 0x02. AirBnB clone - MySQL
## Description :house:
Alx-HolbertonBnB is a complete RESTful web application, integrating file and database (MySQL) storage in a back-end API with front-end interfacing in a clone of AirBnB. The front-end is designed using HTML5/CSS3 and is served using Python Flask. The application is configured on a distributed system - two web servers and one load balancer - with Nginx and HAProxy.

Alx-HolbertonBnB is still in active development, with complete functionality set to deploy in the coming month:
* Complete integration of a RESTful API
* Full configuration of website with domain name
* Serving of dynamic content using JavaScript

# Background Context
Environment variables will be your best friend for this project!
* `HBNB_ENV`: running environment. It can be “dev” or “test” for the moment (“production” soon!)
* `HBNB_MYSQL_USER`: the username of your MySQL
* `HBNB_MYSQL_PWD`: the password of your MySQL
* `HBNB_MYSQL_HOST`: the hostname of your MySQL
* `HBNB_MYSQL_DB`: the database name of your MySQL
* `HBNB_TYPE_STORAGE`: the type of storage used. It can be “file” (using `FileStorage`) or `db` (using `DBStorage`)

# Resources🏗️
### Read or watch:
* [cmd module](https://docs.python.org/3/library/cmd.html)
* **packages** concept page
* [unittest module](https://docs.python.org/3/library/unittest.html#module-unittest)
* [args/kwargs](https://yasoob.me/2013/08/04/args-and-kwargs-in-python-explained/)
* [SQLAlchemy tutorial](https://docs.sqlalchemy.org/en/13/orm/tutorial.html)
* [How To Create a New User and Grant Permissions in MySQL](https://www.digitalocean.com/community/tutorials/how-to-create-a-new-user-and-grant-permissions-in-mysql)
* [Python3 and environment variables](https://docs.python.org/3/library/os.html?highlight=env#os.getenv)
* [SQLAlchemy](https://docs.sqlalchemy.org/en/13/)
* [MySQL 8.0 SQL Statement Syntax](https://dev.mysql.com/doc/refman/8.0/en/sql-statements.html)

# General🧵
* What is Unit testing and how to implement it in a large project
* What is `*args` and how to use it
* What is `**kwargs` and how to use it
* How to handle named arguments in a function
* How to create a MySQL database
* How to create a MySQL user and grant it privileges
* What ORM means
* How to map a Python Class to a MySQL table
* How to handle 2 different storage engines with the same codebase
* How to use environment variables

# Requirements
## Python Scripts
* All your modules should have documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
* All your classes should have documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
* All your functions (inside and outside a class) should have documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
* A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

# Python Unit Tests
* All your test files should be inside a folder tests
* You have to use the [unittest module](https://docs.python.org/3/library/unittest.html#module-unittest)
* All your test files should be python files (extension: `.py`)
* All your test files and folders should start by `test_`
* Your file organization in the tests folder should be the same as your project: ex: for `models/base_model.py`, unit tests must be in: tests/test_models/test_base_model.py
* All your tests should be executed by using this command: python3 -m unittest discover tests
* You can also test file by file by using this command: python3 -m unittest tests/test_models/test_base_model.py
* All your modules should have documentation (python3 -c 'print(__import__("my_module").__doc__)')
* All your classes should have documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
* All your functions (inside and outside a class) should have documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
* We strongly encourage you to work together on test cases, so that you don’t miss any edge cases
















































































