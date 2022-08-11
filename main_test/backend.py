from .crawler import crawl_page
from .scraper import Post

from nltk.stem.porter import PorterStemmer

from nltk.corpus import wordnet



def is_child_harassment(text):
  
  stemmer = PorterStemmer()

  syn_arr = wordnet.synsets("child")
  
  syn_child = []
  for syn in syn_arr:
    for s in syn.lemma_names():
        syn_child.append(stemmer.stem(s.lower()))

    for word in text.split(' '):
        if stemmer.stem(word.lower()) in s:
           return True

    return False 


def extracing(TAG = 'attentat'):
    url = f"https://twitter.com/hashtag/{TAG}?src=hashtag_click"

    print(f"Starting Crawling Process for topic = {TAG}")
    
    page_source = crawl_page(url)

    print("Extracing...")

    descriptions_of_post = []       
    
    for post in Post.scrape_posts(page_source):
        description = post.get_text()
        if description != "":
            print("-----------------------------------------------------------------")
            print(description)
            print("-----------------------------------------------------------------")
            if is_child_harassment(description):
                descriptions_of_post.append(description)
    
    print("Finished Successfully !")
    
    return descriptions_of_post

