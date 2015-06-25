#include "builtin.hpp"
#include "solution.hpp"

/**
Your program is to use the brute-force approach in order to find the Answer to Life, the Universe, and Everything. More precisely... rewrite small numbers from input to output. Stop processing input after reading in the number 42. All numbers at input are integers of one or two digits.
*/

namespace __solution__ {

str *const_0;


str *__name__;



void *solution(list<__ss_int> *l) {
    __iter<__ss_int> *__1;
    list<__ss_int> *__0;
    __ss_int __2, n;
    list<__ss_int>::for_in_loop __3;


    FOR_IN(n,l,0,2,3)
        if ((n==42)) {
            break;
        }
        print2(NULL,0,1, ___box(n));
    END_FOR

    return NULL;
}

void __init() {
    const_0 = new str("__main__");

    __name__ = new str("__main__");

    if (__eq(__name__, const_0)) {
        solution((new list<__ss_int>(10,1,2,3,4,5,53,42,12,2,3)));
    }
}

} // module namespace

int main(int, char **) {
    __shedskin__::__init();
    __shedskin__::__start(__solution__::__init);
}
