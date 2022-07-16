def lengthOfLongestSubstring(s):
    
    max_so_far = 0
    max_ending_here = 0
    
    seen_so_far = []
    for c in s:
        print(seen_so_far)
        if c in seen_so_far:
            seen_so_far = [c]
            max_ending_here = 1
            if max_ending_here > max_so_far:
                max_so_far = max_ending_here
        else:
            seen_so_far.append(c)
            max_ending_here += 1
            if max_ending_here > max_so_far:
                max_so_far = max_ending_here
    return max_so_far

### Correct solution

def lengthOfLongestSubstring(s):
    
    start = 0
    result = 0
    seen = {}

    for idx,ch in enumerate(s):
        if ch in seen and start <= seen[ch]:
            start = seen[ch] + 1
        else:
            result = max(result, idx-start+1)
        
        seen[ch] = idx
    
    return result

if __name__ == "__main__":
    s = "dvdf"
    lengthOfLongestSubstring(s)