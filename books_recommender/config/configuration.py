import os
import sys

from books_recommender.utils.util import read_yaml_file
from books_recommender.exception.exception_handler import AppException
from books_recommender.constant import CONFIG_FILE_PATH
from books_recommender.entity.config_entity import (
    DataIngestionConfig,
    DataValidationConfig,
    DataTransformationConfig,
    ModelTrainerConfig,
    ModelRecommendationConfig
)


class AppConfiguration:

    def __init__(self, config_file_path=CONFIG_FILE_PATH):
        try:
            self.configs_info = read_yaml_file(config_file_path)
        except Exception as e:
            raise AppException(e, sys)

    # 🔹 ARTIFACTS DIR
    def get_artifacts_dir(self):
        artifacts_dir = self.configs_info["artifacts_config"]["artifacts_dir"]
        os.makedirs(artifacts_dir, exist_ok=True)
        return artifacts_dir

    # 🔹 DATA INGESTION
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        try:
            config = self.configs_info["data_ingestion_config"]
            artifacts_dir = self.get_artifacts_dir()

            raw_data_dir = os.path.join(artifacts_dir, config["dataset_dir"], config["raw_data_dir"])
            ingested_dir = os.path.join(artifacts_dir, config["dataset_dir"], config["ingested_dir"])

            os.makedirs(raw_data_dir, exist_ok=True)
            os.makedirs(ingested_dir, exist_ok=True)

            return DataIngestionConfig(
                dataset_download_url=config["dataset_download_url"],
                raw_data_dir=raw_data_dir,
                ingested_dir=ingested_dir
            )

        except Exception as e:
            raise AppException(e, sys)

    # 🔹 DATA VALIDATION
    def get_data_validation_config(self) -> DataValidationConfig:
        try:
            config = self.configs_info["data_validation_config"]
            ingestion_config = self.configs_info["data_ingestion_config"]
            artifacts_dir = self.get_artifacts_dir()

            dataset_dir = ingestion_config["dataset_dir"]

            books_path = os.path.join(
                artifacts_dir, dataset_dir, ingestion_config["ingested_dir"], config["books_csv_file"]
            )

            ratings_path = os.path.join(
                artifacts_dir, dataset_dir, ingestion_config["ingested_dir"], config["ratings_csv_file"]
            )

            clean_data_dir = os.path.join(
                artifacts_dir, dataset_dir, config["clean_data_dir"]
            )

            serialized_dir = os.path.join(
                artifacts_dir, config["serialized_objects_dir"]
            )

            os.makedirs(clean_data_dir, exist_ok=True)
            os.makedirs(serialized_dir, exist_ok=True)

            return DataValidationConfig(
                clean_data_dir=clean_data_dir,
                books_csv_file=books_path,
                ratings_csv_file=ratings_path,
                serialized_objects_dir=serialized_dir
            )

        except Exception as e:
            raise AppException(e, sys)

    # 🔹 DATA TRANSFORMATION
    def get_data_transformation_config(self) -> DataTransformationConfig:
        try:
            config = self.configs_info["data_transformation_config"]
            validation_config = self.configs_info["data_validation_config"]
            ingestion_config = self.configs_info["data_ingestion_config"]

            artifacts_dir = self.get_artifacts_dir()
            dataset_dir = ingestion_config["dataset_dir"]

            clean_file = os.path.join(
                artifacts_dir, dataset_dir, validation_config["clean_data_dir"], "clean_data.csv"
            )

            transformed_dir = os.path.join(
                artifacts_dir, dataset_dir, config["transformed_data_dir"]
            )

            os.makedirs(transformed_dir, exist_ok=True)

            return DataTransformationConfig(
                clean_data_file_path=clean_file,
                transformed_data_dir=transformed_dir
            )

        except Exception as e:
            raise AppException(e, sys)

    # 🔹 MODEL TRAINER
    def get_model_trainer_config(self) -> ModelTrainerConfig:
        try:
            config = self.configs_info["model_trainer_config"]
            transformation_config = self.configs_info["data_transformation_config"]
            ingestion_config = self.configs_info["data_ingestion_config"]

            artifacts_dir = self.get_artifacts_dir()
            dataset_dir = ingestion_config["dataset_dir"]

            transformed_file = os.path.join(
                artifacts_dir, dataset_dir, transformation_config["transformed_data_dir"], "transformed_data.pkl"
            )

            model_dir = os.path.join(
                artifacts_dir, config["trained_model_dir"]
            )

            os.makedirs(model_dir, exist_ok=True)

            return ModelTrainerConfig(
                transformed_data_file_dir=transformed_file,
                trained_model_dir=model_dir,
                trained_model_name=config["trained_model_name"]
            )

        except Exception as e:
            raise AppException(e, sys)

    # 🔹 RECOMMENDATION
    def get_recommendation_config(self) -> ModelRecommendationConfig:
        try:
            config = self.configs_info["recommendation_config"]
            validation_config = self.configs_info["data_validation_config"]
            model_config = self.configs_info["model_trainer_config"]

            artifacts_dir = self.get_artifacts_dir()

            book_names = os.path.join(artifacts_dir, validation_config["serialized_objects_dir"], "book_names.pkl")
            book_pivot = os.path.join(artifacts_dir, validation_config["serialized_objects_dir"], "book_pivot.pkl")
            final_rating = os.path.join(artifacts_dir, validation_config["serialized_objects_dir"], "final_rating.pkl")

            model_path = os.path.join(artifacts_dir, model_config["trained_model_dir"], model_config["trained_model_name"])

            return ModelRecommendationConfig(
                book_name_serialized_objects=book_names,
                book_pivot_serialized_objects=book_pivot,
                final_rating_serialized_objects=final_rating,
                trained_model_path=model_path
            )

        except Exception as e:
            raise AppException(e, sys)