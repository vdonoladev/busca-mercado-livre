import sys
import json
import codecs
import urllib.request
import urllib.parse

def usage():
	print('Uso: {0} "PRODUTO"'.format(sys.argv[0]))
	print('Busque um produto por vez')
	sys.exit(1)

def busca(item):
	url = 'https://api.mercadolibre.com/sites/MLB/search?q={0}'.format(item)
	opener = urllib.request.build_opener()
	opener.addheaders = [
		('User-agent', "Mozilla/5.0 (Windows; U; Windows NT 6.1; rv:2.2) Gecko/20110201")]

	with opener.open(url) as fd:
		content = fd.read()
		encoding = fd.info().get_content_charset()
		content = content.decode(encoding)

	dic	= json.loads(content)

	sys.stdout = codecs.getwriter('UTF-8') (sys.stdout.detach())
	for elem in dic ['results']:
		print('{0:<70}R${1}\n{2}\n'.format(elem['title'],
										   elem['price'],
										   elem['permalink']))

if __name__ == '__main__':
	if len(sys.argv) == 1 or sys.argv[1] in {'-h', '--help'}:
		usage()

	busca(urllib.parse.quote_plus(' '.join(sys.argv[1:])))
	