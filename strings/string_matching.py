# Build a deterministic finite automata for the given pattern
# For the given text simulate the automata to see if pattern exists. 

"""
dfa for pattern ABAC

state       0 A 1 B 2 A 3 C 4
==========================
A           1   1   3   1
B           0   2   0   2
C           0   0   0   4

prev_state  0
"""
def _build_kmp_dfa(pat):
    num_states = len(pat)
    dfa = [[0 for _ in range(num_states)] for _ in range(128)]
    print(ord(pat[0]))
    dfa[ord(pat[0])][0] = 1

    prev_state = 0
    for state in range(1, len(pat)):
        for c in range(0, 128):
            dfa[c][state] = dfa[c][prev_state]
        dfa[ord(pat[state])][state] = state+1
        prev_state = dfa[ord(pat[state])][prev_state]

    for state in range(0, len(pat)):
        print(dfa[ord(pat[state])][state])
    return dfa

def string_match_kmp_automata(txt, pat):
    # dfa stores what state will we move to if we encounter a character at
    # a particular state, ie dfa[c][state_x] = state_y
    dfa = _build_kmp_dfa(pat)
    #print(dfa)
    state = 0	#start from state 0

    for t in range(0, len(txt)):
         c = ord(txt[t])
         state = dfa[c][state]
         if state == len(pat):
             return True

    print(state, c, t)
    return False

# for every position in txt, check if pat matches
# O(n**2)
def brute_force_string_match(txt, pat):
    for t in range(0, len(txt)-len(pat)):
        p = 0
        while p < len(pat):
            if txt[t+p] != pat[p]:
                break
            p += 1
        if p == len(pat):
            return True
    return False

def pattern_match(txt, pat, expected):
    print(brute_force_string_match(txt, pat) == expected, "brute force")
    print(string_match_kmp_automata(txt, pat) == expected, "kmp")

if __name__ == "__main__":
   pattern_match("ACABDGA", "DG", True)
   pattern_match("ACABasdf;lj;lkjjhagdlfkgfGA", "lfkg", True)
   pattern_match("ACABasdf;lj;lkjjhagdlfkgfGA", "lfg", False)
