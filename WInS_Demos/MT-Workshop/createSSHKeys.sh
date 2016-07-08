# Enter the arguments for -N (This is to specify the passpharase, you can leave it blank),Please dont change anything else 

ssh-keygen -t rsa -N "" -b "2048" -C "winsmt" -f /u01/content/weblogic-innovation-seminars/cloud.demos/pk.openssh
cd /u01/content/weblogic-innovation-seminars/cloud.demos/
chmod 600 pk.openssh
