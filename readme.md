# Lambda MCP Agent

This project deploys an AWS Lambda function that uses the [Strands Agent Framework](https://strandsagents.com) and MCP tools to fetch weather information dynamically.

## 🚀 Features

- Uses `strands` and `mcp` to run tools like `weather.py`
- Deployable via GitHub Actions
- Automatically uploads large packages to S3
- AWS Lambda compatible (Python 3.11)

## 🧾 Requirements

- AWS Lambda function pre-created
- IAM user with access to:
  - `lambda:UpdateFunctionCode`
  - `s3:PutObject`, `s3:GetObject`
- GitHub secrets:
  - `AWS_ACCESS_KEY_ID`
  - `AWS_SECRET_ACCESS_KEY`

## 🛠️ Setup

```bash
git clone https://github.com/your-username/lambda-mcp-agent.git
cd lambda-mcp-agent
