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
        column_width = header["size"] + 2
        top_line.append(hor_line * column_width)
    top_line = left_corner_top + top_connector.join(top_line) + right_corner_top
    return top_line


def format_headers(headers):
    headers_row = []
    for header in headers:
        column_width = header["size"] + 2
        headers_row.append(header["name"].ljust(column_width - 1).rjust(column_width))
    headers_row = vertical_line + vertical_line.join(headers_row) + vertical_line
    return headers_row


def format_bottom_line(headers):
    bottom_line = []
    for header in headers:
        column_width = header["size"] + 2
        bottom_line.append(hor_line * column_width)
    bottom_line = left_corner_bottom + bottom_connector.join(bottom_line) + right_corner_bottom
    return bottom_line


def format_separator_line(headers):
    separator_line = []
    for header in headers:
        column_width = header["size"] + 2
        separator_line.append(hor_line * column_width)
    separator_line = left_side + cross.join(separator_line) + right_side
    return separator_line



def format_data_line(data, headers):
    data_row = []
    for header in headers:
        column_width = header["size"] + 2
        data_row.append(data[header["name"]].ljust(column_width - 1).rjust(column_width))
    data_row = vertical_line + vertical_line.join(data_row) + vertical_line
    return data_row





# def format_data_line(data, headers):
#     data_row = []
#     for header in headers:
#         column_width = header["size"] 
#         data[header["name"]] = adjust_text(data[header["name"]], column_width)
#         data_row.append(data[header["name"]].ljust(column_width - 1).rjust(column_width))
#     data_row = vertical_line + vertical_line.join(data_row) + vertical_line
#     return data_row



def _data_to_string(data):
    new_data = []
    for item in data:
        new_data.append({k: str(v) for k,v in item.items()})
    return new_data



def adjust_text(string, column_width):
    new_col_width = column_width - 2 #to have a space at the beginning and at the end
    char_num_so_far=0 
    line = []
    line_to_print = []
    for word in string.split():
        if char_num_so_far + len(word) + 1 <= new_col_width:
            line.append(word)
            char_num_so_far += len(word) + 1
        else:
            char_left = new_col_width - char_num_so_far 
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
            end = new_col_width
            while length > 0:
                if length < new_col_width:
                    line.append(new_word[start:start+length])
                    char_num_so_far = length + 1
                    break
                line_to_print.append(new_word[start:end])
                length -= new_col_width
                start += new_col_width 
                end = start + new_col_width

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



# def format_lines_adjusted_to_console(data):
#     console_width = 32
#     data = _data_to_string(data)
#     headers_and_sizes = get_headers_and_sizes_from_data(data)

#     headers_and_sizes_adjusted = adjust_col_sizes_to_console(headers_and_sizes, console_width)
#     lines_to_print = []
#     lines_to_print.append(format_top_line(headers_and_sizes_adjusted))
#     lines_to_print.append(format_headers(headers_and_sizes_adjusted))
#     lines_to_print.append(format_separator_line(headers_and_sizes_adjusted))
#     for row in data[:-1]:
#         lines_to_print.append(format_data_line(row, headers_and_sizes_adjusted))
#         lines_to_print.append(format_separator_line(headers_and_sizes_adjusted))

#     lines_to_print.append(format_data_line(data[-1], headers_and_sizes_adjusted))
#     lines_to_print.append(format_bottom_line(headers_and_sizes_adjusted))
#     return lines_to_print


#IN PROGRESS
# lines = format_lines_adjusted_to_console(data)
# for line in lines:
#     line = adjust_text(line)
#     print(line)



