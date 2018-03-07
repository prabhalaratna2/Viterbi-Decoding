states = ('start','Noun', 'Verb','Adv','stop')

observations = ('start','Learning', 'Changes', 'Throughly','stop')

start_probability = {'start': 1,'Noun': 0.2, 'Verb': 0.3, 'Adv': 0, 'stop': 0}

transition_probability = {
   'start' : {'start' : 0,'Noun': 0.2, 'Verb': 0.3, 'Adv':0,'stop':0},
   'Noun' : {'start' : 0,'Noun': 0.1, 'Verb': 0.3,'Adv': 0.1, 'stop': 0},
   'Verb' : {'start' : 0,'Verb': 0.1, 'Noun': 0.4, 'Adv': 0.4, 'stop': 0},
   'Adv' : {'start' : 0,'Verb': 0, 'Noun': 0, 'Adv': 0,'stop': 0.1},
   'stop' : {'start' : 0,'Verb': 0, 'Noun': 0, 'Adv': 0,'stop': 1}
   }
emission_probability = {
   'start':{'start': 1,'Learning': 0, 'Changes': 0, 'Throughly': 0,'stop': 0},
   'Verb' : {'start': 0,'Learning': 0.003, 'Changes': 0.004, 'Throughly': 0,'stop': 0},
   'Noun' : {'start': 0,'Learning': 0.001, 'Changes': 0.003, 'Throughly': 0,'stop': 0},
   'Adv' : {'start': 0,'Learning': 0,'Changes': 0,'Throughly': 0.002,'stop': 0},
   'stop':{'start': 0,'Learning': 0, 'Changes': 0, 'Throughly': 0,'stop': 1}
   }
# Helps visualize the steps of Viterbi.
def print_dptable(Viterbi):
    Viterbi_matrix = "    " + " ".join(("%15s" % observations[i]) for i in range(len(Viterbi))) + "\n"
    for y in Viterbi[0]:
        Viterbi_matrix += "%.15s: " % y
        Viterbi_matrix += " ".join("%.15s" % ("%.15f" % v[y]) for v in Viterbi)
        Viterbi_matrix += "\n"
    print(Viterbi_matrix)

def viterbi(obs, states, start_p, trans_p, emit_p):
    Viterbi = [{}]
    path = {}

    for y in states:
        Viterbi[0][y] = start_p[y] * emit_p[y][obs[0]]
        path[y] = [y]

    for t in range(1, len(obs)):
        Viterbi.append({})
        newpath = {}

        for y in states:
            (prob, state) = max((Viterbi[t-1][y0] * trans_p[y0][y] * emit_p[y][obs[t]], y0) for y0 in states)
            Viterbi[t][y] = prob
            newpath[y] = path[state] + [y]

        path = newpath

    print_dptable(Viterbi)
    (prob, state) = max((Viterbi[t][y], y) for y in states)
    return (prob, path[state])

def Homework():
    return viterbi(observations,
                   states,
                   start_probability,
                   transition_probability,
                   emission_probability)

print("POS Output:",Homework())
