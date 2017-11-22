## Simple Python SSL Website Enumeration & Reconnaissance

### Purpose
Program reads a `websites.txt` file as input. `websites.txt` follows this format:

    website1.com
    website2.com
    website3.com

With the help of [PhantomJS](http://phantomjs.org/), it is able to reach each hostname, take a screenshot, and save this screenshot with the following naming convention `hostname.png` in a local directory.

### Setup
* Install Python
* Install PhantomJS
* Install selenium `pip install selenium`
* Generate a SSL Cert Report for your company's domain using [Symantec's CryptoReport](https://cryptoreport.websecurity.symantec.com/checker/views/ctsearch.jsp)
* Export the .csv and copy/paste the hostname column into a `websites.txt` file

### To-Do
* Read directly from csv
* Allow user to supply file name as a command-line argument to program
* Multi-threading for scalability 
