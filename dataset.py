import pickle
import tarfile
import lmdb

# with open('oc22_metadata.pkl','rb') as f:
#     data = pickle.load(f)
    
# print(len(data))

tar = tarfile.open('is2res_total_train_val_test_lmdbs.tar.gz')
tar.extractall()
tar.close()