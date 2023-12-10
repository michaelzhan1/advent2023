def main():
    res = 0
    with open('4.in') as f:
        for line in f.readlines():
            line = line.strip()
            all_nums = line.split(':')[1]
            wins = all_nums.split('|')[0].split()
            mine = all_nums.split('|')[1].split()
            wins = set(wins)
            score = 0
            for n in mine:
                if n in wins:
                    if score == 0:
                        score += 1
                    else:
                        score *= 2
            res += score
    print(res)
    
    res2 = 0
    multiplier = {}
    with open('4.in') as f:
        for line in f.readlines():
            line = line.strip()
            card_num = line.split(':')[0].split()[1]
            all_nums = line.split(':')[1]
            wins = all_nums.split('|')[0].split()
            mine = all_nums.split('|')[1].split()
            wins = set(wins)
            if card_num not in multiplier:
                multiplier[card_num] = 1
            else:
                multiplier[card_num] += 1
            num_wins = 0
            for n in mine:
                if n in wins:
                    num_wins += 1
            for i in range(int(card_num) + 1, int(card_num) + 1 + num_wins):
                i = str(i)
                if i not in multiplier:
                    multiplier[i] = multiplier[card_num]
                else:
                    multiplier[i] += multiplier[card_num]
            res2 += multiplier[card_num]
    print(res2)


if __name__ == "__main__":
    main()