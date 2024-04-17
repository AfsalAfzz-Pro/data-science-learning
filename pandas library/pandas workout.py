import pandas as pd
import numpy as np

# normal pandas dataframe
df = pd.DataFrame([[1,2],
                   [3,4]])
print(df)


# pandas dataframe with nan value
d = pd.DataFrame({'colours': ["red", "blue", "red", np.nan, "yellow"], "student":[3,5,7,2,np.nan]}, index=
                 [1,2,3,4,5])

print(d)

# findig count of each value
print(d.value_counts())

# fills empty values
print(d.fillna())

# forward fills empty values
print(d.ffill())

# backward fills empty values
print(d.bfill())

