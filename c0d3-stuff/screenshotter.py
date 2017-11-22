#!/usr/bin/python
from selenium import webdriver

with open('websites.txt', 'r')  as fp:
    line = fp.readline()
    for line in fp:
        line_get = "https://" + line.strip()
        # set up browser
        driver = webdriver.PhantomJS(service_args=['--ignore-ssl-errors=true', '--ssl-protocol=any', '--web-security=false'])
        driver.set_window_size(1024,768)
        browser = webdriver.PhantomJS(service_args=['--ignore-ssl-errors=true', '--ssl-protocol=any', '--web-security=false'])

        print "getting web page..." + line_get
        driver.get(line_get)

        name = line.strip() + ".png"
        driver.save_screenshot(name)
        driver = ""
