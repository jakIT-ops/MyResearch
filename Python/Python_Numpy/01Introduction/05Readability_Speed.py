import numpy as np
# More readability, less speed
def function_1(seq, sub): 
    return [i for i in range(len(seq) - len(sub) +1) if seq[i:i+len(sub)] == sub]

# More speed, less readability  
def function_2(seq, sub):
    target = np.dot(sub, sub)
    candidates = np.where(np.correlate(seq, sub, mode='valid') == target)[0]
    check = candidates[:, np.newaxis] + np.arange(len(sub))
    mask = np.all((np.take(seq, check) == sub), axis=-1)
    return candidates[mask]

seq=[12, 10, 2, 45, 13, 65, 11, 8, 5]
sub=[11, 8]
print("Function 1:",function_1(seq,sub))
print("Function 2:",function_2(seq,sub))