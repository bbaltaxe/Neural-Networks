import json
from bs4 import BeautifulSoup


def main(): 

    filepath = ("/Users/breanna/Downloads/reviews_Video_Games_5.json")
    
    #open json file 
    with open(filepath,'r') as ofile: 
        review_dictionary = json.load(ofile)

    with open('reviews.txt', 'w') as cfile: 
        for review in review_dictionary['items']:
            #to filter on a parameter, swap the following two lines for the one being used now and change file name above
            #if review['overall'] == 5.0:
            #    cfile.write('\n\n'+BeautifulSoup(review['reviewText']).text+'\n')
            
            cfile.write('\n\n'+BeautifulSoup(review['reviewText']).text+'\n')
if __name__ == "__main__":
    main()
