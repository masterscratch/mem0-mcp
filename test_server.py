#!/usr/bin/env python3
"""
Test script to demonstrate Mem0 MCP server capabilities.
"""

import os
import json
from mem0_mcp_server.server import create_server

def test_mem0_server():
    """Test the Mem0 MCP server tools."""
    
    # Set a test API key (this will fail but shows the server structure)
    os.environ['MEM0_API_KEY'] = 'test-key-for-demo'
    
    # Create the server
    server = create_server()
    print("Mem0 MCP server created successfully")
    
    # Show the server object
    print(f"Server type: {type(server)}")
    print(f"Server name: {server.name}")
    
    print("\nMem0 MCP server is ready to use!")
    print("To use the server, you need a valid MEM0_API_KEY environment variable.")

if __name__ == "__main__":
    test_mem0_server()