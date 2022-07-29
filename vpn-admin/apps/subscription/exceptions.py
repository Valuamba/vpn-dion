from rest_framework.exceptions import APIException


class InstanceNotFound(APIException):
    status_code = 404
    default_detail = "The request instance does not exists"