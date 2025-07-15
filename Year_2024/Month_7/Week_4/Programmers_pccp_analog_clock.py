from fractions import Fraction

def solution(h1,m1,s1,h2,m2,s2):
    answer = 0
    h_pos = Fraction((h1 % 12), 1) + Fraction(m1,60) + Fraction(s1,3600)
    m_pos = Fraction(m1,1) + Fraction(s1,60)
    s_pos = Fraction(s1)

    if s_pos == h_pos or s_pos == m_pos:
        answer += 1

    flag_m = -1 if m_pos - s_pos < 0 else 1
    flag_h = -1 if h_pos*5 - s_pos < 0 else 1

    elapse = (h2 * 3600 + m2 * 60 + s2) - (h1 * 3600 + m1 * 60 + s1)

    for _ in range(elapse):
        s_nxt_pos = (s_pos + Fraction(1, 1))
        m_nxt_pos = (m_pos + Fraction(1, 60))
        h_nxt_pos = (h_pos + Fraction(1,3600))

        temp_flag_m = -1 if m_nxt_pos - s_nxt_pos < 0 else 1
        temp_flag_h = -1 if h_nxt_pos - s_nxt_pos < 0 else 1

        if not flag_m == temp_flag_m:
            answer += 1
            flag_m = temp_flag_m
        if not flag_h == temp_flag_h:
            answer += 1
            flag_h = temp_flag_h
        h_pos = h_nxt_pos % 12
        m_pos = m_nxt_pos % 60
        s_pos = s_nxt_pos % 60
    if s_pos == h_pos or s_pos == m_pos:
        answer += 1

    print(answer)
