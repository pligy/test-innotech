from fastapi import APIRouter, Request, Form, Depends, HTTPException, status
from fastapi.responses import RedirectResponse, HTMLResponse, JSONResponse

from app.models.appsec import AppSecModelIn
from app.api.dependencies import get_token_or_raise_http_exc
from app.service.utils import generate_token
from app.service.constants import X_AUTH_TOKEN_COOKIE, APPSEC_PRACTICES, LOGIN_FORM_HTML, LOGIN_SUCCESS_HTML
from app.models.config import settings

router = APIRouter()

@router.get("/", response_class=RedirectResponse)
async def root():
    return RedirectResponse(url="/login")


@router.get("/login", response_class=HTMLResponse)
async def login_form():
    return LOGIN_FORM_HTML


@router.post("/login", response_class=HTMLResponse)
async def login(request: Request, username: str = Form(...), password: str = Form(...)):
    if username == settings.admin_username and password == settings.admin_password:
        token = generate_token(username, password)
        response = HTMLResponse(content=LOGIN_SUCCESS_HTML)
        response.set_cookie(
            X_AUTH_TOKEN_COOKIE,
            value=token,
            httponly=True,
            max_age=86400,  # 1 day
            expires=86400,
        )
        return response
    else:
        raise HTTPException(status_code=401, detail="Incorrect username or password")


@router.get("/appsec", response_class=JSONResponse)
async def appsec(model_in: AppSecModelIn = Depends(), _token: str = Depends(get_token_or_raise_http_exc)):
    key = model_in.key
    return APPSEC_PRACTICES[key]
