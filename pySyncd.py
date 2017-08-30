#!/usr/bin/python

import schedule
import time
import logging
import os
import argparse

from dirsync import sync

def sync_dirs(srcParent, targetParent, configfile, logfile):
    with open(configfile, "r") as syncDirs:
        srcDirList = [line.rstrip('\n') for line in syncDirs]

    dirList = []
    for dirName in srcDirList:
        src = os.path.join(srcParent, dirName)
        target = os.path.join(targetParent, dirName)
        dirList.append((src, target))

    logging.basicConfig(filename=logfile,
                        level=logging.INFO,
                        format='%(asctime)s %(levelname)-8s %(message)s')

    logging.info("-*-*-*- STARTING SYNC -*-*-*-")
    for src, target in dirList:
        sync(src, target, "sync", logger=logging, verbose=True, create=True)

def job():
    parser = argparse.ArgumentParser(description="Periodically syncs directories.")
    parser.add_argument("source", type=int, nargs="+", help="Directory containing a config file and child source folders.")
    parser.add_argument("target", type=int, nargs="+", help="Directory to parent target folder.")
    args = parser.parse_args()
    configfile = os.path.join(args.source, "syncConfig.txt")
    logfile = os.path.join(args.parent, "syncLog.log")
    sync_dirs(args.source, args.target, configfile, logfile)

def run_daemon():
    schedule.every().day.at("02:00").do(job)
    
    while True:
        schedule.run_pending()
        time.sleep(1)

def main():
    run_daemon()

if __name__ == "__main__":
    main()
