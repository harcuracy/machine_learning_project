import mlflow
import pandas as pd
from joblib import  load
from sklearn.metrics import root_mean_squared_error, mean_absolute_error, r2_score


from src.utils import save_json
from src.entity.config_entity import ModelEvaluationConfig


class ModelEvaluation:
    def __init__(self,config:ModelEvaluationConfig):
        self.config = config
        
    def eval_metric(self,y_true,y_pred):
        rmse = root_mean_squared_error(y_true, y_pred,)
        mae = mean_absolute_error(y_true, y_pred)
        r2 = r2_score(y_true, y_pred)
        
        return rmse, mae, r2
    
    def log_into_mlflow(self):
        model = load(self.config.model_file)
        test_data = pd.read_csv(self.config.test_data_file)
        X_test = test_data.drop(columns=[self.config.target_column])
        y_test = test_data[self.config.target_column]
        
        mlflow.set_tracking_uri(self.config.mlflow_tracking_uri)
        mlflow.set_experiment(experiment_name="model_evaluation")
        
        with mlflow.start_run():
            y_pred = model.predict(X_test)
            rmse,mae, r2 = self.eval_metric(y_test, y_pred)
            scores = {
                "rmse" : rmse,
                "mae": mae,
                "r2": r2
            }
            save_json( scores, self.config.report_file)
            mlflow.log_params(self.config.all_params)
    
            mlflow.log_metrics(scores)
            mlflow.sklearn.log_model(model, artifact_path="model_training", registered_model_name="ElasticNet")
            

    
