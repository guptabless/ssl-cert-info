import bcolors
import sys, argparse
import ssl
import socket
import os

def banner():
    print("""

            ░██████╗░██████╗██╗░░░░░░░░░░░░█████╗░███████╗██████╗░████████╗░░░░░░██╗███╗░░██╗███████╗░█████╗░
            ██╔════╝██╔════╝██║░░░░░░░░░░░██╔══██╗██╔════╝██╔══██╗╚══██╔══╝░░░░░░██║████╗░██║██╔════╝██╔══██╗
            ╚█████╗░╚█████╗░██║░░░░░█████╗██║░░╚═╝█████╗░░██████╔╝░░░██║░░░█████╗██║██╔██╗██║█████╗░░██║░░██║
            ░╚═══██╗░╚═══██╗██║░░░░░╚════╝██║░░██╗██╔══╝░░██╔══██╗░░░██║░░░╚════╝██║██║╚████║██╔══╝░░██║░░██║
            ██████╔╝██████╔╝███████╗░░░░░░╚█████╔╝███████╗██║░░██║░░░██║░░░░░░░░░██║██║░╚███║██║░░░░░╚█████╔╝
            ╚═════╝░╚═════╝░╚══════╝░░░░░░░╚════╝░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░░░░░░░╚═╝╚═╝░░╚══╝╚═╝░░░░░░╚════╝░
                                                                                                  Code By: NG
              """
          )
if len(sys.argv) > 1:
    banner()
    if (sys.argv[1] != 'd'):
        try:
              input_url = sys.argv[2]
              parser = argparse.ArgumentParser()
              parser.add_argument("-d", required=True)

              print(bcolors.BITALIC + "Testing for SSL Certificate Information")
              if (os.path.exists(input_url) == True):
               file = open(input_url, "r")
               lines = file.readlines()
               for te_url in lines:
                strip_url = te_url.strip()
                print('**************************************************************')
                print(bcolors.BOLD ,te_url)
                c = ssl.create_default_context()
                with c.wrap_socket(socket.socket(), server_hostname=strip_url) as s:
                    s.connect((strip_url, 443))
                    cert = s.getpeercert()
                  #  print('cert',cert)
                subject = dict(x[0] for x in cert['subject'])
                issued_to = subject['commonName']
                print('Certificate issued to', bcolors.BOLD + issued_to)
                issuer = dict(x[0] for x in cert['issuer'])
                issued_by = issuer['commonName']
                print('Certificate issued BY',bcolors.BOLD + issued_by)

                countryName = dict(x[0] for x in cert['issuer'])
                country = countryName['countryName']
                print("Country", bcolors.BOLD + country)

              elif (os.path.exists(input_url) != True):
                    print('**************************************************************')
                    print(bcolors.BOLD, input_url)
                    c = ssl.create_default_context()
                    with c.wrap_socket(socket.socket(), server_hostname=input_url) as s:
                            s.connect((input_url, 443))
                            cert = s.getpeercert()
                        #  print('cert',cert)
                    subject = dict(x[0] for x in cert['subject'])
                    issued_to = subject['commonName']
                    print('Certificate issued to', bcolors.BOLD + issued_to)
                    issuer = dict(x[0] for x in cert['issuer'])
                    issued_by = issuer['commonName']
                    print('Certificate issued BY', bcolors.BOLD + issued_by)

                    countryName = dict(x[0] for x in cert['issuer'])
                    country = countryName['countryName']
                    print("Country", bcolors.BOLD + country)
        except:
                print(bcolors.OKMSG + 'Please enter python sslCertInfo.py -u <valid URL with https:// or http://> ')
    elif (sys.argv[1] == '-h'):
            print(bcolors.BOLD + 'usage: sslCertInfo.py [-h] -d DOMAIN' '\n' 'OPTIONS:' '\n' '-h,--help    '
                                 'show this help message and exit' '\n''-d DOMAIN,   --domain domain which certificate you want to check')
    elif (sys.argv[1] != '-d'):
            print(bcolors.OKMSG + 'Please enter -d < valid domain >')
    else:
        banner()
        print(bcolors.ERR + 'Please select at-least 1 option from -d or -h, with a valid domain')


#C:\Users\gupta\PycharmProjects\miraa\sslcert.txt
