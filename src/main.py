import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from .ml_app.router import router
from .exceptions import BaseAPIException

app = FastAPI(debug=True)

app.include_router(router)


@app.exception_handler(BaseAPIException)
async def base_exception_handler(request: Request, exc: BaseAPIException):
    return JSONResponse(
        status_code=exc.status_code,
        content={**exc.model().dict()}
    )


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
