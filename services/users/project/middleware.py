import logging
import time

from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request

logger = logging.getLogger(__name__)


class TimingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start_time = time.perf_counter()
        response = await call_next(request)
        process_time = time.perf_counter() - start_time
        response.headers["X-Process-Time"] = f"{process_time:.4f}"

        if process_time > 0.5:
            logger.warning(
                f"Slow request: {request.method} {request.url.path} "
                f"took {process_time:.4f}s"
            )
        else:
            logger.info(
                f"{request.method} {request.url.path} completed in {process_time:.4f}s"
            )

        return response
