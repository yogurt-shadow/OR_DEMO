\ Model cutting stock
\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  5 x[0] + 5 x[1] + 5 x[2]
Subject To
 R0: 2 x[0] >= 30
 R1: x[1] >= 20
 R2: x[2] >= 40
Bounds
Generals
 x[0] x[1] x[2]
End
