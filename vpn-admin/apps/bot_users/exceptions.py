from rest_framework.exceptions import APIException


class BotUserNotFound(APIException):
    status_code = 404
    default_detail = "The request bot user does not exists"
