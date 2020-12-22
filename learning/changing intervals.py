print('<상수>\n교통정체 발생율 = %.2f \n도로 길이 = %d \n신호등 간격 = %d \n차 개수 = %d \n차간 안전거리 = %d \n(차)최대 속도 = %d' %(troll, road_len, interval, num, dis, speed))
print('\n\n1을 누르면 상수를 변경하며, 1이 아닌 아무 문자를 입력하면 위 상수로 실행합니다',end = ('\t: '))
a = input()

if a == '1' :
    print('교통정체 발생율(현재 값 = %.2f)' %(troll), end = ('\t: '))
    troll_ = float(input())
    print('도로 길이(현재 값 = %d)' %(road_len), end = ('\t: '))
    road_len_ = int(input())
    print('신호등 간격(현재 값 = %d)' %(interval), end = ('\t: '))
    interval_ = int(input())
    print('차 대수(현재 값 = %d)' %(num), end = ('\t: '))
    num_ = int(input())
    print('차간 안전거리(현재 값 = %d)' %(dis), end = ('\t: '))
    dis_ = int(input())
    print('(차)최대 속도(현재 값 = %d)' %(speed), end = ('\t: '))
    speed_ = int(input())
    
    print('\n<바뀐 상수>')
    if troll == troll_ :
        print('교통정체 발생율 = %.2f' %(troll))
    else :
        print('교통정체 발생율 = %.2f  ==>  %.2f' %(troll, troll_))
        troll = troll_
    if road_len == road_len_ :
        print('도로 길이 = %d' %(road_len))
    else : 
        print('도로 길이 = %d  ==>  %d' %(road_len, road_len_))
        road_len = road_len_
    if interval == interval_ :
        print('신호등 간격 = %d' %(interval))
    else :
        print('신호등 간격 = %d  ==>  %d' %(interval, interval_))
        interval = interval_
    if num == num_ :
        print('차 대수 = %d' %(num))
    else :
        print('차 대수 = %d  ==>  %d' %(num, num_))
        num = num_
    if dis == dis_ :
        print('차간 안전거리 = %d' %(dis))
    else :
        print('차간 안전거리 = %d  ==>  %d' %(dis, dis_))
        dis = dis_
    if speed == speed_ :
        print('(차)최대 속도 = %d' %(speed))
    else :
        print('(차)최대 속도 = %d  ==>  %d' %(speed, speed_))
        speed = speed_
