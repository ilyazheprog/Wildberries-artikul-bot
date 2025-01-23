from fastapi import HTTPException, Header
from fastapi.security import HTTPBearer
from modules.envs.settings import settings

security = HTTPBearer()


def verify_token(authorization: str = Header(None)):
    """Проверяет токен из заголовка Authorization."""
    if not authorization:
        raise HTTPException(status_code=403, detail="Authorization header is missing")
    
    scheme, _, token = authorization.partition(" ")
    if scheme.lower() != "bearer" or token != settings.backend.auth_token:
        raise HTTPException(status_code=403, detail="Invalid or missing token")
    
    return True