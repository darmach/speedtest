import subprocess
import json
import datetime
from time import sleep
import sys
from multimethod import multimethod


def speedtest(providerId: int) -> tuple:
    now = datetime.datetime.now()
    result = json.loads(subprocess.run(['speedtest', '-s', str(providerId), '-f', 'json'], stdout=subprocess.PIPE).stdout)
    return (now.strftime("%Y-%m-%d-%H:%M:%S"), round(result["ping"]["latency"]), round(result["download"]["bandwidth"]/125000), round(result["upload"]["bandwidth"]/125000))


def saveResults(filename: str, result: tuple):
    print("{} {} {} {}".format(result[0], result[1], result[2], result[3]))
    f = open(filename, "a")
    f.write("{} {} {} {}\n".format(result[0], result[1], result[2], result[3]))
    f.close()


def main():
    # Generacja
    # serverId = 11965
    # Connecta
    serverId = 26265
    # Korbank
    # serverId = 5679
    logFile = sys.argv[1] if len(sys.argv) > 1 else "speedtest.serverId.log"
    while True:
        try:
            saveResults(logFile, speedtest(serverId))
            sleep(300)
        except KeyboardInterrupt:
            print("losing^")
            sys.exit()


if __name__ == '__main__':
    main()
