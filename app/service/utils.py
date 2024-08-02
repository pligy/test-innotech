import hashlib


def generate_token(username: str, password: str) -> str:
    to_hash = f"{username}:{password}".encode()
    return hashlib.sha256(to_hash).hexdigest()
