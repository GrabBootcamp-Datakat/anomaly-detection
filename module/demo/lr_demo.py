import sys
sys.path.append('../')
from train.models import LR
from train import dataloader, preprocessing

struct_log = '../../result/merged_logs.log_structured.csv' # The structured log file
label_file = '../../result/merged_labled.csv' # The anomaly label file

if __name__ == '__main__':
    (x_train, y_train), (x_test, y_test) = dataloader.load_Spark(struct_log,
                                                                label_file=label_file,
                                                                window='session', 
                                                                train_ratio=0.5,
                                                                split_type='uniform')

    feature_extractor = preprocessing.FeatureExtractor()
    x_train = feature_extractor.fit_transform(x_train, term_weighting='tf-idf')
    x_test = feature_extractor.transform(x_test)

    model = LR()
    model.fit(x_train, y_train)

    print('Train validation:')
    precision, recall, f1 = model.evaluate(x_train, y_train)

    print('Test validation:')
    precision, recall, f1 = model.evaluate(x_test, y_test)
