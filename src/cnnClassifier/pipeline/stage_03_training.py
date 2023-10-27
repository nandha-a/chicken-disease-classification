from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.prepare_callbacks import Preparecallbacks
from cnnClassifier.components.training import Training
from cnnClassifier import logger

STAGE_NAME = "Training"

class ModelTrainingPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config = ConfigurationManager()
        prepare_callbacks_config = config.get_prepare_callbacks_config()
        prepare_callbacks = Preparecallbacks(config=prepare_callbacks_config)
        callback_list = prepare_callbacks.get_tb_ckpt_callback()

        training_config = config.get_training_config()
        training = Training(config=training_config)
        training.get_base_model()
        training.train_generator()
        training.train(callback_list=callback_list)


if __name__ == "__main__":
    try:
        logger.info(f"******************************")
        logger.info(f">>>>>>>> stage {STAGE_NAME} started <<<<<<<<")
        obj = ModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>> {STAGE_NAME} completed <<<<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e