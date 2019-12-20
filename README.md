# CSE505

To run the program, you must first create a directory name 'programs' and give it read/write access: ```chmod 777 programs```

This project uses some libraries to run, such as PySWIP and BeautifulSoup, so you may need to install them.

In order to load a program, you must supply the url for a webpage that contains LogicWeb code. All loadable pages must contain an html element containing the property ```lw_code```. This tag's contents will then be loaded as a file that can be queried.

BeautifulSoup: [https://www.crummy.com/software/BeautifulSoup/bs4/doc/](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

PySWIP: [https://github.com/yuce/pyswip/blob/master/INSTALL.md](https://github.com/yuce/pyswip/blob/master/INSTALL.md)
