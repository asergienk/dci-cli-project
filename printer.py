hor_line = u'\u2500'
left_corner_top = u'\u250C'
right_corner_top = u'\u2510'
left_side = u'\u251C'
right_side = u'\u2524'
top_connector = u'\u252C'
bottom_connector = u'\u2534'
cross = u'\u253C'
left_corner_bottom = u'\u2514'
right_corner_bottom = u'\u2518'
vertical_line = u'\u2502'


def get_headers_and_sizes_from_data(data):
    key_size_list = []
    for item in data:
        for key, value in item.items():
            size = max(map(lambda x:len(x[key]), data))
            if len(key) > size:
                size = len(key)
            key_size_list.append({"size": size, "name": key})
        break
    return key_size_list


def adjust_col_sizes_to_console(key_size_list, console_width):
    i = 0
    sum_of_sizes = 0
    proportions = []
    for item in key_size_list:
        sum_of_sizes += int(item["size"])

    for item in key_size_list:
        proportions.append(int(item["size"])/sum_of_sizes)
        item["size"] = (int(console_width * proportions[i]))
        i += 1

    return key_size_list


def format_top_line(headers):
    top_line = []
    for header in headers:
        column_width = header["size"] 
        top_line.append(hor_line * column_width)
    top_line = left_corner_top + top_connector.join(top_line) + right_corner_top
    return top_line


def format_bottom_line(headers):
    bottom_line = []
    for header in headers:
        column_width = header["size"] 
        bottom_line.append(hor_line * column_width)
    bottom_line = left_corner_bottom + bottom_connector.join(bottom_line) + right_corner_bottom
    return bottom_line


def format_separator_line(headers):
    separator_line = []
    for header in headers:
        column_width = header["size"] 
        separator_line.append(hor_line * column_width)
    separator_line = left_side + cross.join(separator_line) + right_side
    return separator_line


def split_strings(data_row):
    splitted_strings = []
    for string in data_row:
        splitted_strings.append(string.split("\n"))
    return splitted_strings


def create_line_content(splitted_strings):
    lines = []
    line = []
    max_length = max([len(item) for item in splitted_strings])
    i = 0
    while max_length > 0:
        for item in splitted_strings:
                try:
                    line.append(item[i])
                except IndexError:
                    line.append(" ")
                continue
        lines.append(line)
        line = []
        max_length -= 1
        i += 1

    return lines


def format_text_to_width(row, headers):
    data_row = []
    for header in headers:
        string_width = header["size"] - 2 # to have 2 spaces
        data_row.append(adjust_text(row[header["name"]], string_width)) #['6018975a-dde7-46\n66-9436-b171c5a1\n1dde', 'Jo\nnh\nDo\ne', 'jdoe@ex\nample.o\nrg']
    splitted_strings = split_strings(data_row) # [['6018975a-dde7-46', '66-9436-b171c5a1', '1dde'], ['Jo', 'nh', 'Do', 'e'], ['jdoe@ex', 'ample.o', 'rg']]
    return splitted_strings


def format_data_line(row, headers):
    headers_sizes = [header["size"] for header in headers]
    row_to_print = []
    final_data = []
    splitted_strings = format_text_to_width(row, headers)# [['6018975a-dde7-46', '66-9436-b171c5a1', '1dde'], ['Jo', 'nh', 'Do', 'e'], ['jdoe@ex', 'ample.o', 'rg']]
    
    line = create_line_content(splitted_strings) #[['6018975a-dde7-46', 'Jo', 'jdoe@ex'], ['66-9436-b171c5a1', 'nh', 'ample.o'], ['1dde', 'Do', 'rg'], [' ', 'e', ' ']]
    for item in line:
        i = 0
        for string in item:
            column_width = headers_sizes[i]
            row_to_print.append(string.ljust(column_width - 1).rjust(column_width))
            i += 1
        final_data.append(vertical_line + vertical_line.join(row_to_print) + vertical_line) #│ 6018975a-dde7-46 │ Jo │ jdoe@ex │
        row_to_print = []
    return final_data #['│ 6018975a-dde7-46 │ Jo │ jdoe@ex │', '│ 66-9436-b171c5a1 │ nh │ ample.o │', '│ 1dde             │ Do │ rg      │', '│                  │ e  │         │']



