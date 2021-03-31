import unittest

suite = unittest.TestLoader().discover('./', 'my*.py')

ruuner = unittest.TextTestRunner()
ruuner.run(suite)
