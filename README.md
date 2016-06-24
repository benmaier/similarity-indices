# SimInd

Provides two classes for the computation of either incidence based or abundance based similarity measures for data in numpy arrays.

## Install

```bash
$ pip install ../simind    # or
$ python setup.py install
```

## Example

```python
from __future__ import print_function
import simind
import numpy as np

a = np.array([ 0, 1, 2, 3, 4 ],dtype=int)
b = np.array([ 3, 4, 5], dtype=int)

# initialize
similarities = simind.incidence_based_similarity(a,b,assume_unique=True)

print(similarities.jaccard())
print(similarities.sorensen())

# for the abundance based similarities, one needs dictionaries with weights
# (traditionally, the weight would be the number of times, species "key" was
# found, but the weights don't have to be integers)
wa = { 0: 0.5, 1: 2, 2: 0.75, 3: 1, 4: 1 }
wb = { 3: 2, 4: 1, 5: 2 }

# initialize
similarities = simind.abundance_based_similarity(a,b,wa,wb,assume_unique=True)

print(similarities.jaccard())
print(similarities.sorensen())
```
