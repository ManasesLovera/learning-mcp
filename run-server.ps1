$env:MCP_HOST = "127.0.0.1"
$env:MCP_PORT = "8001"
$env:MCP_PATH = "/mcp"

Set-Location "C:\Users\manas\Desktop\personal\mcp"
uv run python main.py
