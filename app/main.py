# app/main.py
from fastapi import FastAPI
from .routers import org_router, admin_router

app = FastAPI(title="Org Management Service")

app.include_router(org_router.router)
app.include_router(admin_router.router)

@app.get("/")
async def root():
    return {"status": "ok", "service": "Org Management Service"}
