def Check(s):
    netMax = netMin = 0;        # net number of open/closed brackets
    for i in range(len(s)):
        if ('a' <= s[i] <= 'z') or (s[i] in [' ', ':', '(', ')']):

            if s[i] == '(':
                netMax += 1;
                if s[i-1] != ':':
                    netMin += 1;
            if s[i] == ')':
                netMin -= 1;
                if s[i-1] != ':':
                    netMax -= 1;

            netMin = max(netMin, 0);
            if netMax < 0:
                return 'NO'
        else:
            return 'NO'
    if netMin != 0:
        return 'NO'
    return 'YES'


T = int(raw_input());
for case in range(1, T+1):
    print 'Case #%i: %s' % (case, Check(' '+raw_input()));
