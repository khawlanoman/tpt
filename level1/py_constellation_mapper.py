from typing import List, Tuple
def constellation_mapper(stars: List[Tuple[int, int]], dim: int) -> List[str]:
    tab = []
    
    col = dim
    row = dim
  
    for c in range(col):
        coll = ''
        for r in range(row):
            
                if (c, r) in stars:
                    coll+='*'
                else:
                    coll+='.'
        tab.append(coll)
    return tab


print(constellation_mapper([(1, 0), (1, 1), (1, 2)], 3))