def format_headers(headers):
    headers_row = []
    for header in headers:
        column_width = header["size"] 
        headers_row.append(header["name"].ljust(column_width - 1).rjust(column_width))
    headers_row = vertical_line + vertical_line.join(headers_row) + vertical_line
    return headers_row



def _data_to_string(data):
    new_data = []
    for item in data:
        new_data.append({k: str(v) for k,v in item.items()})
    return new_data



def adjust_text(string, column_width):
    char_num_so_far=0 
    line = []
    line_to_print = []
    for word in string.split():
        if char_num_so_far + len(word) + 1 <= column_width:
            line.append(word)
            char_num_so_far += len(word) + 1
        else:
            char_left = column_width - char_num_so_far 
            if char_left == 1:
                line.append(word[char_left-1])
            if char_left > 1:
                line.append(word[:char_left])
            line_to_print.append(" ".join(line))
            char_num_so_far = 0
            line = []
            new_word = word[char_left:]
            length = len(new_word)
            start = 0
            end = column_width
            while length > 0:
                if length < column_width:
                    line.append(new_word[start:start+length])
                    char_num_so_far = length + 1
                    break
                line_to_print.append(new_word[start:end])
                length -= column_width
                start += column_width 
                end = start + column_width

    if line: 
        line_to_print.append(" ".join(line))
    
    return "\n".join(line_to_print)
 


def format_lines(data):
    data = _data_to_string(data)
    headers_and_sizes = get_headers_and_sizes_from_data(data)
    lines_to_print = []
    lines_to_print.append(format_top_line(headers_and_sizes))
    lines_to_print.append(format_headers(headers_and_sizes))
    lines_to_print.append(format_separator_line(headers_and_sizes))
    for row in data[:-1]:
        lines_to_print.append(format_data_line(row, headers_and_sizes))
        lines_to_print.append(format_separator_line(headers_and_sizes))

    lines_to_print.append(format_data_line(data[-1], headers_and_sizes))
    lines_to_print.append(format_bottom_line(headers_and_sizes))
    return lines_to_print



def format_lines_adjusted_to_console(data):
    console_width = 32
    data = _data_to_string(data)
    headers_and_sizes = get_headers_and_sizes_from_data(data)
    headers_and_sizes_adjusted = adjust_col_sizes_to_console(headers_and_sizes, console_width)

    lines_to_print = []
    lines_to_print.append(format_top_line(headers_and_sizes_adjusted))
    #lines_to_print.append(format_headers(headers_and_sizes_adjusted))
    lines_to_print.append(format_separator_line(headers_and_sizes_adjusted))
    for row in data:
        data_line = format_data_line(row, headers_and_sizes_adjusted)#['│ 6018975a-dde7-46 │ Jo │ jdoe@ex │', '│ 66-9436-b171c5a1 │ nh │ ample.o │', '│ 1dde             │ Do │ rg      │', '│                  │ e  │         │']
        for string in data_line:
            lines_to_print.append(string)
    #lines_to_print.append(format_separator_line(headers_and_sizes_adjusted))

    #lines_to_print.append(format_data_line(data, headers_and_sizes_adjusted))
    lines_to_print.append(format_bottom_line(headers_and_sizes_adjusted))
    return lines_to_print




data = [
    {
        "id": "6018975a-dde7-4666-9436-b171c5a11dde",
        "name": "Jonh Doe",
        "email": "jdoe@example.org",
    },
    ]

lines = format_lines_adjusted_to_console(data)
for line in lines:
    print(line)

