s = "cbaebabacd"
p = "abc"
def allanagram(s,p):
    pfreq = {}
    for ch in p:
        pfreq[ch] = pfreq.get(ch, 0) + 1
    window_freq = {}
    result = []
    left = 0
    for right in range(len(s)):
        ch = s[right]
        window_freq[ch] = window_freq.get(ch,0) + 1
        if right - left + 1 > len(p):
            left_ch = s[left]
            window_freq[left_ch] -= 1
            if window_freq[left_ch] == 0:
                del window_freq[left_ch]
            left += 1
        if window_freq == pfreq:
            result.append(left)
    return result

print(allanagram(s,p))
        