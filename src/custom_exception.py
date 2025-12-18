import traceback #tracking error 
import sys

class CustomException(Exception):

    def __init__(self,error_message, error_detail:sys):
        super().__init__(error_message) #inheriting from Predefined Exception
        self.error_message = self.get_detailed_error_message(error_message, error_detail)

     # we don't need to create custom class again and again to show our custom error 
    @staticmethod
    def get_detailed_error_message(error_message, error_detail:sys):
        _,_,exc_tb = traceback.sys.exc_info() #we only need the traceback
        file_name = exc_tb.tb_frame.f_code.co_filename # to get the filename
        line_number = exc_tb.tb_lineno # line number 

        return f"Error in {file_name} , line {line_number} : {error_message}"
    
    #this gives a text representation to your error message
    def __str__(self):
        return self.error_message 

