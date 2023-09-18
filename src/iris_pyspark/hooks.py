from kedro.framework.hooks import hook_impl
from pyspark import SparkConf
from pyspark.sql import SparkSession
import os
import subprocess

class SparkHooks:
    @hook_impl
    def after_context_created(self, context) -> None:
        """Initialises a SparkSession using the config
        defined in project's conf folder.
        """

        dst_lh_url  = os.environ.get('DST_LH_URL', 'spark://spark-master-0.spark-headless.demml.svc.cluster.local:7077')
        dst_lh_appn = os.environ.get('DST_LH_APPN', 'conexion_pyspark_iceberg_edu')
        my_pod_ip = subprocess.run(['hostname', '-I'], stdout=subprocess.PIPE).stdout.decode('utf-8').strip(' \n\t')

        spark = SparkSession.builder \
            .master(dst_lh_url) \
            .appName(dst_lh_appn) \
            .config('spark.jars.packages','org.apache.iceberg:iceberg-spark-runtime-3.3_2.12:1.1.0,org.mariadb.jdbc:mariadb-java-client:2.3.0,org.postgresql:postgresql:42.5.4,software.amazon.awssdk:bundle:2.17.257,software.amazon.awssdk:url-connection-client:2.17.257,software.amazon.awssdk:s3:2.17.257,software.amazon.awssdk:iam:2.17.257,org.apache.hadoop:hadoop-aws:3.2.3') \
            .config('spark.driver.host', my_pod_ip) \
            .config('spark.sql.extensions','org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions') \
            .config('spark.sql.catalog.spark_catalog','org.apache.iceberg.spark.SparkSessionCatalog') \
            .config('spark.sql.catalog.spark_catalog.catalog-impl','org.apache.iceberg.jdbc.JdbcCatalog') \
            .config('spark.sql.catalog.spark_catalog.uri','jdbc:postgresql://postgresql:5432/iceberg') \
            .config('spark.sql.catalog.spark_catalog.jdbc.useSSL','false') \
            .config('spark.sql.catalog.spark_catalog.jdbc.user','iceberg') \
            .config('spark.sql.catalog.spark_catalog.jdbc.password','iceberg') \
            .config('spark.sql.catalog.spark_catalog.warehouse','s3a://warehouse/') \
            .config('spark.sql.catalog.spark_catalog.s3.endpoint','http://minio:9000') \
            .config('spark.sql.catalog.spark_catalog.io-impl', 'org.apache.iceberg.aws.s3.S3FileIO') \
            .config('spark.sql.defaultCatalog','spark_catalog') \
            .config('spark.hadoop.fs.s3a.endpoint','http://minio:9000') \
            .config('spark.hadoop.fs.s3a.access.key','admin') \
            .config('spark.hadoop.fs.s3a.secret.key','t4bl4red0nd4') \
            .config('spark.hadoop.fs.s3a.path.style.access','true') \
            .config('spark.hadoop.fs.s3a.impl','org.apache.hadoop.fs.s3a.S3AFileSystem') \
            .config("spark.hadoop.fs.s3a.connection.ssl.enabled", "false") \
            .config("spark.hadoop.fs.s3a.aws.credentials.provider", "org.apache.hadoop.fs.s3a.SimpleAWSCredentialsProvider") \
            .getOrCreate()
        spark.sparkContext.setLogLevel("WARN")
