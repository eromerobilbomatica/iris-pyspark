"""
This is a boilerplate pipeline 'data_science'
generated using Kedro 0.18.13
"""

from kedro.pipeline import Pipeline, pipeline, node

from .nodes import (
    transform_data, split_data, 
    train_naive_bayes, predict_and_evaluate
)


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func = transform_data, 
                inputs = "iris_iceberg_table",
                outputs = "transformed_data",
                name="VectorAssembler",
                tags="data_science"
            ),
            node(
                func = split_data, 
                inputs = "transformed_data",
                outputs = ["train_data", "test_data"],
                name="split_data",
                tags="data_science"
            ),
            node(
                func = train_naive_bayes, 
                inputs = "train_data",
                outputs = "naiveBayes_model",
                name="train_naive_bayes",
                tags="data_science"
            ),
            node(
                func = predict_and_evaluate, 
                inputs = ["naiveBayes_model", "test_data"],
                outputs = "evaluation_results",
                name="predict_and_evaluate",
                tags="data_science"
            ),
        ]
    )
