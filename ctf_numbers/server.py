import random
import sys

if __name__ == '__main__':
    number_list=[]
    ans = 0
    for i in range(5):
        rnd = random.randint(0, 2)
        if rnd == 0:
            base = 'b'
            prefix='0b'
        elif rnd == 1:
            base = 'o'
            prefix='0o'
        elif rnd == 2:
            base = 'x'
            prefix='0x'
        num = random.randint(0, 1000)
        ans += num
        number_list.append(prefix+str(format(num, base)))
    print(' '.join(number_list))
    sys.stderr.write(' '.join(number_list)+'\n')
    sys.stderr.write(str(ans)+'\n')

    sys.stdout.flush()

    line = sys.stdin.readline()
    # print(line)
    if int(line) == ans:
        print('correct!, flag is CTF{xxxxxxxx}')
        sys.stderr.write('correct\n')
    else:
        print('wrong anser')
        sys.stderr.write('wrong\n')

