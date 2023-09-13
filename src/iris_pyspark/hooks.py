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
        dst_lh_appn = os.environ.get('DST_LH_APPN', 'iris_naive_bayes_classification_pyspark_EDU')
        my_pod_ip = subprocess.run(['hostname', '-I'], stdout=subprocess.PIPE).stdout.decode('utf-8').strip(' \n\t')

        # Load the spark configuration in spark.yaml using the config loader
        parameters = context.config_loader["spark"]
        spark_conf = SparkConf().setAll(parameters.items())

        # Initialise the spark session
        spark_session_conf = (
            SparkSession.builder \
            .master(dst_lh_url) \
            .appName(dst_lh_appn) \
            .enableHiveSupport() \
            .config('spark.driver.host', my_pod_ip) \
            .config(conf=spark_conf)
        )
        _spark_session = spark_session_conf.getOrCreate()
        _spark_session.sparkContext.setLogLevel("WARN")
