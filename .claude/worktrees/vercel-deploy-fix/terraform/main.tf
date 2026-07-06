terraform {
  required_version = ">= 1.6.0"
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "~> 6.0"
    }
  }
}

provider "google" {
  project = var.project_id
  region  = var.region
}

resource "google_storage_bucket" "raw_data" {
  name                        = "${var.project_id}-ecomind-raw"
  location                    = var.region
  uniform_bucket_level_access = true
}

resource "google_bigquery_dataset" "ecomind" {
  dataset_id = "ecomind"
  location   = "US"
}
