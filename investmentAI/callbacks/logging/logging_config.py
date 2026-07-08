import json
import logging
import time
import uuid
from datetime import datetime

logger = logging.getLogger("adk_logger")
logger.setLevel(logging.INFO)

# Configure Console Logging
if not logger.handlers:
    handler = logging.StreamHandler()
    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s"
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)


class ExecutionLogger:

    def __init__(self):
        self.request_start = {}

  
    # Before Agent
    async def before_agent_callback(self, callback_context):

        request_id = str(uuid.uuid4())

        self.request_start[request_id] = time.perf_counter()

        callback_context.state["request_id"] = request_id

        log = {
            "event": "AGENT_STARTED",
            "timestamp": datetime.utcnow().isoformat(),
            "request_id": request_id,
            "agent_name": callback_context.agent_name,
            "session_id": callback_context.state.get("session_id"),
        }

        logger.info(json.dumps(log))

        return None

    # After Agent
    async def after_agent_callback(self, callback_context):

        request_id = callback_context.state.get("request_id")

        start = self.request_start.get(request_id)

        latency = None

        if start:
            latency = round(
                time.perf_counter() - start,
                3
            )

        log = {
            "event": "AGENT_COMPLETED",
            "timestamp": datetime.utcnow().isoformat(),
            "request_id": request_id,
            "agent_name": callback_context.agent_name,
            "session_id": callback_context.state.get("session_id"),
            "latency_seconds": latency,
        }

        logger.info(json.dumps(log))

        return None

    # Before Model
    async def before_model_callback(
        self,
        callback_context,
        llm_request,
    ):

        log = {
            "event": "MODEL_REQUEST",
            "timestamp": datetime.utcnow().isoformat(),
            "agent_name": callback_context.agent_name,
            "model": callback_context.model,
        }

        logger.info(json.dumps(log))

        return None

    # After Model
    async def after_model_callback(
        self,
        callback_context,
        llm_response,
    ):

        usage = getattr(
            llm_response,
            "usage_metadata",
            None,
        )

        log = {
            "event": "MODEL_RESPONSE",
            "timestamp": datetime.utcnow().isoformat(),
            "agent_name": callback_context.agent_name,
            "prompt_tokens":
                getattr(usage, "prompt_token_count", None),
            "completion_tokens":
                getattr(usage, "candidates_token_count", None),
            "total_tokens":
                getattr(usage, "total_token_count", None),
        }

        logger.info(json.dumps(log))

        return None

    # Before Tool
    async def before_tool_callback(
        self,
        tool,
        args,
        tool_context,
    ):

        log = {
            "event": "TOOL_STARTED",
            "timestamp": datetime.utcnow().isoformat(),
            "tool_name": tool.name,
            "arguments": args,
        }

        logger.info(json.dumps(log))

        return None

    # After Tool
    async def after_tool_callback(
        self,
        tool,
        args,
        tool_context,
        tool_response,
    ):

        log = {
            "event": "TOOL_COMPLETED",
            "timestamp": datetime.utcnow().isoformat(),
            "tool_name": tool.name,
            "response": str(tool_response),
        }

        logger.info(json.dumps(log))

        return None

    # Error Callback
    async def on_error_callback(
        self,
        callback_context,
        error,
    ):

        log = {
            "event": "ERROR",
            "timestamp": datetime.utcnow().isoformat(),
            "agent_name": callback_context.agent_name,
            "error": str(error),
        }

        logger.error(json.dumps(log))

        return None