import json
from bs4 import BeautifulSoup


def main(): 

    filepath = ("/Users/breanna/Downloads/reviews_Video_Games_5.json")
    
    #open json file 
    with open(filepath,'r') as ofile: 
        review_dictionary = json.load(ofile)

    with open('reviews.txt', 'w') as cfile: 
        for review in review_dictionary['items']:

            cfile.write('\n\n'+BeautifulSoup(review['reviewText']).text+'\n')
            #cfile.write('\n\n'+json.dumps(review['reviewText'].encode('ascii','ignore').decode(), indent=5)+'\n')


if __name__ == "__main__":
    main()
