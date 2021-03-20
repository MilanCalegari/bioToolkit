def editDistance(seq_a, seq_b):
  D = []
  for i in range(len(seq_a)+1):
    D.append([0 for _ in range(len(seq_b)+1)])
  
  for i in range(len(seq_a)+1):
    D[i][0] = i
  for i in range(len(seq_b)+1):
    D[0][i] = i

    for i in range(1, len(seq_a) + 1):
      for j in range(1, len(seq_b) + 1):
        distHorz = D[i][j-1] + 1
        distVert = D[i-1][j] + 1
        if seq_a[i-1] == seq_b[j-1]:
          distDiag = D[i-1][j-1]
        else:
          distDiag = D[i-1][j-1] + 1
        D[i][j] = min(distHorz, distVert, distDiag)

  return D[-1][-1]

def hammingDistance(seq_a, seq_b):
    if len(seq_a) != len(seq_b):
        raise ValueError("Strings must have the same size")
    else:
        distance = 0
        for i in range(len(seq_a)):
            if seq_a[i] != seq_b[i]:
                distance += 1
    return distance
            
