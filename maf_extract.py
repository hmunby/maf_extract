import sys
file_test = sys.argv[1]
target_sequence_name = sys.argv[2]
range_start = int(sys.argv[3])
range_end = int(sys.argv[4])

line_gen = open(file_test)
reading_file = 1
while reading_file == 1:
    linecount = 0
    block = []
    while True:
        nextline = line_gen.readline()
        linecount = linecount + 1
        if nextline == '\n':
            break
        if not nextline:
            reading_file = 0
            break
        block.append(nextline)

    target_line = [s for s in block if target_sequence_name in s]

    if not target_line:
        pass
    else:
        (alignment_start, alignment_length, direction, size) = target_line[0].split()[2:6]
        if direction == '-':
            end = int(size) - int(alignment_start)
            start = end - int(alignment_length) + 1
        else:
            start = int(alignment_start) + 1
            end = start + int(alignment_length) + 1
        if (range_start <= start <= range_end) or (start <= range_start <= end):
            print(*block)
print("finished scanning file")
exit
