import argparse

parser = argparse.ArgumentParser()
parser.add_argument('name',type=str,help='name to display')
parser.add_argument('-l','--language',default='en',choices=['en','ru','es'])

args = parser.parse_args()

if args.language == 'en':
    print(f'hello {args.name}')
elif args.language == 'ru':
    print(f'привет {args.name}')
else:
    print(f'hola {args.name}')


