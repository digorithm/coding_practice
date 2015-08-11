


def is_cancelled(k,arrivals):
    before_class = [x for x in arrivals if x<=0]
    after_class = [x for x in arrivals if x>0]

    if len(before_class) < k:
        return "YES"
    else:
        return "NO"


if __name__ == "__main__":
    test_cases = int(raw_input())
    for t in xrange(test_cases):
        n_and_k = map(int,raw_input().split())
        arrivals = map(int,raw_input().split())
        print is_cancelled(n_and_k[1], arrivals)

