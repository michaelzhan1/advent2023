def main():
    res = 0
    with open('4.in') as f:
        for line in f.readlines():
            line = line.strip()
            all_nums = line.split(':')[1]
            wins = all_nums.split('|')[0].split()
            loses = all_nums.split('|')[1].split()
            wins = set(wins)
            score = 0
            for n in loses:
                if n in wins:
                    if score == 0:
                        score += 1
                    else:
                        score *= 2
            res += score
    print(res)
    
    res2 = 0
    card_counts = {}
    count_total = 0
    with open('4.in') as f:
        for line in f.readlines():
            count_total += 1
            line = line.strip()
            card_num = line.split(':')[0].split()[1]
            all_nums = line.split(':')[1]
            wins = all_nums.split('|')[0].split()
            loses = all_nums.split('|')[1].split()
            wins = set(wins)
            if card_num not in card_counts:
                card_counts[card_num] = 1
            else:
                card_counts[card_num] += 1
            num_wins = 0
            for n in loses:
                if n in wins:
                    num_wins += 1
            for i in range(int(card_num) + 1, int(card_num) + 1 + num_wins):
                if str(i) in card_counts:
                    card_counts[str(i)] += 1 * card_counts[card_num]
                else:
                    card_counts[str(i)] = 1 * card_counts[card_num]
            print(card_counts)
    for card in card_counts:
        if int(card) > count_total:
            break
        res2 += card_counts[card]
    print(res2)


if __name__ == "__main__":
    main()