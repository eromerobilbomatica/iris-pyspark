"""
This is a boilerplate pipeline 'data_science'
generated using Kedro 0.18.13
"""

from pyspark.ml.classification import NaiveBayes
from pyspark.ml.evaluation import MulticlassClassificationEvaluator
from pyspark.ml.feature import VectorAssembler
from pyspark.sql import DataFrame
from typing import Tuple, Dict

def transform_data(iris: DataFrame) -> DataFrame:
    """
    En este nodo, realiza la transformación de datos 
    utilizando VectorAssembler.
    """

    feature_assembler = VectorAssembler(
        inputCols=['sepal_length', 'sepal_width', 'petal_length', 'petal_width'],
        outputCol='Features'
    )
    output = feature_assembler.transform(iris)

    return output.select('Features', 'target')


def split_data(transformed_data: DataFrame) -> Tuple[DataFrame, DataFrame]:
    """
    En este nodo, divide los datos en conjuntos de entrenamiento y prueba.
    """

    train_data, test_data = transformed_data.randomSplit([0.8, 0.2])

    return train_data, test_data


def train_naive_bayes(train_data: DataFrame) -> NaiveBayes:
    """
    En este nodo, ajusta el modelo Naive Bayes a los datos de entrenamiento.
    """

    nb = NaiveBayes(featuresCol='Features', labelCol='target')
    nb_model = nb.fit(train_data)

    return nb_model

def predict_and_evaluate(nb_model: NaiveBayes, test_data) -> Dict:
    """
    En este nodo, realiza la predicción en el conjunto de prueba y calcula métricas de evaluación.
    """

    y_pred = nb_model.transform(test_data)

    evaluator = MulticlassClassificationEvaluator(
        labelCol='target', predictionCol='prediction'
    )

    accuracy = evaluator.evaluate(y_pred)
    precision = evaluator.evaluate(y_pred, {evaluator.metricName: 'weightedPrecision'})
    recall = evaluator.evaluate(y_pred, {evaluator.metricName: 'weightedRecall'})
    f1_score = evaluator.evaluate(y_pred, {evaluator.metricName: 'f1'})

    print("- Accuracy: ", accuracy)
    print("- Precision: ", precision)
    print("- Recall: ", recall)
    print("- F1 score: ", f1_score)

    return {
        "accuracy": accuracy,
        "precision": precision,
        "recall": recall,
        "f1_score": f1_score,
    }
