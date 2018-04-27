import os
import time
import argparse
import platform
import urllib2
print(platform.system().lower())
def visit_win(url, times, duration):

    def _visit_win():
        try:
            s = urllib2.urlopen(url).read()
        except urllib2.HTTPError,e:
            print (e.code)
    for i in range(times):
        _visit_win()
        print("{} Done!".format(i+1))
        #do not use duration in win

def visit_linux(url, times, duration):
    import subprocess
    cmd = "curl {}".format(url)
    for i in range(times):
        subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE,shell=True)
        print("{} Done!".format(i+1))
        time.sleep(duration)

def parse_input():
    input_parser = argparse.ArgumentParser()
    input_parser.add_argument("--url",'-u', help="the url your need to visit")
    input_parser.add_argument("--times",'-t', type=int, default=10, help="how many times you need to visit")
    input_parser.add_argument("--duration",'-d', default=0.5, type=float, help="the duration between two visits")
    input_args = input_parser.parse_args()
    url = input_args.url
    times = input_args.times
    duration = input_args.duration
    return url, times, duration

def main():
    url, times, duration = parse_input()
    if platform.system().lower() == 'linux':
        visit_linux(url, times, duration)
    else:
        visit_win(url, times, duration)
    print("My evil job is finished!")

if __name__ == '__main__':
    main()