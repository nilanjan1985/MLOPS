from creditcard.component.data_validation import DataValidation
from creditcard.config.configuration import Configuration
from creditcard.logger import logging
from creditcard.exception import CreditcardException
from collections import namedtuple
from datetime import datetime
import uuid
from creditcard.config.configuration import Configuartion
from creditcard.logger import logging, get_log_file_name
from creditcard.exception import HousingException
from threading import Thread
from typing import List
from multiprocessing import Process
from creditcard.entity.artifact_entity import ModelPusherArtifact, DataIngestionArtifact, ModelEvaluationArtifact
from creditcard.entity.artifact_entity import DataValidationArtifact, DataTransformationArtifact, ModelTrainerArtifact
from creditcard.entity.config_entity import DataIngestionConfig, ModelEvaluationConfig
from creditcard.component.data_ingestion import DataIngestion
from creditcard.component.data_validation import DataValidation
from creditcard.component.data_transformation import DataTransformation
from creditcard.component.model_trainer import ModelTrainer
from creditcard.component.model_evaluation import ModelEvaluation
from creditcard.component.model_pusher import ModelPusher

import os, sys
from collections import namedtuple
from datetime import datetime
import pandas as pd
from creditcard .constant import EXPERIMENT_DIR_NAME, EXPERIMENT_FILE_NAM

from creditcard.entity.artifact_entity import DataIngestionArtifact
from creditcard.entity.config_entity   import DataIngestionConfig
from creditcard.component.data_ingestion import DataIngestion
from creditcard.component.data_validation import DataValidation
from creditcard.component.data_transformation import DataTransformation
from creditcard.component.model_trainer import ModelTrainer
from creditcard.component.model_evaluation import ModelEvaluation
from creditcard.component.model_pusher import ModelPusher
import os, sys
from collections import namedtuple
from datetime import datetime
import pandas as pd
from creditcard.constant import EXPERIMENT_DIR_NAME, EXPERIMENT_FILE_NAME

import os , sys

class Pipeline:

    def __init__(self,config:Configuration = Configuration()) -> None:
        try:
            self.config=config
        except Exception as e:
            raise CreditcardException(e,sys) from e

    def start_data_ingestion(self)->DataIngestionArtifact:
        try:
            data_ingestion = DataIngestion(data_ingestion_config=self.config.get_data_ingestion_config())
            data_ingestion.initiate_data_ingestion()

        except Exception as e:
            raise CreditcardException(e,sys) from e

    def start_data_validation(self,data_ingestion_artifact:DataIngestionArtifact):
        try:
            data_validation = DataValidation(data_validation_config=self.config.get_data_validation_config(),
                                             data_ingestion_artifact=data_ingestion_artifact
                                             )
            return data_validation.initiate_data_validation()
        except Exception as e:
            raise CreditcardException(e, sys) from e
        pass

    def start_data_transformation(self,
                                  data_ingestion_artifact: DataIngestionArtifact,
                                  data_validation_artifact: DataValidationArtifact
                                  ) -> DataTransformationArtifact:
        try:
            data_transformation = DataTransformation(
                data_transformation_config=self.config.get_data_transformation_config(),
                data_ingestion_artifact=data_ingestion_artifact,
                data_validation_artifact=data_validation_artifact
            )
            return data_transformation.initiate_data_transformation()
        except Exception as e:
            raise CreditcardException(e, sys)


    def start_model_trainer(self):
        pass
    
    def start_model_evaluation(self):
        pass

    def start_model_pusher(self):
        pass       

    def run_pipeline(self):
        try:
            ## data ingestion 
            data_ingestion_artifact = self.start_data_ingestion()
            data_validation_artifact = self.start_data_validation(data_ingestion_artifact=data_ingestion_artifact)
        except Exception as e:
            raise CreditcardException(e,sys) from e           