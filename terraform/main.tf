provider "aws" {
  region = "eu-west-1"
}

resource "aws_dynamodb_table" "cloud_resume_challenge" {
  name         = "cloud-resume-challenge"
  billing_mode = "PAY_PER_REQUEST"

  attribute {
    name = "ID"
    type = "S"
  }

  hash_key = "ID"

  tags = {
    Name = "cloud-resume-challenge"
  }
}

output "dynamodb_table_name" {
  value = aws_dynamodb_table.cloud_resume_challenge.name
}
