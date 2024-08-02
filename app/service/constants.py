X_AUTH_TOKEN_COOKIE = "X-Auth-Token"

APPSEC_PRACTICES = {
    "practice_main": {
        "description": "Main AppSec practices",
        "practices": ["SAST", "DAST", "IAST"]
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

LOGIN_FORM_HTML = """
<form action="/login" method="post">
    <label for="username">Username:</label><br>
    <input type="text" id="username" name="username"><br>
    <label for="password">Password:</label><br>
    <input type="password" id="password" name="password"><br><br>
    <input type="submit" value="Submit">
</form>
"""

LOGIN_SUCCESS_HTML = """
<html>
    <head>
        <meta http-equiv="refresh" content="2;url=/appsec?key=practice_main">
    </head>
    <body>
        <p>All correct. Redirecting to AppSec practices...</p>
    </body>
</html>
"""
