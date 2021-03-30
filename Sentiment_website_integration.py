import pandas as pd
import re
import sys
import sklearn


def sentiment_analysis_both(category1, category2):
    if category2 in ['Electronics', 'Home', 'Books', 'Sports']:
        return 'Flipkart'
    elif category2 in ['Apparel']:
        return 'Amazon'
    return 'Amazon'


def run_sentiment_analysis(product_name):
    print(product_name)
    product_name = product_name.lower()
    amazon_reviews = pd.read_csv('amazon_reviews.csv')
    relevant_columns = ['RATING', 'PRODUCT_CATEGORY',
       'PRODUCT_TITLE', 'REVIEW_TITLE', 'REVIEW_TEXT']
    amazon_reviews = amazon_reviews[relevant_columns]
    flipkart_reviews = pd.read_csv('Flipkart_reviews.csv')
    
    print("running")
    
    if (amazon_reviews['PRODUCT_TITLE'].str.lower().str.contains(product_name).any()) and (flipkart_reviews['PRODUCT_TITLE'].str.lower().str.contains(product_name).any()):
        print("1")
        category1 = amazon_reviews[amazon_reviews['PRODUCT_TITLE'].str.lower().str.contains(product_name)]['PRODUCT_CATEGORY'].iloc[0]
        print(category1)
        
        category2 = flipkart_reviews[flipkart_reviews['PRODUCT_TITLE'].str.lower().str.contains(product_name)]['PRODUCT_CATEGORY'].iloc[0]
        print(category2)
        
        return sentiment_analysis_both(category1, category2)
    elif (amazon_reviews['PRODUCT_TITLE'].str.lower().str.contains(product_name).any()) and (flipkart_reviews['PRODUCT_TITLE'].str.lower().str.contains(product_name).any()):
        print("2")
        return 'Amazon'
    elif (not amazon_reviews['PRODUCT_TITLE'].str.lower().str.contains(product_name).any()) and (flipkart_reviews['PRODUCT_TITLE'].str.lower().str.contains(product_name).any()):
        print("3")
        return 'Flipkart'
    else:
        print("4")
        return 'Amazon'

    return 'Amazon'



if __name__ == '__main__':
    product_name = sys.argv[1]
    run_sentiment_analysis(product_name)
