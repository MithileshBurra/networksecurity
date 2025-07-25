import sys 
from networksecurity.logging import logger

class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        self.error_message = error_message
        _,_,exc_tb = error_detail.exc_info()
        self.lineno = exc_tb.tb_lineno
        self.filename = exc_tb.tb_frame.f_code.co_filename 
    def __str__(self):
        retrun "Error occured at filename {0} line no{} Error Message {3}".format(
            self.filename, self.lineno, str(self.error_message)
        )



     
