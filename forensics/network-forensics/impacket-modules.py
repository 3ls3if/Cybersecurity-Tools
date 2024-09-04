#!/usr/bin/python3


import sys
from pcapy import open_offline, open_live
from impacket.ImpactDecoder import EthDecoder

class ImpacketDemo(object):
	def __init__(self):
		super(ImpacketDemo, self).__init__()
		pass


	def read_packet(self, hdr, data):
		decoder = EthDecoder()
		ether = decoder.decode(data)
		
		ip = ether.child()
		tcp = ip.child()
		#print(tcp)
		
		try:
			print(ip.get_ip_src())
			print(tcp.get_th_sport())
		except:
			pass

	def main(self, pcap_file):
		pcap = open_offline(pcap_file)

		#print(pcap)

		pcap.loop(0, self.read_packet)


if __name__ == '__main__':
	if len(sys.argv) <=1:
		sys.exit(f"Usage: {sys.argv[0]} <filename>")

	demo = ImpacketDemo()
	demo.main(sys.argv[1])



