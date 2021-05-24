#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

#General Imports
import sys
import os
from os import path
import csv
import json
import datetime
from datetime import datetime,timezone
from configparser import ConfigParser
import time

import dpkt
import pcap
from scapy.all import *

LoggerConfFile = "usr/local/etc/ipanalyzer/ipanalyzer.conf"
LoggerCSVPath = "/usr/local/opnsense/scripts/OPNsense/IPAnalyzer/http_requests.csv"
BadIpFile = "usr/local/opnsense/resources/sample_bad_ips.txt"

result = {}
fields = ['timestamp','id','srcEth','IPsrc','srcPort','destEth','IPdest','destPort', 'nature']
stop = false

# def filterPacket(f):
#     nature = "good IP"
#     lines = []
#
#     with open(BadIpFile) as badIpFile
#     lines = badIpFile.readlines()
#
#     pc = pcap.pcap(name = sys.argv[2])
#     pc.setfilter('udp dst port 53')
#
#     for ts, pkt in pc:
#             #take Ethernet interface where to take DNS requests
#             #Parse the packet. Check if the network interface is IP
#             eth = dpkt.ethernet.Ethernet(pkt)
#             if eth.type == dpkt.ethernet.EHT_TYPE_IP:
#                 ip = eth.data
#                 #Check if the protocol is UDP
#                 if ip.p == dpkt.IP_PROTO_UDP:
#                     udp = ip.data
#
#                     ip = dpkt.ip.IP(udp.data)
#
#                     if str(src) in lines:
#                         nature = "BAD IP!"
#
#                     ts = str(datetime.datetime.utcfromtimestamp(ts))
#
#                     currentPacket = {
#                         'timestamp': ts,
#                         'srcEth': eth.src,
#                         'IPsrc': ip.src,
#                         'id': ip.id,
#                         'srcPort': udp.sport,
#                         'destEth': eth.dst,
#                         'IPdest': ip.dst,
#                         'destPort': udp.dport,
#                         'qr': ip.qr,
#                         'nature': nature
#                     }
#
#             csv.writer(f,delimiter=',').writerow(currentPacket)

def start_filter(packet):

    global f

    nature = "good IP"
    lines = []
    with open(BadIpFile) as badIpFile
    lines = badIpFile.readlines()

    srcIp = packet[IP].src
    dstIp = packet[IP].dst
    udpSport = packet[UDP].sport
    udpDport = packet[UDP].dport
    srcEth = packet[Ether].src
    dstEth = packet[Ether].dst

    if srcIp in lines:
        nature = "BAD IP!"

    ts = packet.time
    ts = time.gmtime(ts)
    ts_asc = time.asctime(ts)

    currentPacket = [ts_asc, str(srcEth), str(srcIp), '', str(udpSport), str(dstEth), str(dstIp), str(udpDport), nature]

    csv.writer(f,delimiter',').writerow(currentPacket)

def stop_filter(packet):
    return stop

# get 10-th more recent requests
def readPacketsFromFile(csvFile):
    requests = []
    if not csvFile.closed:
        data = csv.reader(csvFile,delimiter=',')
        for data in requests:
            data[0] = datetime.fromtimestamp(float(data[0])).isoformat()
            requests.append(data)
    requests = sorted(requests, reverse=True)
    print(json.dumps(requests[:10],file=sys.stdout)
    quit()

def performOperation(csvFilePath):

    global f

    arg = ''
    if len(sys.argv) > 1:
         arg = str(sys.argv[1])
    else:
         quit()

    p = not os.path.exists(csvFilePath)
    if p:
        f = open(csvFilePath,'w',encoding = 'utf-8')
        csv.writer(f,delimiter=',').writerow(fields)
        fclose(f)

    if arg == "-log":
         f = open(csvFilePath,'r', encoding = 'utf-8')
         readPacketsFromFile(f)
         fclose(f)
    elif arg == "-i":
         f = open(LoggerCSVPath,'a',encoding = 'utf-8')
         if str(sys.argv[2]) == "em0" or str(sys.argv[2]) == "em1" :
#              filterPacket(f)
             sniff(iface=str(sys.argv[2]), filter='udp', stop_filter=stop_filter, prn=start_filter, count=0)
         fclose(f)
    elif arg == "-stop":
         stop = true

def main():
    if os.path.exists(LoggerConfFile):
        cnf = ConfigParser()
        cnf.read(LoggerConfFile)
        if cnf.has_section("general"):
            performOperation(LoggerCSVPath)
         else:
            result["message"] = "no section general found in ipanalyzer.conf"
    else:
        result["message"] = "no configuration file found"

    print(json.dumps(result))

#Entry point to the main  script
if __name__ == "__main__":
    main()