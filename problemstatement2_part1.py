def case1(pos,rem_moves):

    if pos==100:
        return 1
    if rem_moves == 0:
        return0
    ans = 0
    f0r i in range(1,7):
     if pos + i <= 100:
         ans +=case1(pos + i, rem_moves - 1)
    return ans