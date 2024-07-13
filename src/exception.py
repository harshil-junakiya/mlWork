import sys
import logging

def error_message_detail(err, err_desc:sys):
    _, _, exec_tb = err_desc.exc_info()
    file_name = exec_tb.tb_frame.f_code.co_filename
    err_msg = "Error Occured in python script name [{0}] line no. [{1}] error message [{2}]".format(
        file_name, exec_tb.tb_lineno, str(err)
    )
    return err_msg

    

class CustomException(Exception):
    def __init__(self, err_msg, err_desc:sys):
        super().__init__(err_msg)
        self.err_msg = error_message_detail(err_msg, err_desc=err_desc)
        
    def __str__(self):
        return self.err_msg
    
