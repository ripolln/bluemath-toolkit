# TODO all multiplications / divisions with np.pi could be removed without affecting end results
import numpy as np


def normalize_base(data, minis, maxis, idir=None):
    '''
    normalize data based on externally set max and min values

    data - data to normalize, data variables at columns.
    minis, maxis - externally set min and max values
    idir - directional columns indexes
    '''
    data_norm = (data - minis) / (maxis - minis)
    if idir is not None:
        data_norm[:, idir] = data[:, idir] * np.pi / 180.0
    return data_norm


def normalize(data, idir=None):
    '''
    normalize data for MaxDiss algorithm

    data - data to normalize, data variables at columns.
    idir - directional columns indexes
    '''
    minis = data.min(axis=0, keepdims=True)
    maxis = data.max(axis=0, keepdims=True)
    data_norm = normalize_base(data, minis, maxis, idir)
    return data_norm, minis, maxis


def denormalize(data_norm, minis, maxis, idir=None):
    '''
    denormalize data normalized for MaxDiss algorithm

    data_norm - normalized data, data variables at columns.
    minis, maxis - externally set min and max values
    idir - directional columns indexes
    '''
    data = data_norm * (maxis - minis) + minis
    if idir is not None:
        data[:, idir] = data_norm[:, idir] * 180.0 / np.pi
    return data


def normalized_distance(matrix, reference=0, idir=None):
    '''
    Normalized distance between rows in M and D

    matrix - numpy array
    reference - numpy array bradcastable to matrix or number
    idir - directional columns indexes
    '''
    dif =  matrix - reference
    if idir is not None:
        dir_absdif = abs(dif[:, idir])
        dif[:, idir] = np.minimum(dir_absdif, 2 * np.pi - dir_absdif) / np.pi
    dist = np.sum(dif**2, 1)
    return dist


def nearest_indexes(data_q, data, idir=None):
    '''
    for each row in data_q, find nearest point in data and store index.

    Returns array of indexes of each nearest point to all entries in data_q
    '''
    # normalize scalar and directional data
    data_norm, minis, maxis = normalize(data, idir)
    data_q_norm =  normalize_base(data_q, minis, maxis, idir)

    # compute distances, store nearest distance index
    i_near = np.zeros(data_q_norm.shape[0]).astype(int)
    for c, dq in enumerate(data_q_norm):
        D = normalized_distance(data_norm, dq, idir)
        i_near[c] = np.argmin(D)
    return i_near


def maxdiss(data, num_centers, idir=None, seed=None):
    '''
    Normalize data and calculate centers using maxdiss algorithm

    data - data to apply maxdiss algorithm, data variables at columns
    num_centers - number of centers to calculate
    idir - directional columns indexes
    '''
    print('\nMaxDiss parameters: {0} --> {1}\n'.format(data.shape[0], num_centers))
    data_norm = normalize(data, idir)[0]
    if seed is None:
        # seed = data[:, 0].argmax()  # previous default
        seed = normalized_distance(data_norm, 0, idir).argmax()

    bmus = [seed]
    cumdist = data_norm[:, 0] * 0
    for _ in range(1, num_centers):
        cumdist[bmus[-1]] = np.nan  # to avoid repeating centroids
        reference = data_norm[bmus[-1], :]
        cumdist += normalized_distance(data_norm, reference, idir)
        bmus += [cumdist.argmax()]
    centroids = data[bmus]
    return centroids
