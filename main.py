
from fastmcp import FastMCP
import math


# --------------------------------------------------
# 1. MCP Server Configuration
# --------------------------------------------------

mcp = FastMCP("Arithmetic Server")


# --------------------------------------------------
# 2. Number Validation
# --------------------------------------------------

def _as_number(value):

    try:
        return float(value)

    except (ValueError, TypeError):
        raise ValueError(
            "Expected a number (int/float or numeric string)"
        )


# --------------------------------------------------
# 3. Arithmetic Tools
# --------------------------------------------------

@mcp.tool()
async def add(a: float, b: float):

    return a + b


@mcp.tool()
async def subtract(a: float, b: float):

    return a - b


@mcp.tool()
async def multiply(a: float, b: float):

    return a * b


@mcp.tool()
async def divide(a: float, b: float):

    if b == 0:
        return "Error: Division by zero"

    return a / b


@mcp.tool()
async def power(a: float, b: float):

    return a ** b


@mcp.tool()
async def sqrt(a: float):

    if a < 0:
        return "Error: Cannot compute square root of a negative number"

    return a ** 0.5


@mcp.tool()
async def log(a: float, base: float = 10):

    if a <= 0:
        return "Error: Logarithm undefined for non-positive values"

    if base <= 0 or base == 1:
        return "Error: Logarithm base must be positive and not equal to 1"

    return math.log(a, base)


# --------------------------------------------------
# 4. Start MCP Server
# --------------------------------------------------

if __name__ == "__main__":

    mcp.run()
