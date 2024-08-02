from fastapi import Request, HTTPException, status

from app.service.constants import X_AUTH_TOKEN_COOKIE


async def get_token_or_raise_http_exc(request: Request) -> str:
    cookie_token = request.cookies.get(X_AUTH_TOKEN_COOKIE)

    if not cookie_token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authenticated. Go to /login",
        )

    return cookie_token
