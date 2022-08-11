from bs4 import BeautifulSoup

class Post(object):
    """
    Post class (model) that handles process, extracting and saving post data
    """

    COLLECTION_NAME = "posts" # the name of the collection where the data will be stored


    def __init__(self,document):
        self.document = document


    @staticmethod
    def scrape_posts(document):
        soup = BeautifulSoup(document,'html.parser')

        div_text = soup.find_all("div", {"class":["css-901oao", "r-1nao33i", "r-37j5jr", "r-a023e6", "r-16dba41", "r-rjixqe", "r-bcqeeo", "r-bnwqim", "r-qvutc0"]})                                            
        
        return div_text

