#!/usr/bin/env python
from core.app import create_app
from core.conf import settings

app = create_app()


if __name__ == '__main__':
    app.run(
        host=settings.DEBUG_HOST, port=settings.DEBUG_PORT,
        debug=settings.DEBUG
    )
