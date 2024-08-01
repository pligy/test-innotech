from fastapi import FastAPI, Form, Request
from fastapi.responses import RedirectResponse, HTMLResponse, JSONResponse
from typing import Dict

app = FastAPI()

appsec_practices = {
    "practice_main": {
        "description": "Main AppSec practices",
        "practices": ["SAST", "DAST", "Threat Modeling"]
    },
    "practice_sast": {
        "description": "Static Application Security Testing",
        "details": "Analysis of source code for security vulnerabilities."
    },
}

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
async def login(username: str = Form(...), password: str = Form(...)):
    if username == "admin" and password == "admin":
        # return "All correct"
        return RedirectResponse(url="/appsec?key=practice_main")
    else:
        return "Incorrect"

@app.get("/appsec", response_class=JSONResponse)
async def appsec(key: str):
    if key in appsec_practices:
        return appsec_practices[key]
    else:
        return {"error": "Key not found"}
