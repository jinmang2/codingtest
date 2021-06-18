"""
가장 동전을 많이 얻을 경로 찾기
- Beam Search로 풀기
"""
TestCase = {
    "case1": {
        "answer": 240,
        "tile": [[27, 47, 31, 33, 5],
                 [17,  0, 33, 43, 0],
                 [36, 49,  0, 27, 0],
                 [44, 32, 10, 32, 0]]
    }
}


def solution(tile):
    N = len(tile)    # number of rows
    M = len(tile[0]) # number of columns
    beam_size = 20
    states = [(tile[0][0], 0, 0)] # Initial state i.e., (score, r_ind, c_ind)
    for i in range(N + M - 2):
        new_states = []
        for (score, r_ind, c_ind) in states:
            if r_ind < N - 1:
                new_states.append((score + tile[r_ind+1][c_ind], r_ind + 1, c_ind))
            if c_ind < M - 1:
                new_states.append((score + tile[r_ind][c_ind+1], r_ind, c_ind + 1))
        states = sorted(new_states, reverse=True)[:beam_size]
    return states[0][0] # Max score
