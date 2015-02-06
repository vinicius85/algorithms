import facebook
import json
import io
import preprocessing as pp
	
def getData(token):
	global g
	g = facebook.GraphAPI(token)
	
def getPosts(profile, object):
	return g.get_object('/'+profile+'/posts', limit=500)
	
def main():
	profile =   'ShoppingUOL'
	token = 'CAACEdEose0cBAKmFyoNTsq1MaCLwcZAfxxuZAGTwZBHmaBG3dPW8GcFvJMnm1zNUvI1AOZB1mcYOZAy4oyNBKwRudko0S4i82ZBbRvBukbnBRC57gSzlZA5JllR7ZBNrphxNy9jiczmGPYZBpEtTjNZAZBp9NufLYdczIBmteg6a5U2mcBsb8ZBKZAdzkF20HPfSA4Br1qyApNZBKmnm9e53ZBNyqro'
	
	
	print 'GET '+profile+'/posts ...'
	
	getData(token)
	
	##Melhorar retrieval de posts em lote
	posts = getPosts(profile, 'posts')['data']
	
	print 'writing posts on file ...'
	
	f = io.open('output.log','w')
	
	i = 1
	
	for post in posts:
		if 'message' in post:
			likes = g.get_object('/'+post['id']+'/likes', summary=1)['summary']['total_count']
			line = unicode(i)+'\t'+post['message']+'\t'+pp.extractDateTime(post['created_time'])+'\t'+unicode(likes)
			
			shares = 0
			if 'shares' in post:
				shares = post['shares']['count']
			line+='\t'+unicode(shares)
			
			url = pp.extractLinkUrl(post['message'])
			if url is not None:
				line+='\t'+url
			
			if 'link' in post:
				line+='\t'+post['link']

			line+='\n'
			
			i+=1

			f.write(unicode(line))
	f.close()
	
	print 'done!'

	
	##Aplicar filtros textuais
	##Rankear posts por likes
	##Aplicar algoritmos de agrupamento e verificar se existe dentro do grupo likes similares e descobrir se existem palavras com mais like

	
if __name__ == "__main__": main()