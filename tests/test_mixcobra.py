import unittest
import numpy as np
import os
import sys
from sklearn.metrics import mean_squared_error

from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
import logging
from tqdm import tqdm, trange

# Get the current directory of the test file
current_dir = os.path.dirname(__file__)

# Get the absolute path to the main directory (one level up)
main_dir = os.path.abspath(os.path.join(current_dir, ".."))

print(main_dir)

# Add the main directory to the Python path
sys.path.insert(0, main_dir)

from gradientcobra.mixcobra import MixCOBRARegressor

from sklearn.utils.estimator_checks import check_estimator


class TestPrediction(unittest.TestCase):
    def setUp(self):
        rd_state = np.random.RandomState(11111)
        n_features = 20

        # D1 = train machines; D2 = create COBRA; D3 = calibrate epsilon, alpha; D4 = testing
        X, y = make_regression(
            n_samples=1000, 
            n_features=n_features, 
            noise=1,
            random_state=rd_state)

        # Train-test data splitting
        X_train, X_test, y_train, y_test = train_test_split(
            X, 
            y, 
            test_size=0.2, 
            random_state=rd_state)

        agg_model = MixCOBRARegressor(random_state=rd_state,
                                      show_progress = True)
        agg_model.fit(X_train, y_train)

        self.y_train = y_train
        self.X_test = X_test
        self.y_test = y_test
        self.MixCOBRARegressor = agg_model

    def test_opt_bandwidth(self):
        expected_alpha = 1e-05
        expected_beta = 1.2244985714285717 #0.10101989898989899 #0.707079292929293
        self.assertAlmostEqual(expected_alpha, self.MixCOBRARegressor.optimization_outputs['opt_alpha'])
        self.assertAlmostEqual(expected_beta, self.MixCOBRARegressor.optimization_outputs['opt_beta'])
    
    def test_basic_estimators(self):
        expected = [1.2032133203682551, 1.2448736091320127, 1.2087950033295554, 3843.024108235918, 2578.96653974025]
        res = [mean_squared_error(self.MixCOBRARegressor.Pred_X_l_[:,j] / self.MixCOBRARegressor.normalize_constant_y, self.y_train[self.MixCOBRARegressor.iloc_l]) for j in range(len(expected))]
        for i in range(len(expected)):
            self.assertAlmostEqual(expected[i], res[i])

    def test_predict(self):
        expected = 14.759855788898653 #31.816559459542464 #30.966584258235706
        result = mean_squared_error(self.MixCOBRARegressor.predict(self.X_test), self.y_test)
        self.assertAlmostEqual(expected, result)
        
if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.DEBUG)
    unittest.main()
