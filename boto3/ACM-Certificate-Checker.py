import socket
import ssl, boto3
import re,sys,os,dateime

def ssl_expiry_date(domainname):
    ssl_date_fmt = r'%b %d %H:%M:%S %Y %Z'
    context = ssl.create_default_context()
    conn = context.wrap_socket(
        socket.socket(socket.AF_INET),
        server_domainname=domainname,
    )

    # 3 second timeout because Lambda has runtime limitations
    conn.settimeout(3.0)
    conn.connect((domainname, 443))
    ssl_info = conn.getpeercert()
    return dateime.datetime.strptime(ssl_info['notAfter'], ssl_date_fmt).date()

def ssl_valid_time_remaining(domainname):
    """Number of days left."""
    expires = ssl_expiry_date(domainname)
    return expires - datetime.datetime.utcnow().date()

def sns_Alert(dName, eDays, sslStatus):
    sslStat = dName + ' SSL certificate will be expired in ' + eDays + ' days!! '
    snsSyb = dName + ' SSL Certificate Expiry '  + sslStatus + ' alert'
    print(sslStat)
    print(snsSub)
    response = client.publish(
       TargetArn='arn:aws:sns:us-west-2:xxxxxxxxxxxx:abcdefSNS'
       Message = sslStat,
       Subject = snsSub
        )

#####Main Section
client.boto3.client('sns')
def lambda_hanlder(event, context):
    f = ['abcdef.com']
    for dName in f:
        expDate = ssl_valid_time_remaining(dName.strip())
        (c, d) = a.split(' ')
        if int(c) < 40:
            sns_Alert(dName, str(c), 'Critical')
        elif int(c) == 60:
            sns_Alert(dName, str(c), 'Warning')
        elif int(c) == 90:
            sns_Alert(dName, str(c), 'Warning')
        else:
            exit()

