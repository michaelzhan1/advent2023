if [ $# -ne 1 ]; then
    echo "Usage: $0 <day_number>"
    exit 1
fi

day=$1
mkdir -p $day
cd $day
touch test.in
touch $day.py
touch $day.in

cat > $day.py << EOF
fname = 'test.in'


def part1():
    with open(fname) as f:
        all_lines = f.read()


def part2():
    with open(fname) as f:
        all_lines = f.read()


if __name__ == '__main__':
    part1()
    part2()

EOF