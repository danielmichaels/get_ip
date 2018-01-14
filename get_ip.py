#!/usr/bin/env python3
import csv
import os.path
from datetime import datetime

import requests
from requests import ConnectionError


def main():
    ip = get_ip()
    time = get_time()
    make_csv(ip, time)


def get_ip():
    """Use requests to get api.ipify.org external address."""
    try:
        r = requests.get('https://api.ipify.org').text
        return r
    except ConnectionError:
        return 'No Connection'


def get_time():
    """Gets the timedate of change."""
    date = datetime.now()
    now = date.strftime('%d-%m-%y %H:%M')
    return now


def make_csv(ip, time):
    """Takes the dict and puts it into a csv object."""
    data = {'IP': ip, 'Timestamp': time}
    header_check = os.path.isfile('connect_log.csv')
    # TODO: os module to create monthly csv
    with open('connect_log.csv', 'a+') as csv_file:
        csv_file.seek(0)  # 'a' points the file to end of file, seek(0) resets
        # it to the beginning. 'a' must be done to open a file if not exist.
        reader = csv.DictReader(csv_file)
        fieldnames = ['IP', 'Timestamp']

        # with open('connect_log.csv', 'a+') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        if not header_check:
            '''This exists to check that file exists, if not it will append
            the headers at the top of the csv. If it does exist, it will
            do nothing.
            '''
            writer.writeheader()
            writer.writerow(data)
        else:
            '''Without an index this will fail the script so the writeheaders
                and first entry must succeed before this can execute.'''
            ip_list = [ip['IP'] for ip in reader]
            if ip_list[-1] != ip:
                print('working')
                writer.writerow(data)


def show_ip(): #TODO
    """ This function shows the ip address when called from cli"""
    pass


if __name__ == '__main__':
    main()
