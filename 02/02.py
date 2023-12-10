def main():
    res = 0
    red_max = 12
    green_max = 13
    blue_max = 14
    with open('2.in') as f:
        for line in f.readlines():
            line = line.strip()
            game_str = line.split(':')[0]
            game_id = int(game_str.split()[1])
            pulls = line.split(':')[1].split(';')
            done = False
            for pull in pulls:
                color_strs = pull.split(',')
                for color in color_strs:
                    num, c = color.strip().split()
                    num = int(num)
                    if c == 'red' and num > red_max:
                        done = True
                        break
                    elif c == 'green' and num > green_max:
                        done = True
                        break
                    elif c == 'blue' and num > blue_max:
                        done = True
                        break
                if done:
                    break
            else:
                res += game_id
    print(res)

    res2 = 0
    with open('2.in') as f:
        for line in f.readlines():
            line = line.strip()
            game_str = line.split(':')[0]
            game_id = int(game_str.split()[1])
            pulls = line.split(':')[1].split(';')
            mins = {
                'red': 0,
                'green': 0,
                'blue': 0
            }
            done = False
            for pull in pulls:
                color_strs = pull.split(',')
                for color in color_strs:
                    num, c = color.strip().split()
                    num = int(num)
                    mins[c] = max(mins[c], num)
            temp = 1
            for color in mins:
                temp *= mins[color]
            res2 += temp
        print(res2)



if __name__ == "__main__":
    main()