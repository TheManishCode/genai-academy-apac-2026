import logging
from dataclasses import dataclass

from backend.app.core.config import settings

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class BigQueryJob:
    sql: str
    dataset: str
    dry_run: bool = True


class BigQueryClient:
    def query(self, sql: str) -> BigQueryJob:
        logger.info("Prepared BigQuery query for dataset=%s", settings.bigquery_dataset)
        return BigQueryJob(sql=sql, dataset=settings.bigquery_dataset)


class CloudStorageClient:
    def signed_upload_target(self, object_name: str) -> str:
        logger.info("Generated placeholder upload target for bucket=%s", settings.gcs_bucket)
        return f"gs://{settings.gcs_bucket}/{object_name}"


class VertexAIClient:
    def model_name(self) -> str:
        return f"projects/{settings.google_cloud_project}/locations/{settings.google_cloud_location}/publishers/google/models/{settings.vertex_model}"
