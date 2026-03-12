# Generic Example FastMCP Server

This project provides a FastMCP server with 5 generic example tools. It uses HTTP transport by default.

- `generate_random_number`
- `get_users`
- `get_posts`
- `get_comments`
- `get_todos`

Each tool has a detailed name/description and returns the code or HTTP request it executed in the response payload.

## Tools

### `generate_random_number`
- Description: Generates a random integer between two inclusive bounds.
- Executed code: `random.randint(min_value, max_value)`

### `get_users`
- Description: Fetches users from JSONPlaceholder.
- Executed request: `GET https://jsonplaceholder.typicode.com/users`

### `get_posts`
- Description: Fetches posts from JSONPlaceholder, optionally filtered by `user_id`.
- Executed request:
  - `GET https://jsonplaceholder.typicode.com/posts`
  - `GET https://jsonplaceholder.typicode.com/posts?userId=<user_id>`

### `get_comments`
- Description: Fetches comments from JSONPlaceholder, optionally filtered by `post_id`.
- Executed request:
  - `GET https://jsonplaceholder.typicode.com/comments`
  - `GET https://jsonplaceholder.typicode.com/comments?postId=<post_id>`

### `get_todos`
- Description: Fetches todos from JSONPlaceholder, optionally filtered by `user_id`.
- Executed request:
  - `GET https://jsonplaceholder.typicode.com/todos`
  - `GET https://jsonplaceholder.typicode.com/todos?userId=<user_id>`

## Run

```powershell
uv sync
python main.py
```

By default, the server starts on:

- Host: `127.0.0.1`
- Port: `8000`
- MCP path: `/mcp`

You can override them with environment variables:

```powershell
$env:MCP_HOST="0.0.0.0"
$env:MCP_PORT="9000"
$env:MCP_PATH="/mcp"
python main.py
```

The entrypoint runs:

```python
mcp.run(transport="http", host=DEFAULT_HOST, port=DEFAULT_PORT, path=DEFAULT_PATH)
```

## Notes

- FastMCP generates the MCP tool schema from the Python function signatures.
- Tool descriptions are defined explicitly via `@mcp.tool(...)`.
- HTTP-backed tools call the free JSONPlaceholder API.
