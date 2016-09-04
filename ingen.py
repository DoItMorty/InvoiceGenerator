import argparse

#Configurating argparse
parser = argparse.ArgumentParser(description='SeaSquids Invoice Generator',
    usage='ingen --client [client] --line [description,unitcost,quantity]')

parser.add_argument('--client',required='True',help='Client template to use')
parser.add_argument('--line',nargs='?',action='append',required='True',
    help='Information for lines. May specify more than once for multiple lines.')

args = parser.parse_args()
workingfile = "./" + args.client + "/template.tex"



#args.line is what is specified on the command line
for i in range(len(args.line)):
    split1 = args.line[i]
    newsplit = split1.split(';')
    print newsplit
    
    


