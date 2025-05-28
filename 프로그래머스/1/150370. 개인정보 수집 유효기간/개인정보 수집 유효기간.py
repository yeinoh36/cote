def solution(today, terms, privacies):
    answer = []
    
    def date_to_int(date_str):
        y, m, d = map(int, date_str.split('.'))
        return y, m, d
    
    def compare_date(y1, m1, d1, y2, m2, d2):
        if y1 != y2:
            return y1 < y2
        if m1 != m2:
            return m1 < m2
        return d1 <= d2
    
    ty,tm, td = date_to_int(today)

    term_dict = {}
    for term in terms:
        kind, period = term.split()
        term_dict[kind] = int(period)
    
    for i, privacy in enumerate(privacies):
        date, kind = privacy.split()
        y, m, d = date_to_int(date)
        m += term_dict[kind]
        ey = y + (m-1) // 12
        em = (m-1) % 12 +1
        ed = d
        
        if compare_date(ey, em, ed, ty, tm, td):
            answer.append(i + 1)
        
    return answer