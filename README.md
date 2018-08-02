Lenses.csv: 
This file is a table containing recently discovered astronomical lensed objects found at: https://www.cfa.harvard.edu/castles/noimages.html

Cross.py 
This file is a python script that takes no arguments and reads from Lenses.csv.
The script will generate queries and place them in Queries.txt that I will be able to run on the SDSS Casjobs command line tool to produce tables containing primitive Einstein Cross models.

Queries.txt
This file is where I place my scheduled queries. The beauty of this is that when I use the terminal to run these queries I can simply copy the whole file into the terminal window and it will execute every query in order.

The Models directory contains models that were generated using the queries in Queries.txt

