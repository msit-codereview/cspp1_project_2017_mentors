def lcs(xstr, ystr):
    """
    >>> lcs('thisisatest', 'testing123testing')
    'tsitest'
    """
    if not xstr or not ystr:
        print "2" 
        return ""
    x, xs, y, ys = xstr[0], xstr[1:], ystr[0], ystr[1:]
    if x == y:
        print "3"
        return x + lcs(xs, ys)
    else:
        print "4"
        return max(lcs(xstr, ys), lcs(xs, ystr), key=len)

print "LCS is " + lcs('Doubttruthtobealiar','Tobeornottobe')
# print "LCS is " + str(lcs('thisisatest', 'testing123testing'))