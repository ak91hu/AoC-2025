input_str = "96952600-96977512,6599102-6745632,32748217-32835067,561562-594935,3434310838-3434398545,150-257,864469-909426,677627997-677711085,85-120,2-19,3081-5416,34-77,35837999-36004545,598895-706186,491462157-491543875,5568703-5723454,6262530705-6262670240,8849400-8930122,385535-477512,730193-852501,577-1317,69628781-69809331,2271285646-2271342060,282-487,1716-2824,967913879-967997665,22-33,5722-11418,162057-325173,6666660033-6666677850,67640049-67720478,355185-381658,101543-146174,24562-55394,59942-93946,967864-1031782"

ranges = []
max_limit = 0
for part in input_str.split(','):
    start, end = part.split('-')
    r = (int(start), int(end))
    ranges.append(r)
    if r[1] > max_limit:
        max_limit = r[1]

invalid_ids = set()

# Seeds up to 5 digits are sufficient to cover the max_limit (~10 digits)
for seed in range(1, 100000):
    s_str = str(seed)
    current_str = s_str + s_str # Start with k=2
    
    while True:
        if len(current_str) > len(str(max_limit)) + 1:
             break 
             
        val = int(current_str)
        if val > max_limit:
            break
        
        # Check ranges
        for start, end in ranges:
            if start <= val <= end:
                invalid_ids.add(val)
                break
        
        current_str += s_str
print(f"Total sum: {sum(invalid_ids)}")
