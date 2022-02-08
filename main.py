#!/usr/bin/env python

import random
import time
from lxml.html import fromstring
import nltk, sys, requests
import argparse

from multigro.bin_py import*
from multigro.bin_py.pvt_fit import PVT

# Autorship information
__author__ = "Hüsamettin Deniz Özeren"
__copyright__ = "Copyright 2021"
__credits__ = ["Hüsamettin Deniz Özeren"]
__license__ = "GNU General Public License v3.0"
__maintainer__ = "Hüsamettin Deniz Özeren"
__email__ = "denizozeren614@gmail.com"

def share_twitter(news_funcs):
    """Encompasses the main loop of the bot."""
    nltk.download('punkt') 
    news_iterators = []  
    for func in news_funcs:
        news_iterators.append(globals()[func]())
    while True:
        for i, iterator in enumerate(news_iterators):
            try:
                tweet = next(iterator)
                api.update_status(status=tweet)
                print(tweet)
                time.sleep(10800) 
            except (StopIteration, IndexError, TwythonError): #fix index error cf line 37
                news_iterators[i] = globals()[news_funcs[i]]()

def main():
    parser = argparse.ArgumentParser("theateraatw")
    parser.add_argument("nytimes", nargs='?', help="Start scraping and sending tweets from New York Times.")
    parser.add_argument("wostage", nargs='?', help="Start scraping and sending tweets from WhatsOnStage.")
    parser.add_argument("tmania", nargs='?', help="Start scraping and sending tweets from TheaterMania.")
    parser.add_argument("ttimes", nargs='?', help="Start scraping and sending tweets from The Theatre Times.")
    args = parser.parse_args()
    
    if len(sys.argv) == 1: 
        print("You should put the arguments: nytimes or wostage or tmania or ttimes")
        return

    #elif sys.argv[1] == "-h":
    #    print(args.counter + 1)
    #    return

    elif sys.argv[1] == 'nytimes':
        news_funcs = ['scrape_nytimes']
        print('-------New York Times Bot started.-------')
    
    elif sys.argv[1] == 'wostage':
        news_funcs = ['scrape_wostage']
        print('-------Wostage Bot started.-------')

    elif sys.argv[1] == 'tmania':
        news_funcs = ['scrape_tmania']
        print('-------The TheaterMania Bot started.-------')

    elif sys.argv[1] == 'ttimes':
        news_funcs = ['scrape_ttimes']
        print('-------The Theatre Times Bot started.-------')
    
    else: 
        parser.print_help()
        return

    share_twitter(news_funcs)


if __name__ == "__main__":
    main()
