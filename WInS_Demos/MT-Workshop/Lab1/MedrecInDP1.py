connect('weblogic','welcome1','t3://localhost:7001')
edit()

startEdit()
cd('/Partitions/dp1/ResourceGroups/app1RG')
cmo.createMailSession('MedRecMailSession')
cd('/Partitions/dp1/ResourceGroups/app1RG/MailSessions/MedRecMailSession')
cmo.setJNDIName('mail/MedRecMailSession')
activate()

startEdit()
cd('/Partitions/dp1/ResourceGroups/app1RG')
cmo.createFileStore('MedRec-fs')
activate()

startEdit()
cd('/Partitions/dp1/ResourceGroups/app1RG')
cmo.createJMSServer('MedRecJMSServer')
cd('/Partitions/dp1/ResourceGroups/app1RG/JMSServers/MedRecJMSServer')
cmo.setPersistentStore(getMBean('/Partitions/dp1/ResourceGroups/app1RG/FileStores/MedRec-fs'))
activate()


startEdit()
cd('/Partitions/dp1/ResourceGroups/app1RG')
cmo.createJMSSystemResource('MedRecModule')
activate()

startEdit()
cd('/Partitions/dp1/ResourceGroups/app1RG/JMSSystemResources/MedRecModule')
cmo.createSubDeployment('MedRecJMS ')
cd('/Partitions/dp1/ResourceGroups/app1RG/JMSSystemResources/MedRecModule/SubDeployments/MedRecJMS')
set('Targets',jarray.array([ObjectName('com.bea:Name=MedRecJMSServer,Type=JMSServer,Partition=dp1,ResourceGroup=app1RG')], ObjectName))
activate()

startEdit()
cd('/Partitions/dp1/ResourceGroups/app1RG/JMSSystemResources/MedRecModule/JMSResource/MedRecModule')
cmo.createConnectionFactory('MedRecConnectionFactory')
cd('/Partitions/dp1/ResourceGroups/app1RG/JMSSystemResources/MedRecModule/JMSResource/MedRecModule/ConnectionFactories/MedRecConnectionFactory')
cmo.setJNDIName('com.oracle.medrec.jms.connectionFactory ')
cd('/Partitions/dp1/ResourceGroups/app1RG/JMSSystemResources/MedRecModule/JMSResource/MedRecModule/ConnectionFactories/MedRecConnectionFactory/SecurityParams/MedRecConnectionFactory')
cmo.setAttachJMSXUserId(false)
cd('/Partitions/dp1/ResourceGroups/app1RG/JMSSystemResources/MedRecModule/JMSResource/MedRecModule/ConnectionFactories/MedRecConnectionFactory/ClientParams/MedRecConnectionFactory')
cmo.setClientIdPolicy('Restricted')
cmo.setSubscriptionSharingPolicy('Exclusive')
cmo.setMessagesMaximum(10)
cd('/Partitions/dp1/ResourceGroups/app1RG/JMSSystemResources/MedRecModule/JMSResource/MedRecModule/ConnectionFactories/MedRecConnectionFactory/TransactionParams/MedRecConnectionFactory')
cmo.setXAConnectionFactoryEnabled(true)
cd('/Partitions/dp1/ResourceGroups/app1RG/JMSSystemResources/MedRecModule/SubDeployments/MedRecJMS')
set('Targets',jarray.array([ObjectName('com.bea:Name=MedRecJMSServer,Type=JMSServer,Partition=dp1,ResourceGroup=app1RG')], ObjectName))
cd('/Partitions/dp1/ResourceGroups/app1RG/JMSSystemResources/MedRecModule/JMSResource/MedRecModule/ConnectionFactories/MedRecConnectionFactory')
cmo.setSubDeploymentName('MedRecJMS')
activate()

startEdit()
cd('/Partitions/dp1/ResourceGroups/app1RG/JMSSystemResources/MedRecModule/JMSResource/MedRecModule')
cmo.createUniformDistributedQueue('PatientNotificationQueue')
cd('/Partitions/dp1/ResourceGroups/app1RG/JMSSystemResources/MedRecModule/JMSResource/MedRecModule/UniformDistributedQueues/PatientNotificationQueue')
cmo.setJNDIName('com.oracle.medrec.jms.PatientNotificationQueue')
cd('/Partitions/dp1/ResourceGroups/app1RG/JMSSystemResources/MedRecModule/SubDeployments/MedRecJMS')
set('Targets',jarray.array([ObjectName('com.bea:Name=MedRecJMSServer,Type=JMSServer,Partition=dp1,ResourceGroup=app1RG')], ObjectName))
cd('/Partitions/dp1/ResourceGroups/app1RG/JMSSystemResources/MedRecModule/JMSResource/MedRecModule/UniformDistributedQueues/PatientNotificationQueue')
cmo.setSubDeploymentName('MedRecJMS')
activate()

startEdit()
deploy(appName='medrec', partition='dp1', resourceGroup='app1RG', path='/u01/content/weblogic-innovation-seminars/WInS_Demos/MT-Workshop/Lab1/medrec.ear')
deploy(appName='physician', partition='dp1', resourceGroup='app1RG', path='/u01/content/weblogic-innovation-seminars/WInS_Demos/MT-Workshop/Lab1/physician.ear')
deploy(appName='chat', partition='dp1', resourceGroup='app1RG', path='/u01/content/weblogic-innovation-seminars/WInS_Demos/MT-Workshop/Lab1/chat.war')
activate()

disconnect()