import numpy as np;
import matplotlib.pyplot as plt;
def scale_data(array_2d:np.ndarray):
   mean = np.mean(array_2d, axis = 0);
   print(mean)
   stddev = np.std(array_2d, axis = 0);
   out = np.divide(np.subtract(array_2d, mean), stddev)
   print(stddev)
   return out


def read_csv(path):
    out = []
    with open(path, 'r') as file:
        file_content = file.read()
    lines = file_content.splitlines();
    skipped = False;
    for i in lines:
        if not skipped:
            skipped = True;
            continue;
        tmp = []
        for j in i.split(','):
            if len(j)>0:
                tmp.append(float(j))
        out.append(np.array(tmp))
    l = len(out[0])
    return out

data = read_csv("LAB_1_Template/hgcal.csv")
data = scale_data(np.array(data))
print(data)
