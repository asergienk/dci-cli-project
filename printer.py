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
    headers_and_sizes = []
    for item in data:
        for key, value in item.items():
            size = max(map(lambda x:len(x[key]), data))
            if len(key) > size:
                size = len(key)
            headers_and_sizes.append({"size": size, "name": key})
        break
    return headers_and_sizes


def adjust_column_width_to_console(headers, console_width):
    sum_of_sizes = 0

    for item in headers:
        sum_of_sizes += int(item["size"])

    for item in headers:
        item["size"] = int(console_width * (int(item["size"])/sum_of_sizes))

    return headers


def format_line(headers, line_position):
    line = []
    for header in headers:
        column_width = header["size"] 
        line.append(hor_line * column_width)
    if line_position == "top":
        line = left_corner_top + top_connector.join(line) + right_corner_top
    if line_position == "separator":
        line = left_side + cross.join(line) + right_side
    if line_position == "bottom":
        line = left_corner_bottom + bottom_connector.join(line) + right_corner_bottom
    return line


def split_strings(data_row):
    substrings = []
    for string in data_row:
        substrings.append(string.split("\n"))
    return substrings


def create_line_content(substrings):
    lines = []
    line = []
    max_length = max([len(item) for item in substrings])
    i = 0
    while max_length > 0:
        for item in substrings:
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


def format_data_line(row, headers):
    data_row = []
    for header in headers:
        string_width = header["size"] - 2 
        data_row.append(adjust_text(row[header["name"]], string_width)) 
    substrings = split_strings(data_row) 
    data_line = format_text(headers, substrings)
    return data_line
    

def format_headers_line(headers):
    headers_row = []
    for header in headers:
        string_width = header["size"] - 2
        headers_row.append(adjust_text(header["name"], string_width))
    substrings = split_strings(headers_row)
    headers_line = format_text(headers, substrings)
    return headers_line
    

def format_text(headers, substrings):
    headers_sizes = [header["size"] for header in headers]
    row_to_print = []
    final_data = []
    line = create_line_content(substrings) 
    for item in line:
        i = 0
        for string in item:
            column_width = headers_sizes[i]
            row_to_print.append(string.ljust(column_width - 1).rjust(column_width))
            i += 1
        final_data.append(vertical_line + vertical_line.join(row_to_print) + vertical_line) 
        row_to_print = []
    return final_data 
    


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
 


def format_lines_adjusted_to_console(data, console_width):
    data = _data_to_string(data)
    headers_and_sizes = get_headers_and_sizes_from_data(data)
    headers_and_sizes_adjusted = adjust_column_width_to_console(headers_and_sizes, console_width)

    lines_to_print = []
    lines_to_print.append(format_line(headers_and_sizes_adjusted, "top"))
    headers_line = format_headers_line(headers_and_sizes_adjusted)
    for string in headers_line:
        lines_to_print.append(string)
    lines_to_print.append(format_line(headers_and_sizes_adjusted, "separator"))
    
    for row in data[:-1]:
        data_line = format_data_line(row, headers_and_sizes_adjusted)
        for string in data_line:
            lines_to_print.append(string)
        lines_to_print.append(format_line(headers_and_sizes_adjusted, "separator"))

    data_last_row = format_data_line(data[-1], headers_and_sizes_adjusted)
    for string in data_last_row:
        lines_to_print.append(string)
    lines_to_print.append(format_line(headers_and_sizes_adjusted, "bottom"))
    return lines_to_print




data = [
        {
            "id": "6018975a-dde7-4666-9436-b171c5a11dde",
            "name": "Jonh Doe",
            "email": "jdoe@example.org",
        },
    ]

lines = format_lines_adjusted_to_console(data, 32)
for line in lines:
    print(line)

