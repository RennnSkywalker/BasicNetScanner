import scapy.all as scapy
import optparse

#1)arp request
#2)broadcast
#3)response
def get_user_input():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-i", "--ipaddress",dest="ip_address",help="Enter IP Adress(10.0.2.1/24)")
    (user_input,arguments) = parse_object.parse_args()
    if not user_input.ip_address:
        print("Enter IP Address!!")
    return user_input

def scan_my_network(ip):
    arp_request_packet = scapy.ARP(pdst=ip)  #ARP paketi oluşturma
    #scapy.ls(scapy.ARP())
    broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff") #bu mac adresi default modemlerin mac adresidir.
    #scapy.ls(scapy.Ether())
    combined_packet = broadcast_packet / arp_request_packet # 2 paketi tek pakette birleştirir
    (answered_list, unanswered_list) = scapy.srp(combined_packet, timeout=1)  # paketleri ağa gönderir cevapları toplar
    answered_list.summary()

user_ip_address = get_user_input()
scan_my_network(user_ip_address.ip_address)