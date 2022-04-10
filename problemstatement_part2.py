def case2(pos,rem_moves):

    if pos== 98:
        return 0
    if rem_moves == 0:
        if pos==100:
            return 1
        else:
            return 0
    ans = 0
    for i in range(1,7):
        if pos + i <= 100:
            ans +=case2(pos + i, rem_moves - 1)
    return ans

p1=88
p2=87
print("possible dice throws required by:")
print("Player 1:", case2(p1,4))
print("Player 2:", case2(p2,4))