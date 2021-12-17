########################################
#Setup HTTP server on Ubuntu
#######################################
#
#sudo apt-get update 
#sudo apt-get install apache2 -y  
#sudo systemctl start apache2  
#systemctl enable apache2  
#ps awux | grep apache2 | grep -v grep | head -1
#Create dir junosConfig 
#mkdir /var/www/html/junosConfig
#Create config file conffile under /var/www/html/junosConfig
#Add config statements to the conffile
#vi /var/www/html/junosConfig
#set system syslog file test1 any any
#
#####################################

from jnpr.junos import Device
from jnpr.junos.utils.config import Config
dev = Device(host='xx.xx.xx.xx', user='xyz', password='xyz', gather_facts=False)
dev.open()
cu = Config(dev)
httpcmd = 'http://xx.xx.xx.xx/junosConfig/conffile'
cu.load(url=httpscmd,format='set')
cu.pdiff()
if cu.commit_check():
   cu.commit()
else:
   cu.rollback()
