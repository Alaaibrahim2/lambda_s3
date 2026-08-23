# lambda_s3

This repository contains the Lambda source code for the S3-triggered file processing workflow.

Important:
- Terraform HCL files and Terraform state files are intentionally excluded from GitHub.
- The project uses `.gitignore` to keep local infrastructure files such as `.terraform/`, `*.tf`, `*.tfstate`, and related artifacts out of the remote repository.

The Lambda function reads objects from an S3 bucket, converts their content to lowercase, and writes the transformed result to the corresponding `output/` path.