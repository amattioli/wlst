# ................  import ........................
from java.util import Properties
 
###################################################################
def createMailSession():                                                                                                                                                                    
    try:
        print 'Create EMail session ...';
        edit();
        startEdit();
 
        cd('/')
        myTestMailMbean = cmo.createMailSession('TestNotificationEmail');
        cd('/MailSessions/TestNotificationEmail');
        set('Targets',jarray.array([ObjectName('com.bea:Name=DefaultServer,Type=Server')], ObjectName))
        myTestMailMbean.setJNDIName('mail/TestNotificationEmail');
 
        properties = java.util.Properties();
        properties.put('mail.to','lector@wlsscriptbook.com');
        properties.put('mail.from','author@wlsscriptbook.com');
 
        properties.put('mail.transport.protocol','smtp');
        properties.put('mail.smtp.host','mail.wlsscriptbook.com');
        properties.put('mail.smtp.port','25');
        properties.put('mail.smtp.user','username');
        properties.put('mail.smtp.password','password');
        myTestMailMbean.setProperties(properties);
#See the book code download for full script
 
 
        save();
        activate();
 
    except:
        print 'Exception while create EMail session  !';
        dumpStack();
        exit();
 
 
# ================================================================                                                                                                                          
#           Main Code Execution                                                                                                                                                            
# ================================================================                                                                                                                         
if __name__== "main":                                                                                                                                                                       
        print '###################################################################';
        print '#                 Test create Mail session                        #';
        print '###################################################################';
        print '';
        connect('weblogic', 'weblogic1',  't3://localhost:7101');
        createMailSession()
        disconnect();  