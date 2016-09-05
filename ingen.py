import argparse
import time
import os
from pylatex import Document, Package, Command
from pylatex.utils import NoEscape

#Command line arguments
parser = argparse.ArgumentParser(description='SeaSquids Invoice Generator',
    usage='Havent quite figured it out yet')

parser.add_argument('--client',required='True',help='Client template to use')
parser.add_argument('--line',nargs='?',action='append',required='True',
    help='Information for lines. May specify more than once for multiple lines.')
parser.add_argument('--title',help='Project Title')
parser.add_argument('--myname',help='Your Name')
parser.add_argument('--myaddress',help='street;zip')
parser.add_argument('--myemail',help='Your Email')
parser.add_argument('--clientname',help='Recipent Name')
parser.add_argument('--clientaddress',help='street;zip')
parser.add_argument('--notes',help='Additional Notes')
args = parser.parse_args()

date = time.strftime("%m/%d/%y")

myaddress = args.myaddress.split(';')
clientaddress = args.clientaddress.split(';')


clientdir = './' + args.clientname

numbag = len(os.listdir(clientdir))
nextfile = numbag + 1
invoiceNum = str(nextfile)

doc = Document(documentclass='letter', default_filepath='./' + args.clientname \
	+ '/' + invoiceNum)
doc.packages.append(Package('invoice'))

EscapeMe = args.myname + '\\\\' + myaddress[0] + '\\\\' + myaddress[1] + '\\\\' + args.myemail
doc.preamble.append(Command('address', NoEscape(EscapeMe)))

doc.preamble.append(Command('date', date))

EscapeThem = args.clientname + '\\\\' + clientaddress[0] + '\\\\' + clientaddress[1]
doc.append(Command('begin', NoEscape(EscapeThem)))

doc.append(Command(command='opening', arguments='Invoice ' + invoiceNum))
doc.append(Command(command='begin', arguments=['invoice', 'USD', '0']))
doc.append(Command(command='ProjectTitle', arguments=args.title))

#Line Item Generation 
for i in range(len(args.line)):
	split1 = args.line[i]
	newsplit = split1.split(';')
	doc.append(Command(command='fee', arguments=[newsplit[0], newsplit[1], \
		newsplit[2]]))

#Closing Arguments (heh)
doc.append(Command(command='end', arguments='invoice'))
doc.append(Command(command='closing', arguments=args.notes))
doc.append(Command(command='end', arguments='letter'))

doc.generate_tex()

