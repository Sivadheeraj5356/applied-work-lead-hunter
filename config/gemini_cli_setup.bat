@echo off
REM Gemini CLI Setup Script for Applied Work Research Tools
echo ============================================================
echo Configuring Remote MCP Endpoints for Gemini CLI
echo ============================================================

echo Adding Apollo MCP Server...
gemini mcp add --transport http apollo https://mcp.apollo.io/mcp

echo Adding Tavily MCP Server...
gemini mcp add --transport http tavily https://mcp.tavily.com/mcp

echo.
echo Configuration complete! Next, launch Gemini CLI and authenticate:
echo   gemini
echo Inside Gemini prompt, run:
echo   /mcp auth apollo
echo   /mcp auth tavily
echo   /skills list
echo ============================================================
