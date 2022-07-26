from flask import Flask
import sys
from creditcard.logger import logging
from creditcard.exception import CreditcardException
app=Flask(__name__)

@app.route("/",methods=['GET','POST'])
def index():
    try:
        raise Exception("We are testing custom exception")
    except Exception as e:
        ##raise CreditcardException(e,sys) from e
        creditcard = CreditcardException(e,sys)
        logging.info(creditcard.error_message)    
        logging.info("We are testing logging module")
    return "CI CD pipeline has been established."

if __name__=="__main__":
    app.run(debug=True)    
    