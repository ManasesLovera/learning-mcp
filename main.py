from __future__ import annotations

import json
import os
import random
import urllib.parse
import urllib.request
from typing import Any

from fastmcp import FastMCP


JSONPLACEHOLDER_BASE_URL = "https://jsonplaceholder.typicode.com"
DEFAULT_HOST = os.getenv("MCP_HOST", "127.0.0.1")
DEFAULT_PORT = int(os.getenv("MCP_PORT", "8000"))
DEFAULT_PATH = os.getenv("MCP_PATH", "/mcp")

mcp = FastMCP(
    name="Generic Example MCP Server",
    instructions=(
        "This server exposes five generic example tools. Each tool returns the "
        "code or HTTP request it executed so MCP clients can inspect behavior."
    ),
)


def fetch_json(path: str, query: dict[str, Any] | None = None) -> list[dict[str, Any]]:
    url = f"{JSONPLACEHOLDER_BASE_URL}{path}"
    filtered_query = {key: value for key, value in (query or {}).items() if value is not None}
    if filtered_query:
        url = f"{url}?{urllib.parse.urlencode(filtered_query)}"

    request = urllib.request.Request(
        url,
        headers={"User-Agent": "generic-example-fastmcp/0.1.0"},
    )
    with urllib.request.urlopen(request, timeout=15) as response:
        charset = response.headers.get_content_charset() or "utf-8"
        return json.loads(response.read().decode(charset))


@mcp.tool(
    name="generate_random_number",
    description=(
        "Generate a random integer between two inclusive bounds. "
        "Code executed: random.randint(min_value, max_value)."
    ),
)
def generate_random_number(min_value: int = 1, max_value: int = 100) -> dict[str, Any]:
    if min_value > max_value:
        raise ValueError("min_value must be less than or equal to max_value.")

    return {
        "tool": "generate_random_number",
        "description": "Generate a random integer between two inclusive bounds.",
        "executed_code": f"random.randint({min_value}, {max_value})",
        "result": random.randint(min_value, max_value),
    }


@mcp.tool(
    name="get_users",
    description=(
        "Fetch users from the free JSONPlaceholder API. "
        "Code executed: GET https://jsonplaceholder.typicode.com/users."
    ),
)
def get_users() -> dict[str, Any]:
    data = fetch_json("/users")
    return {
        "tool": "get_users",
        "description": "Fetch users from the JSONPlaceholder users endpoint.",
        "executed_request": f"GET {JSONPLACEHOLDER_BASE_URL}/users",
        "count": len(data),
        "data": data,
    }


@mcp.tool(
    name="get_posts",
    description=(
        "Fetch posts from the free JSONPlaceholder API with optional user filtering. "
        "Code executed: GET https://jsonplaceholder.typicode.com/posts or "
        "GET https://jsonplaceholder.typicode.com/posts?userId=<user_id>."
    ),
)
def get_posts(user_id: int | None = None) -> dict[str, Any]:
    data = fetch_json("/posts", {"userId": user_id})
    request_url = f"{JSONPLACEHOLDER_BASE_URL}/posts"
    if user_id is not None:
        request_url = f"{request_url}?userId={user_id}"

    return {
        "tool": "get_posts",
        "description": "Fetch posts from the JSONPlaceholder posts endpoint.",
        "executed_request": f"GET {request_url}",
        "count": len(data),
        "data": data,
    }


@mcp.tool(
    name="get_comments",
    description=(
        "Fetch comments from the free JSONPlaceholder API with optional post filtering. "
        "Code executed: GET https://jsonplaceholder.typicode.com/comments or "
        "GET https://jsonplaceholder.typicode.com/comments?postId=<post_id>."
    ),
)
def get_comments(post_id: int | None = None) -> dict[str, Any]:
    data = fetch_json("/comments", {"postId": post_id})
    request_url = f"{JSONPLACEHOLDER_BASE_URL}/comments"
    if post_id is not None:
        request_url = f"{request_url}?postId={post_id}"

    return {
        "tool": "get_comments",
        "description": "Fetch comments from the JSONPlaceholder comments endpoint.",
        "executed_request": f"GET {request_url}",
        "count": len(data),
        "data": data,
    }


@mcp.tool(
    name="get_todos",
    description=(
        "Fetch todos from the free JSONPlaceholder API with optional user filtering. "
        "Code executed: GET https://jsonplaceholder.typicode.com/todos or "
        "GET https://jsonplaceholder.typicode.com/todos?userId=<user_id>."
    ),
)
def get_todos(user_id: int | None = None) -> dict[str, Any]:
    data = fetch_json("/todos", {"userId": user_id})
    request_url = f"{JSONPLACEHOLDER_BASE_URL}/todos"
    if user_id is not None:
        request_url = f"{request_url}?userId={user_id}"

    return {
        "tool": "get_todos",
        "description": "Fetch todos from the JSONPlaceholder todos endpoint.",
        "executed_request": f"GET {request_url}",
        "count": len(data),
        "data": data,
    }


def main() -> None:
    mcp.run(transport="http", host=DEFAULT_HOST, port=DEFAULT_PORT, path=DEFAULT_PATH)


if __name__ == "__main__":
    main()
