##########
# VMWare #
##########
- For this workshop you'll need the latest version of VMWare Workstation (Windows), Fusion (Mac), or Player.

- http://www.vmware.com/ap/products/player.html


- Although you can get the VM to run in VirtualBox, I will not be supporting this configuration for this class.

Here is the VMWare virtual machine for the class:
 
https://s3.amazonaws.com/StrategicSec-VMs/StrategicsecUbuntu-v3.zip
 
user: strategicsec
 
pass: strategicsec


####################
# Intro to TCPDump #
####################
sudo apt-get install tcpdump



Basic sniffing

sudo tcpdump -n


Now lets increase the display resolution of this packet, or get more details about it. The verbose switch comes in handy
sudo tcpdump -v -n



Getting the ethernet header (link layer headers)

In the above examples details of the ethernet header are not printed. Use the -e option to print the ethernet header details as well.
sudo tcpdump -vv -n -e


Sniffing a particular interface

In order to sniff a particular network interface we must specify it with the -i switch. First lets get the list of available interfaces using the -D switch.
sudo tcpdump -D


Filtering packets using expressions
Selecting protocols

$ sudo tcpdump -n tcp


Particular host or port

Expressions can be used to specify source ip, destination ip, and port numbers. The next example picks up all those packets with source address 192.168.1.101

$ sudo tcpdump -n 'src 192.168.1.101'


Next example picks up dns request packets, either those packets which originate from local machine and go to port 53 of some other machine.

$ sudo tcpdump -n 'udp and dst port 53'


To display the FTP packets coming from 192.168.1.100 to 192.168.1.2

$ sudo tcpdump 'src 192.168.1.100 and dst 192.168.1.2 and port ftp'


Search the network traffic using grep

Grep can be used along with tcpdump to search the network traffic. Here is a very simple example

$ sudo tcpdump -n -A | grep -e 'POST'


So what is the idea behind searching packets. Well one good thing can be to sniff passwords.
Here is quick example to sniff passwords using egrep


tcpdump port http or port ftp or port smtp or port imap or port pop3 -l -A | egrep -i 'pass=|pwd=|log=|login=|user=|username=|pw=|passw=|passwd=|password=|pass:|user:|username:|password:|login:|pass |user ' --color=auto --line-buffered -B20




#########
# NGrep #
#########

Install ngrep on Ubuntu
$ sudo apt-get install ngrep


Search network traffic for string "User-Agent: "
$ sudo ngrep -d eth0 "User-Agent: " tcp and port 80

In the above command :
a) tcp and port 80 - is the bpf filter (Berkeley Packet Filter) , that sniffs only TCP packet with port number 80
b) The d option specifies the interface to sniff. eth0 in this case.
c) "User-Agent: " is the string to search for. All packets that have that string are displayed.

2. Search network packets for GET or POST requests :

$ sudo ngrep -l -q -d eth0 "^GET |^POST " tcp and port 80

