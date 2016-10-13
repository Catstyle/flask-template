from .const import messages


def make_response(data=None, status=10000):
    return {
        "code": status,
        "data": data,
        "msg": messages.get(status)
    }
