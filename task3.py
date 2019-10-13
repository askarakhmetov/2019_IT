import numpy as np

def get_indices(N, n_batches, split_ratio):
    """Generates splits of indices from 0 to N-1 into uniformly distributed\
       batches. Each batch is defined by 3 indices [i, j, k] where\
       (j-i) = split_ratio*(k-j). The first batch starts with i = 0,\
       the last one ends with k = N - 1.
    Args:
        N (int): total counts
        n_batches (int): number of splits
        split_ratio (float): split ratio, defines position of j in [i, j, k].

    Returns:
        generator for batch indices [i, j, k]
    """
    #shag = N//(n_batches*2)+1
    shag = np.ceil(N/(n_batches*2)) + 1
    inds = np.array([0, 0, 0])
    for i in range(n_batches):
        if i == (n_batches-1) and ((0+(i)*shag)+(shag/split_ratio)+shag)!=(N-1):
            tmp=shag+1
            inds=[N-1-tmp-tmp/split_ratio,N-1-tmp, N-1]
        else:
            inds=[(i)*shag, ((0+(i)*shag)+(shag/split_ratio)), ((0+(i)*shag)+(shag/split_ratio)+shag)]

        yield inds

def main():
    for inds in get_indices(10, 5, 0.25):
        print(inds)
    # expected result:
    # [0, 44, 55]
    # [11, 55, 66]
    # [22, 66, 77]
    # [33, 77, 88]
    # [44, 88, 99]

if __name__ == "__main__":
    main()