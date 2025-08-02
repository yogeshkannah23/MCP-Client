from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Weather")

@mcp.tool()
async def get_weather(location:str) -> str:
    """ Get the weather of the location"""
    return "It's always rainy in california"



mcp.run(transport="streamable-http")