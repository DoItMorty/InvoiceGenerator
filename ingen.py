import argparse
import time
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

invoiceNum = str(9999)


doc = Document(documentclass='letter')
doc.packages.append(Package('invoice'))

#This needs work to fix backticks 
doc.preamble.append(Command('address', args.myname  + myaddress[0] \
	+ myaddress[1] + args.myemail))
doc.preamble.append(Command('date', date))

doc.append(Command(command='begin', arguments='letter', \
	extra_arguments=args.clientname + clientaddress[0] + \
	clientaddress[1]))


doc.append(Command(command='opening', arguments='Invoice ' + invoiceNum))
doc.append(Command(command='begin', arguments='invoice', extra_arguments=['USD','0']))
doc.append(Command(command='ProjectTitle', arguments=args.title))

#Fee



doc.append(Command(command='end', arguments='invoice'))
doc.append(Command(command='closing', arguments=args.notes))
doc.append(Command(command='end', arguments='letter'))
doc.generate_tex()




