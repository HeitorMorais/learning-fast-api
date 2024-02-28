from fastapi import FastAPI, HTTPException, Request
from starlette.datastructures import Headers, QueryParams
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/web", StaticFiles(directory="public"), name="web")
@app.get("/web")
async def root():
    return FileResponse('public/index.html')

@app.get("/info")
async def request_info(request: Request):
    headers = request.headers
    query_params = request.query_params
    headers_dict = dict(headers)
    query_params_dict = dict(query_params)

    return {
        "headers": headers_dict,
        "query_params": query_params_dict
    }

@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    if exc.status_code == 404:
        return FileResponse('public/index.html')
    else:
            raise exc

