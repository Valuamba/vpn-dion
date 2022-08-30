from rest_framework.exceptions import APIException


class BotUserNotFound(APIException):
    status_code = 404
    default_detail = "The request bot_feedback user does not exists"


class UserAlreadyExist(APIException):
    status_code = 404
    default_detail = "The user with this id already exists in database"