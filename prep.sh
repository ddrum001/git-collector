# replace newlines in double quotes
gawk -v RS='"' 'NR % 2 == 0 { gsub(/\n/, "") } { printf("%s%s", $0, RT) }' sample.csv > s1.csv
