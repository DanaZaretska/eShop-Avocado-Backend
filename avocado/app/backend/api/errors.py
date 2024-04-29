from fastapi import HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.openapi.constants import REF_PREFIX
from fastapi.openapi.utils import validation_error_response_definition
from pydantic import ValidationError
from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY
from starlette.status import HTTP_500_INTERNAL_SERVER_ERROR


async def http422_error_handler(
    _: Request, exc: RequestValidationError | ValidationError
) -> JSONResponse:
    return JSONResponse(
        {"errors": exc.errors(), "body": exc.body},
        status_code=HTTP_422_UNPROCESSABLE_ENTITY,
    )


validation_error_response_definition["properties"] = {
    "errors": {
        "title": "Errors",
        "type": "array",
        "items": {"$ref": f"{REF_PREFIX}ValidationError"},
    }
}


async def http_error_handler(_: Request, exc: HTTPException) -> JSONResponse:
    return JSONResponse({"errors": [exc.detail]}, status_code=exc.status_code)


async def global_error_handler(_: Request, exc: Exception) -> JSONResponse:
    # TODO: log exc here but never return it to the user
    return JSONResponse(
        {"errors": ["Internal Server Error"]},
        status_code=HTTP_500_INTERNAL_SERVER_ERROR,
    )
