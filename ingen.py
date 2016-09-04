import argparse
import time

#Configurating argparse
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

myaddress = args.myaddress
myaddrsplit = myaddress.split(';')
mystreet = myaddrsplit[0]
myzip = myaddrsplit[1]


clientaddress = args.clientaddress
clientaddrsplit = clientaddress.split(';')
clientstreet = clientaddrsplit[0]
clientzip = clientaddrsplit[1]


template = """
\documentclass{letter}
\usepackage{invoice} 
\\address{%myname \\\\ %mystreet \\\\ %myzip \\\\ %myemail} 
\date{%date}

\\begin{document}
\\begin{letter}{%clientname \\\\ %clientstreet \\\\ %clientzip}
\opening{invoice %invoicenumber}
\\begin{invoice}{USD}{0}
\ProjectTitle{%title}

\\fee{%description} {%unitprice} {%quantity}

\end{invoice}
\closing{%notes}
\end{letter}
\end{document}

"""

for line in template:
    l1 = template.replace('%date',date)
    l2 = l1.replace('%title',args.title)
    l3 = l2.replace('%myname',args.myname)
    l4 = l3.replace('%mystreet',mystreet)
    l5 = l4.replace('%myzip',myzip)
    l6 = l5.replace('%myemail',args.myemail)
    l7 = l6.replace('%clientname',args.clientname)
    l8 = l7.replace('%clientstreet',clientstreet)
    l9 = l8.replace('%clientzip',clientzip)
    l10 = l9.replace('%title',args.title)
    l11 = l10.replace('%notes',args.notes)





for i in range(len(args.line)):
    split1 = args.line[i]
    newsplit = split1.split(';')
    

    print newsplit[0] + newsplit[1] + newsplit[2]
    
    


