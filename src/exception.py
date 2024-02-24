# Import the sys module for accessing system related information 
import sys
from src.logger import logging



# Define/create a function called error_message_detail that takes two arguments error; which represents the error message and 
# 'error_detail' which is the object that contains detailed information about the error
def error_message_detail(error_message, error_details_object: sys):
    # Unpack the 'error_detail' into three variables _,_,exc_tb
    #the '_' is used to ignore the first two variables while 'exc_tb' contains the required information about the traceback 
    _, _, exc_tb = error_details_object.exc_info()
    # Extract the name of the file where the error occured from the traceback 
    file_name = exc_tb.tb_frame.f_code.co_filename 
    # Create an error message string which contains information about the exception ie filename, line number, and error message
    error_message = f"Error in script [{file_name}] on line [{exc_tb.tb_lineno}]: {error_message}"

    # Return the error message
    return error_message

# Define/create a custom exception class called CustomException, which inherits from the built-in Exception class 
class FileOperationError(Exception):
    # Define the constructor for the CustomException class
    # It takes two arguments: 'error_message', which is the error message and the 'error_message_detail' which is an object containing detailed 
    # information about the error.
    def __init__(self, error_message, error_message_detail: sys):
        # Call the constructor of the built-in Exception class with `error_message_argument`
        super().__init__(error_message)
        # Assign the error message to the 'error_message' attribute of the CustomException class
        self.error_message = error_message
        # Assign the error message to the 'error_message_detail' attribute of the CustomException class
        self.error_message_detail = error_message_detail

    # Define the __str__ method for the CustomException class
    # This method is called when exception is converted to a string
    def __str__(self):
        # Return the error message
        return self.error_message
    
# Try the exception if it will work
if __name__ == "__main__":
    try:
        a = 1/0
    except Exception as e:
        logging.info("Divide by zero error occurred")
        raise FileOperationError(e, sys)




