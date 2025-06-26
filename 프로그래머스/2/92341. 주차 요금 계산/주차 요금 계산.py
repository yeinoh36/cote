def solution(fees, records):
    answer = []
    car_dict = {}
    
    for record in records:
        time_str, num, action = record.split()
        h, m = map(int, time_str.split(":"))
        minutes = h * 60 + m
        
        if num not in car_dict:
            car_dict[num] = [0, None]
        
        if action == "IN":
            car_dict[num][1] = minutes
        else:
            in_time = car_dict[num][1]
            car_dict[num][0] += minutes - in_time
            car_dict[num][1] = None
    
    # 출차 안 된 차량 처리
    for num in car_dict:
        if car_dict[num][1] is not None:
            car_dict[num][0] += (23 * 60 + 59) - car_dict[num][1]
            car_dict[num][1] = None

    base_time, base_fee, unit_time, unit_fee = fees
    for num in sorted(car_dict):
        total = car_dict[num][0]
        if total <= base_time:
            fee = base_fee
        else:
            fee = base_fee + ((total - base_time + unit_time - 1) // unit_time) * unit_fee
        answer.append(fee)
    
    return answer