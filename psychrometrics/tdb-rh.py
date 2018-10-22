import psychrometrics as psy
import sys

psychro = []

prev_ω = 100
prev_h = 1000

for t_db in range(105,31,-1):
    for rh in range(100,10,-1):
        ω = psy.ω_from_t_db_and_rh(t_db, rh/100.0)
        h = psy.h_from_t_db_and_ω(t_db, ω)
        
        ω_diff = abs(prev_ω - ω)
        h_diff = abs(prev_h - h)
        if ω > 0 and h < 60 and ω_diff > 0.00025 and h_diff > 0.25:
            prev_ω = ω
            prev_h = h
            psychro.append( (t_db, rh, ω, h))

with open(sys.argv[1], 'w+') as f:
    for page in psy.chunks(psychro,150):
        lines = []
        for i in range(0,50):
            page_length = len(page)

            if page_length == 150:
                items = list(map(lambda d: psy.print_data_to_string(d), [page[i], page[i + 50], page[i + 100]]))
            else:
                items = [psy.check_page_length(page, i), psy.check_page_length(page, i + 50), psy.check_page_length(page, i + 100)]

            all_items = items[0] + items[1] + items[2]

            line = " & ".join(all_items) + "\\\\"

            lines.append(line)

        header_instance = ["\\(T_{db}\\)", "\\(\\phi\\)", "\\(\\omega\\)", "\\(h\\)"]

        header_line = []
        header_line.extend(header_instance)
        header_line.extend(header_instance)
        header_line.extend(header_instance)

        full_header_string = " & ".join(header_line) + "  \\\\"

        formatted_lines = "\n".join(lines)
        f.write(f'\\begin{{tabular}}{{llll|llll|llll}}\n \\toprule \n{full_header_string} \\midrule \n{formatted_lines}\n\\bottomrule\n\\end{{tabular}}\n\\newpage\n')
