from fastapi import APIRouter, Request, HTTPException
from fastapi.responses import RedirectResponse, JSONResponse
from authlib.integrations.starlette_client import OAuth

from app.core.config import settings

router = APIRouter(prefix="/auth", tags=["auth"])
oauth = OAuth()

oauth.register(
    name="google",
    client_id=settings.GOOGLE_CLIENT_ID,
    client_secret=settings.GOOGLE_CLIENT_SECRET,
    server_metadata_url="https://accounts.google.com/.well-known/openid-configuration",
    client_kwargs={"scope": "openid email profile"},
)


@router.get("/google/login")
async def google_login(request: Request):
    redirect_uri = settings.GOOGLE_REDIRECT_URI
    return await oauth.google.authorize_redirect(request, redirect_uri)


@router.get("/google/callback")
async def google_callback(request: Request):

    token = await oauth.google.authorize_access_token(request)

    user = token.get("userinfo") or await oauth.google.parse_id_token(request, token)

    request.session["user"] = {
        "email": user["email"],
        "name": user.get("name"),
        "picture": user.get("picture"),
        "sub": user.get("sub"),
    }

    return RedirectResponse(url=settings.FRONTEND_URL)


@router.get("/me")
async def me(request: Request):
    user = request.session.get("user")
    if not user:
        return JSONResponse({"user": None}, status_code=401)
    return {"user": user}


@router.post("/logout")
async def logout(request: Request):
    request.session.clear()
    return {"message": "logged out"}
