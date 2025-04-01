# AutoGen with MCP Demo

This repository demonstrates the use of AutoGen with Model Context Protocol (MCP) to build AI-powered applications.
It provides an example setup for integrating Azure OpenAI services, AutoGen, and MCP Server into your project.

## Prerequisites

Before using this repository, ensure you have the following:

1. An Azure account with access to Azure OpenAI services.
2. The necessary API keys and endpoint details for your Azure OpenAI deployment.

## Client Setup

1. Clone this repository:

   ```bash
   git clone https://github.com/your-username/autogen-with-MCP-demo.git
   cd autogen-with-MCP-demo
   ```

2. Create a `.env` file in the root directory and configure it with your Azure OpenAI credentials:

   ```properties
   AZURE_OPENAI_DEPLOYMENT=your_deployment_name
   AZURE_OPENAI_API_KEY=your_api_key
   AZURE_OPENAI_ENDPOINT=your_endpoint_url
   AZURE_OPENAI_API_VERSION=your_api_version
   AZURE_OPENAI_MODEL=your_model_name
   ```

   Alternatively, you can use the provided `.env.template` as a reference.

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## MCP Server Setup

Please refer to the MCP Server documentation which you want to use.

If you want to use Filesystem MCP Server, please follow the instructions below:
https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem

## Usage

Run the application using the following command:

```bash
python 000.MCP.File.py
```