The l option makes the output buffered and the q option is for quiet ( Be quiet; don't output any information other than packet headers and their payloads (if relevant) ).

3. ngrep without any options would simply capture all packets.

$ sudo ngrep

https://dl.packetstormsecurity.net/papers/general/ngreptut.txt

$ sudo ngrep -d eth0 -n 3

$ sudo ngrep -d any port 25
This will let you monitor all activity crossing source or destination port 25
(SMTP). 

$ sudo ngrep -wi -d wlan0 'user|pass' port 6667

$ sudo ngrep -wi -d any 'user|pass' port 21


###############
# NTop Basics #
###############
Reference:
https://www.maketecheasier.com/install-configure-ntop/
https://easyipv6.wordpress.com/2014/08/22/how-to-configure-ntopng-for-collecting-sflow-packets/


#################
# PCAP Analysis #
#################
cd /home/malware/Desktop/Browser\ Forensics
 
ls | grep pcap
 
perl chaosreader.pl suspicious-time.pcap
 
firefox index.html
 
cat index.text | grep -v '"' | grep -oE "([0-9]+\.){3}[0-9]+.*\)"
 
cat index.text | grep -v '"' | grep -oE "([0-9]+\.){3}[0-9]+.*\)" | awk '{print $4, $5, $6}' | sort | uniq -c | sort -nr
 
sudo tshark -i eth0 -r suspicious-time.pcap -qz io,phs
     malware  
 
 
for i in session_00[0-9]*.www.html; do srcip=`cat "$i" | grep 'www:\ ' | awk '{print $2}' |  cut -d ':' -f1`; dstip=`cat "$i" | grep 'www:\ ' | awk '{print $4}' |  cut -d ':' -f1`; host=`cat "$i" | grep 'Host:\ ' | sort -u | sed -e 's/Host:\ //g'`; echo "$srcip --> $dstip = $host";  done | sort -u
 
 
 
 
 
#############################
# PCAP Analysis with tshark #
#############################
tshark -r suspicious-time.pcap | grep 'NB.*20\>' | sed -e 's/<[^>]*>//g' | awk '{print $3,$4,$9}' | sort -u
 
 
tshark -r suspicious-time.pcap | grep 'NB.*1e\>' | sed -e 's/<[^>]*>//g' | awk '{print $3,$4,$9}' | sort -u
 
 
tshark -r suspicious-time.pcap arp | grep has | awk '{print $3," -> ",$9}' | tr -d '?'
 
 
tshark -r suspicious-time.pcap -Tfields -e "eth.src" | sort | uniq
 
 
tshark -r suspicious-time.pcap -R "browser.command==1" -Tfields -e "ip.src" -e "browser.server" | uniq
 
tshark -r suspicious-time.pcap -Tfields -e "eth.src" | sort |uniq
 
tshark -r suspicious-time.pcap -qz ip_hosts,tree
 
tshark -r suspicious-time.pcap -R "http.request" -Tfields -e "ip.src" -e "http.user_agent" | uniq
 
tshark -r suspicious-time.pcap -R "dns" -T fields -e "ip.src" -e "dns.flags.response" -e "dns.qry.name"
 
 
whois rapidshare.com.eyu32.ru
 
whois sploitme.com.cn
 
 
tshark -r suspicious-time.pcap -R http.request  -T fields -e ip.src -e ip.dst -e http.host -e http.request.uri | awk '{print $1," -> ",$2, "\t: ","http://"$3$4}'
 
tshark -r suspicious-time.pcap -R http.request  -T fields -e ip.src -e ip.dst -e http.host -e http.request.uri | awk '{print $1," -> ",$2, "\t: ","http://"$3$4}' | grep -v -e '\/image' -e '.css' -e '.ico' -e google -e 'honeynet.org'
 
tshark -r suspicious-time.pcap -qz http_req,tree
 
tshark -r suspicious-time.pcap -R "data-text-lines contains \"<script\"" -T fields -e frame.number -e ip.src -e ip.dst
 
tshark -r suspicious-time.pcap -R http.request  -T fields -e ip.src -e ip.dst -e http.host -e http.request.uri | awk '{print $1," -> ",$2, "\t: ","http://"$3$4}' | grep -v -e '\/image' -e '.css' -e '.ico'  | grep 10.0.3.15 | sed -e 's/\?[^cse].*/\?\.\.\./g'
 
 
 
######################################
# PCAP Analysis with forensicPCAP.py #
######################################
cd ~/Desktop
wget https://raw.githubusercontent.com/madpowah/ForensicPCAP/master/forensicPCAP.py
 
sudo easy_install cmd2
     malware
 
python forensicPCAP.py Browser\ Forensics/suspicious-time.pcap
 
ForPCAP >>> help
 
 
Prints stats about PCAP
ForPCAP >>> stat
 
 
Prints all DNS requests from the PCAP file. The id before the DNS is the packet's id which can be use with the "show" command.
ForPCAP >>> dns
 
ForPCAP >>> show
 
 
Prints all destination ports from the PCAP file. The id before the DNS is the packet's id which can be use with the "show" command.
ForPCAP >>> dstports
 
ForPCAP >>> show
 
 
Prints the number of ip source and store them.
ForPCAP >>> ipsrc
 
ForPCAP >>> show
 
 
Prints the number of web's requests and store them
ForPCAP >>> web
 
ForPCAP >>> show
 
Prints the number of mail's requests and store them
ForPCAP >>> mail
 
ForPCAP >>> show


##############################################
# Packet Analysis/Network Forensics Homework #
#############################################
In order to receive your certificate of attendance you must complete the all of the quizzes on the http://linuxsurvival.com/linux-tutorial-introduction/ website.


Submit the results via email in an MS Word document with (naming convention example: YourFirstName-YourLastName-PA-NF-Homework.docx)




###############################################
# Packet Analysis/Network Forensics Challenge #
###############################################

In order to receive your certificate of proficiency you must complete all of the tasks covered in the Packet Analysis/Network Forensics pastebin (http://pastebin.com/SwgnkAhQ).

Submit the results via email in an MS Word document with (naming convention example: YourFirstName-YourLastName-PA-NF-Challenge.docx)




IMPORTANT NOTE:
Your homework/challenge must be submitted via email to both (joe-at-strategicsec-.-com and kasheia-at-strategicsec-.-com) by Sunday October 23rd at midnight EST.