import yaml
from creditcard.exception import CreditcardException
import os,sys

def read_yaml_file(file_path:str) -> dict:
    '''
    Reads a yaml file and returns the contents
    file _path: str
    '''
    try:
        with open(file_path,'rb') as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise CreditcardException(e,sys) from e        