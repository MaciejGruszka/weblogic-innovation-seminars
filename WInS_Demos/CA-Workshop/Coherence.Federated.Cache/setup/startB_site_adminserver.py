print "*************** Starting Admin Server in B_site_domain *****************"
nmConnect('weblogic','welcome1',domainName='B_site_domain',port='5559',host='localhost')
nmStart('AdminServer')
exit()