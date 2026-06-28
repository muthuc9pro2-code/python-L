import logging
import log_config

def divide(a, b):
    logging.info(f"Dividing {a} by {b}")
    try:
        result = a / b
        logging.debug(f"result: {result}")
        return result
    
    except ZeroDivisionError:
        logging.error("Tried to divide by zero!")
        return None
    
divide(10, 2)
divide(10, 0)