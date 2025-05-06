import sys
sys.path.append('../')
from train.models import invariants_miner
from train import dataloader, preprocessing

struct_log = '../../result/merged_logs.log_structured.csv' # The structured log file
label_file = '../../result/merged_labled.csv' # The anomaly label file
epsilon = 0.5 # threshold for estimating invariant space

if __name__ == '__main__':
    # Load structured log without label info
    (x_train, _), (x_test, _) = dataloader.load_Spark(struct_log,
                                                     window='session', 
                                                     train_ratio=0.5,
                                                     split_type='sequential')
    # Feature extraction
    feature_extractor = preprocessing.FeatureExtractor()
    x_train = feature_extractor.fit_transform(x_train)

    # Model initialization and training
    model = invariants_miner(epsilon=epsilon)
    model.fit(x_train)

    # Predict anomalies on the training set offline, and manually check for correctness
    y_train = model.predict(x_train)

    # Predict anomalies on the test set to simulate the online mode
    # x_test may be loaded from another log file
    x_test = feature_extractor.transform(x_test)
    y_test = model.predict(x_test)

    # If you have labeled data, you can evaluate the accuracy of the model as well.
    # Load structured log with label info
    (x_train, y_train), (x_test, y_test) = dataloader.load_Spark(struct_log,
                                                               label_file=label_file,
                                                               window='session', 
                                                               train_ratio=0.5,
                                                               split_type='sequential')   
    x_test = feature_extractor.transform(x_test)
    precision, recall, f1 = model.evaluate(x_test, y_test)

