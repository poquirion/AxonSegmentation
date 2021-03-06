import sklearn
import pickle
import numpy as np
from functools import partial
from sklearn.externals import joblib
from features_extraction import features
import time
from skimage import exposure
import warnings
warnings.filterwarnings('ignore')


def prediction(X, clf):
    return clf.predict(X)

def parallized_pred(sequence, clf):
    from multiprocessing import Pool
    pool = Pool(processes=4)
    mapfunc = partial(prediction, clf=clf)
    result = pool.map(mapfunc, sequence)
    cleaned = [x for x in result if not x is None]
    cleaned = np.asarray(cleaned)
    cleaned = np.array([x[0] for x in cleaned])
    pool.close()
    pool.join()
    return cleaned


#######################################################################################################################
#                                            Test                                                                     #
#######################################################################################################################

#
# result_number = 3
# folder = 'resultsPipeline/result_%s'%result_number
#
# clf = joblib.load(folder+'/classifier/clf.pkl')
#
# data = pickle.load(open("data/groundTruth.pkl", "rb"))
# img = data['image']
# img = exposure.equalize_hist(img)
# mask = data['mask']
#
#
# X_test = features(img, 3)[:, :]
# print X_test.shape
#
# start = time.time()
# a = parallized_pred(X_test, clf)
# para_time = time.time()-start
#
# print para_time
#
# start2 = time.time()
# b = clf.predict(X_test)
# norm_time = time.time()-start2
#
# print norm_time
#
# print 'ratio : ', norm_time/para_time







