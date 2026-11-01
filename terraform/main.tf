terraform {
  required_version = ">= 1.0"

  required_providers {
    local = {
      source  = "hashicorp/local"
      version = "~> 2.5"
    }
  }
}

provider "local" {}

resource "local_file" "test_config" {
  filename = "${path.module}/test-environment.txt"

  content = <<-EOT
  Project: JobConnect Selenium Testing
  Target URL: https://job-connect-fsd-project-jha2esm1x-kamalkumar17b-3631s-projects.vercel.app/
  Framework: Selenium
  Test Runner: Pytest
  Test Cases: 18
  EOT
}
