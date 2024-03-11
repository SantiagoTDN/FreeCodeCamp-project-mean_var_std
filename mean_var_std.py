import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    else:
        list=np.array(list)
        g=list.reshape(3,3)
        calculations=dict()
        calculations["mean"]=[np.mean(g, axis=0).tolist(),np.mean(g, axis=1).tolist(),np.mean(list).tolist()]
        calculations["variance"]=[np.var(g,axis=0).tolist(), np.var(g,axis=1).tolist(), np.var(list).tolist()]
        calculations["standard deviation"]=[np.std(g,axis=0).tolist(), np.std(g,axis=1).tolist(), np.std(list).tolist()]
        calculations["max"]=[np.max(g,axis=0).tolist(), np.max(g,axis=1).tolist(), np.max(list).tolist()]
        calculations["min"]=[np.min(g,axis=0).tolist(), np.min(g,axis=1).tolist(), np.min(list).tolist()]
        calculations["sum"]=[np.sum(g,axis=0).tolist(), np.sum(g,axis=1).tolist(), np.sum(list).tolist()]
    return calculations