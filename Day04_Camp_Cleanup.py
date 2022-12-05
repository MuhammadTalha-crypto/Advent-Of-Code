def total_contained(fn, pair_assignments):
        return sum(fn(boundaries(pair)) for pair in pair_assignments)

def boundaries(pair_data):
    	return tuple(tuple(int(elem)for elem in pair.split("-")) for pair in pair_data.strip().split(","))

def is_containing(pair):
    	return ((pair[0][0] <= pair[1][0] and pair[0][1] >= pair[1][1]) or (pair[0][0] >= pair[1][0] and pair[0][1] <= pair[1][1]))

def partial_overlap(pair):
    	return ((pair[0][0] <= pair[1][0] <= pair[0][1]) or (pair[1][0] <= pair[0][0] <= pair[1][1]))


if __name__ == "__main__":

  with open("test.txt", "r") as ifile:
    input = ifile.readlines()

  print("Fully overlapping tasks: {}".format(total_contained(is_containing, input)))
  print("Partially overlapping tasks: {}".format(total_contained(partial_overlap, input)))