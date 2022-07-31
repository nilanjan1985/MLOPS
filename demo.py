from sklearn.pipeline import Pipeline
from creditcard.pipeline.pipeline import Pipeline
from creditcard.exception import CreditcardException
from creditcard.logger import logging

def main():
    try:
        pipeline=Pipeline()
        pipeline.run_pipeline()
    except Exception as e:
        logging.error(f"{e}")
        print(e) 

if __name__=="__main__":
    main()           

    

