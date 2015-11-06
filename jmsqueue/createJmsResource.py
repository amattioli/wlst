#This script starts an edit session, creates a JMS Server, 
#targets the jms server to the server WLST is connected to and creates
#a JMS System module with a jms queue and connection factory. The 
#jms queues and topics are targeted using sub-deployments. 
import sys
from java.lang import System

print "@@@ Starting the script ..."

myJmsSystemResource = "CapiQueue-jms"
factoryName = "CConFac"
jmsServerName = "myJMSServer"
queueName = "CQueue"

url = "t3://localhost:7101"
usr = "weblogic"
password = "weblogic1"

connect(usr,password, url)
edit()
startEdit()

#Step 1
servermb=getMBean("Servers/DefaultServer")
if servermb is None:
    print '@@@ No server MBean found'

else:
    #Step 2
    jmsMySystemResource = create(myJmsSystemResource,"JMSSystemResource")

    #Step 3
    jmsMySystemResource.addTarget(servermb)

    #Step 4
    theJMSResource = jmsMySystemResource.getJMSResource()

    #Step 5
    connfact1 = theJMSResource.createConnectionFactory(factoryName)
    jmsqueue1 = theJMSResource.createQueue(queueName)

    #Step 6
    connfact1.setJNDIName(factoryName)
    jmsqueue1.setJNDIName(queueName)

    #Step 7
    jmsqueue1.setSubDeploymentName('DeployToJMSServer1')  
    connfact1.setSubDeploymentName('DeployToJMSServer1')

    #Step 8
    jmsserver1mb = create(jmsServerName,'JMSServer')

    #Step 9
    jmsserver1mb.addTarget(servermb)

    #Step 10
    subDep1mb = jmsMySystemResource.createSubDeployment('DeployToJMSServer1')

    #Step 11
    subDep1mb.addTarget(jmsserver1mb)
	
    save()
    activate()