import unittest
import numpy as np

from gradientcobra import GradientCOBRA
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.utils.estimator_checks import check_estimator
import logging

class TestPrediction(unittest.TestCase):
    def setUp(self):
        rd_state = np.random.RandomState(123)
        n_features = 20

        # D1 = train machines; D2 = create COBRA; D3 = calibrate epsilon, alpha; D4 = testing
        X, y = make_regression(
            n_samples=1000, 
            n_features=n_features, 
            noise=0.1,
            random_state=rd_state)

        # Train-test data splitting
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

        agg_model = GradientCOBRA(random_state=rd_state)
        agg_model.fit(X_train, y_train)

        self.test_data = X_test
        self.GradientCOBRA = agg_model

    def test_predict(self):
        expected = 54820.097730117064
        result = self.GradientCOBRA.predict(self.test_data)
        self.assertAlmostEqual(expected, result)

    def test_estimators(self):
        check_estimator(GradientCOBRA)

if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.DEBUG)
    unittest.main()
