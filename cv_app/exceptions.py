import logging
from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status

# Get the 'custom' logger from the LOGGING configuration
logger = logging.getLogger('django.request')

def custom_exception_handler(exc, context):
    # Call DRF's default exception handler
    response = exception_handler(exc, context)

    # Log exceptions
    logger.error(f"Exception occurred: {str(exc)}", exc_info=True, extra={"context": context})

    if response is not None:
        custom_data = {
            "error": True,
            "message": response.data.get('detail', str(exc)) if 'detail' in response.data else response.data,
            "status_code": response.status_code,
        }
        return Response(custom_data, status=response.status_code)

    # Handle non-DRF exceptions
    return Response(
        {
            "error": True,
            "message": "An unexpected error occurred.",
            "status_code": status.HTTP_500_INTERNAL_SERVER_ERROR,
        },
        status=status.HTTP_500_INTERNAL_SERVER_ERROR
    )