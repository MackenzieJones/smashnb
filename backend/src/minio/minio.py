from minio import Minio
import os

MINIO_ENDPOINT = os.environ['MINIO_ENDPOINT']
MINIO_BUCKET = os.environ['MINIO_BUCKET']
MINIO_ROOT_USER = os.environ['MINIO_ROOT_USER']
MINIO_ROOT_PASSWORD = os.environ['MINIO_ROOT_PASSWORD']


class MinioClient():

	connection: Minio

	def __init__(self):
		self.client = Minio(
			MINIO_ENDPOINT,
			MINIO_ROOT_USER,
			MINIO_ROOT_PASSWORD
		)

	def get_presigned_url(self, object_path: str):
		self.connection.get_presigned_url(
			method='GET',
			bucket_name=MINIO_BUCKET,
			object_name=object_path
		)
