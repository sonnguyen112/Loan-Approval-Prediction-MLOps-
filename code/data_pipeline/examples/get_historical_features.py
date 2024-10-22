from feast import FeatureStore
import pandas as pd
from datetime import datetime

store = FeatureStore(repo_path="../feature_repo")

entity_df = pd.DataFrame.from_dict(
    {
        "driver_id": [1001, 1002, 1003, 1004],
        "event_timestamp": [
            datetime(2022, 5, 11, 11, 59, 59),
            datetime(2022, 6, 12, 1, 15, 10),
            datetime.now(),
            datetime(2022, 6, 12, 16, 0, 0)
        ],
    }
)
training_df = store.get_historical_features(
    entity_df=entity_df, features=[
        "driver_stats:acc_rate", "driver_stats:conv_rate", "driver_stats:avg_daily_trips"]
).to_df()
# Get 10 records
print(training_df.head(10))
