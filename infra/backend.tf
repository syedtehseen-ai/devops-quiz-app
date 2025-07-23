terraform {
  backend "s3" {
    bucket         = "tehseen-ai-tf"
    key            = "eks/infra.tfstate"
    region         = "us-east-1"
    dynamodb_table = "terraform-lock-table"
    encrypt        = true
  }
}