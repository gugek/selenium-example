import random
import time
import os
import sys
import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import \
    NoSuchElementException, StaleElementReferenceException, WebDriverException
import argparse
import logging
import logging.handlers
import requests
import pprint
import lxml.html
import csv
import backoff
import re
import humps
import parsedatetime as pdt
from datetime import datetime, date


def main(args):
    """Visit a page and take a screenshot"""

    logging.info("scraping {}".format(args.url))
    head, tail = os.path.split(os.path.abspath(__file__))

    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')  # needed for root
    options.add_argument('--window-size=1200x600')

    # initialize the driver
    driver = webdriver.Chrome(chrome_options=options)
    driver.implicitly_wait(10)
    # driver.get(inmates_url)
    driver.get(args.url)
    delay = random.random() * args.pause
    time.sleep(delay)
    logging.info("pausing for {:.4f} seconds".format(delay))

    logging.info("Looking for a specific element!")
    # dom type methods
    select_box = driver.find_element(By.CLASS_NAME, "ui-pg-selbox" )
    select_options = Select(select_box)

    # selecting an option
    select_options.select_by_value('10000')

    delay = random.random() * args.pause * 2
    time.sleep(delay)
    logging.info("pausing for {:.4f} seconds".format(delay))

    logging.info("took a before screenshot")
    driver.get_screenshot_as_file(os.path.join(head,
    "images/args_url_before.png"))

    # count our table rows
    trs = driver.find_elements_by_xpath("//table[@id='tblII']//tr")
    logging.info("I saw {} rows in the table!".format(len(trs)))

    # action change moving around on page
    tr_elem = random.choice(trs)
    logging.info("clicking on {}".format(tr_elem))

    tr_elem.click()
    # just prove we moved around
    delay = random.random() * args.pause
    logging.info("pausing for {:.4f} seconds".format(delay))

    logging.info("taking another screenshot")
    driver.get_screenshot_as_file(os.path.join(head,
        "images/args_url_click.png"))

    driver.back()

    delay = random.random() * args.pause
    time.sleep(delay)
    logging.info("pausing for {:.4f} seconds".format(delay))
    # actions = ActionChains(driver)
    # move_to_elem = driver.find_element_by_class_name("Footer")
    # actions.click(move_to_elem)
    # actions.perform()
    # delay = random.random() * args.pause
    # logging.info("pausing for {:.4f} seconds".format(delay))

    # just prove we moved around
    logging.info("took an after screenshot")
    driver.get_screenshot_as_file(os.path.join(head,
        "images/args_url_after.png"))

    # print out how many table rows we have
    # xpath finds

    tr_count = 0
    for tr in trs:
        tr_count += 1



    driver.close()
    driver.quit()
    logging.info("completed job")


def set_logging(args):
    """Set up basic logging with default in args to sys.stdout"""
    logformat = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    loglevel = getattr(logging, args.loglevel.upper())
    formatter = logging.Formatter(logformat)
    if args.verbose is True:
        loglevel = logging.INFO
    if args.debug is True:
        loglevel = logging.DEBUG
    logging.basicConfig(format=logformat, level=loglevel, stream=sys.stdout)

    if args.verbose is False and args.debug is False:
        logging.getLogger().handlers.pop()

    if args.logfile:
        loghandler = logging.handlers.RotatingFileHandler(
            filename=args.logfile,
            maxBytes=1024*1024*5,
            backupCount=5)
        loghandler.setFormatter(formatter)
        loghandler.setLevel(loglevel)
        logging.getLogger().addHandler(loghandler)
    return True


def parse_arguments():
    path = os.path.dirname(os.path.abspath(__file__))
    parser = argparse.ArgumentParser(
        description='Selenium example')
    parser.add_argument('-v', '--verbose',
        action="store_true",
        default=False,
        help="verbose output")
    parser.add_argument('-d', '--debug',
        action="store_true",
        default=False,
        help="debug output")
    parser.add_argument('-l', '--logfile',
        help="Log file name",
        default=None)
    parser.add_argument('-L', '--loglevel',
        default='WARNING',
        help="Python logging levels")
    parser.add_argument("-p", '--pause',
        default=2,
        type=int,
        help="delay in seconds for clicks")
    parser.add_argument("url",
        help="website to scrape")
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = parse_arguments()
    set_logging(args)
    main(args)
