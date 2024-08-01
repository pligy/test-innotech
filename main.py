from fastapi import FastAPI, Form, Request, Depends, HTTPException, status
from fastapi.responses import RedirectResponse, HTMLResponse, JSONResponse
import hashlib

app = FastAPI()

appsec_practices = {
    "practice_main": {
        "description": "Main AppSec practices",
        "practices": ["SAST", "DAST", "Threat Modeling"]
    },
    "practice_sast": {
        "description": "Static Application Security Testing",
        "details": "Analyzes source code or binaries for security vulnerabilities without executing the program."
    },
    "practice_dast": {
        "description": "Dynamic Application Security Testing",
        "details": "Examines a running application to find security vulnerabilities by simulating external attacks."
    },
    "practice_iast": {
        "description": "Interactive Application Security Testing",
        "details": "Combines aspects of both SAST and DAST by analyzing applications in real-time while they are running and interacting with the code and environment."
    },
}

X_AUTH_TOKEN_COOKIE = "X-Auth-Token"

# Function to generate a hashed token
def generate_token(username: str, password: str) -> str:
    to_hash = f"{username}:{password}".encode()
    return hashlib.sha256(to_hash).hexdigest()

async def get_token_or_raise_http_exc(
    request: Request
) -> str:
    cookie_token = request.cookies.get(X_AUTH_TOKEN_COOKIE)
    if cookie_token:
        return cookie_token
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Not authenticated. Go to /login",
    )

@app.get("/", response_class=RedirectResponse)
async def root():
    return RedirectResponse(url="/login")

@app.get("/login", response_class=HTMLResponse)
async def login_form():
    return """
    <form action="/login" method="post">
        <label for="username">Username:</label><br>
        <input type="text" id="username" name="username"><br>
        <label for="password">Password:</label><br>
        <input type="password" id="password" name="password"><br><br>
        <input type="submit" value="Submit">
    </form>
    """

@app.post("/login", response_class=HTMLResponse)
async def login(request: Request, username: str = Form(...), password: str = Form(...)):
    if username == "admin" and password == "admin":
        token = generate_token(username, password)
        response_content = """
        <html>
            <head>
                <meta http-equiv="refresh" content="2;url=/appsec?key=practice_main">
            </head>
            <body>
                <p>All correct. Redirecting to AppSec practices...</p>
            </body>
        </html>
        """
        response = HTMLResponse(content=response_content)
        response.set_cookie(
            X_AUTH_TOKEN_COOKIE,
            value=token,
            httponly=True,
            max_age=86400,  # 1 day
            expires=86400,
        )
        return response
    else:
        return "Incorrect"

@app.get("/appsec", response_class=JSONResponse)
async def appsec(key: str, token: str = Depends(get_token_or_raise_http_exc)):
    if key in appsec_practices:
        return appsec_practices[key]
    else:
        return {"error": "Key not found"}
