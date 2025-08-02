from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Math")

@mcp.tool()
def add(a: int, b:int) -> int:
    """
    Add two numbers
    """
    return  a+ b

@mcp.tool()
def multiple(a:int, b:int) -> int:
    """
    Multiply two numbers
    """
    return a*b


mcp.run(transport="stdio")
