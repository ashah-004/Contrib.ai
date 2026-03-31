terraform {
    required_providers {
        google = {
            source = "hashicorp/google"
            version = "~> 5.0"
        }
    }
}

provider "google" {
    project = "project-22b2928f-3abd-44fe-9eb"
    region = "us-west2"
    zone = "us-west2-a"
}