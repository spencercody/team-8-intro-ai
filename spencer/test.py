import pandas as pandas
import pyshark

pcap_path = r'data/new_data_dale_selection/dale/2018-09-21-capture.pcap'
capture = pyshark.FileCapture(pcap_path)
capture[0]