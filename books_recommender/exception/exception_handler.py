import os
import sys


class AppException(Exception):
    """
    Organization: iNeuron Intelligence Private Limited

    AppException is a customized exception class designed to capture
    detailed information about exceptions such as:
    - Python script file name
    - Line number where error occurred
    - Original error message

    This helps in faster debugging and production-level error handling.
    """

    def __init__(self, error_message: Exception, error_detail: sys):
        """
        :param error_message: Exception message
        :param error_detail: sys module (for traceback info)
        """
        super().__init__(error_message)

        # store detailed error message
        self.error_message = AppException.error_message_detail(
            error_message, error_detail=error_detail
        )

    @staticmethod
    def error_message_detail(error: Exception, error_detail: sys):
        """
        Extracts detailed error message from traceback

        :param error: Exception object raised
        :param error_detail: sys module (contains execution info)
        :return: formatted error message
        """
        _, _, exc_tb = error_detail.exc_info()

        # File name where exception occurred
        file_name = exc_tb.tb_frame.f_code.co_filename

        # Line number of error
        line_number = exc_tb.tb_lineno

        # Final formatted error message
        error_message = (
            f"\nError occurred in python script: [{file_name}]"
            f"\nLine number: [{line_number}]"
            f"\nError message: [{str(error)}]\n"
        )

        return error_message

    def __repr__(self):
        """
        Representation of the object (developer-friendly)
        """
        return f"{self.__class__.__name__}({self.error_message})"

    def __str__(self):
        """
        String representation (user-friendly)
        """
        return self.error_message