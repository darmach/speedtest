#!/usr/bin/env python3
import subprocess
import json
import datetime
from time import sleep
import sys
from multimethod import multimethod


@multimethod
def speedtest(providerId: int) -> tuple:
    now = datetime.datetime.now()
    result = json.loads(subprocess.run(['speedtest', '-s', str(providerId), '-f', 'json'], stdout=subprocess.PIPE).stdout)
    return (now.strftime("%Y-%m-%d-%H:%M:%S"), str(round(result["ping"]["latency"]))+" ms", str(round(result["download"]["bandwidth"]/125000))+" Mb", str(round(result["upload"]["bandwidth"]/125000))+" Mb")


@multimethod
def speedtest(providerTuple: tuple) -> tuple:
    now = datetime.datetime.now()
    resultDict = dict()
    for singleProvider in providerTuple:
        resultDict[singleProvider] = json.loads(subprocess.run(['speedtest', '-s', str(singleProvider), '-f', 'json'], stdout=subprocess.PIPE).stdout)
    return (now.strftime("%Y-%m-%d %H:%M:%S"),
            round(resultDict[providerTuple[0]]["ping"]["latency"]), round(resultDict[providerTuple[0]]["download"]["bandwidth"]/125000), round(resultDict[providerTuple[0]]["upload"]["bandwidth"]/125000),
            round(resultDict[providerTuple[1]]["ping"]["latency"]), round(resultDict[providerTuple[1]]["download"]["bandwidth"]/125000), round(resultDict[providerTuple[1]]["upload"]["bandwidth"]/125000),
            round(resultDict[providerTuple[2]]["ping"]["latency"]), round(resultDict[providerTuple[2]]["download"]["bandwidth"]/125000), round(resultDict[providerTuple[2]]["upload"]["bandwidth"]/125000))


def saveResults(filename: str, result: tuple):
    resultString = str()
    for i in result:
        resultString += str(i)+" "
    print(resultString)
    f = open(filename, "a")
    f.write(resultString+"\n")
    f.close()


def main():
    # Provider list
    providers = (11965, 36250, 5679)
    # Generacja
    # serverId = 11965
    # Connecta doesnt seem to work anymore
    # serverId = 26265
    # Orange
    # serverId = 36250
    # Korbank
    # serverId = 5679

    logFile = sys.argv[1] if len(sys.argv) > 1 else "speedtest.log"
    while True:
        try:
            saveResults(logFile, speedtest(providers))
            sleep(300)
        except KeyboardInterrupt:
            print("losing^")
            sys.exit()

    # print(speedtest(serverId))


if __name__ == '__main__':
    main()
