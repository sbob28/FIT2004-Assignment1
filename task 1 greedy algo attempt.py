def fuse(fitmons):
    
    while len(fitmons) > 1: #while more than one fitmon exists, continue fusing
        max_cuteness = -1
        best_index = None

        for i in range(len(fitmons) - 1): #to find the best pair to fuse bc v-1

            # the potential cuteness if fused (the best pair that was found just before)
            potential_cuteness = int(fitmons[i][1] * fitmons[i][2] + fitmons[i + 1][1] * fitmons[i + 1][0])
            if potential_cuteness > max_cuteness:
                max_cuteness = potential_cuteness
                best_index = i
        
        # to fuse
        new_fitmon = [
            fitmons[best_index][0],  #left affinity (new)
            max_cuteness,  # new score (cuteness)
            fitmons[best_index + 1][2]  #right affinity also new
        ]
        
        # puts the new one in place of the old fusing fitmons
        fitmons.pop(best_index)
        fitmons[best_index] = new_fitmon
    
    # returns the cuteness score (final fused fitmon)
    return fitmons[0][1]

print(fuse([[0, 29, 0.9], [0.9, 91, 0.8], [0.8, 48, 0]]))  # Expected: 126
print(fuse([[0, 48, 0.8], [0.8, 91, 0.9], [0.9, 29, 0]]))  # Expected: 126
print(fuse([[0, 50, 0.3], [0.3, 50, 0.3], [0.3, 50, 0]]))  # Expected: 24
print(fuse([[0, 50, 0.6], [0.6, 50, 0.3], [0.3, 50, 0]]))  # Expected: 48
print(fuse([[0, 50, 0.3], [0.3, 50, 0.3], [0.3, 80, 0]]))  # Expected: 33
print(fuse([[0, 50, 0.6], [0.6, 98, 0.4], [0.4, 54, 0.9], [0.9, 6, 0.3],
             [0.3, 34, 0.5], [0.5, 66, 0.3], [0.3, 63, 0.2], [0.2, 52, 0.5],
             [0.5, 39, 0.9], [0.9, 62, 0]]))  # Expected: 132
