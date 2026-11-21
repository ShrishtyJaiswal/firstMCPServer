from fastmcp import FastMCP

mcp = FastMCP("Enterprise MCP Server")

from .github.tools import *

if __name__ == "__main__":
    mcp.run()