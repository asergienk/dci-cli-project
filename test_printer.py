from printer import get_headers_and_sizes_from_data
from printer import format_top_line
from printer import format_headers
from printer import format_bottom_line
from printer import format_separator_line
from printer import format_data_line
from printer import format_lines
from printer import adjust_col_sizes_to_console
from printer import adjust_text
from printer import get_num_of_lines
from printer import split_strings
from printer import create_line_content
from printer import format_text_to_width
from printer import format_lines_adjusted_to_console



def test_get_headers_and_sizes_from_data():
    data = [
        {
            "id": "6018975a-dde7-4666-9436-b171c5a11dde",
            "name": "Jonh Doe",
            "email": "jdoe@example.org",
        },
        {
            "id": "f05b3da7-701b-40bd-87e8-780693a07b13",
            "name": "Bob Dylan",
            "email": "bdylan@example.org",
        },
    ]

    expected_headers = [
        { "size": 36, "name": "id" },
        { "size": 9, "name": "name" },
        { "size": 18, "name": "email" },
    ]
    assert get_headers_and_sizes_from_data(data) == expected_headers


def test_format_top_line():
    headers_and_sizes = [
        { "size": 5, "name": "id"} ,
        { "size": 5, "name": "name"} ,
        { "size": 5, "name": "email"} ,
    ]
    assert format_top_line(headers_and_sizes) == "┌─────┬─────┬─────┐"

    headers_and_sizes = [
        { "size": 5, "name": "id"} ,
        { "size": 10, "name": "name"} ,
        { "size": 5, "name": "email"} ,
    ]
    assert format_top_line(headers_and_sizes) == "┌─────┬──────────┬─────┐"


# def test_headers_line():
#     headers_and_sizes = [
#         { "size": 5, "name": "id"} ,
#         { "size": 5, "name": "name"} ,
#         { "size": 5, "name": "email"} ,
#     ]
#     assert format_headers(headers_and_sizes) == "│ id    │ name  │ email │"

#     headers_and_sizes = [
#         { "size": 10, "name": "id"} ,
#         { "size": 5, "name": "name"} ,
#         { "size": 5, "name": "email"} ,
#     ]
#     assert format_headers(headers_and_sizes) == "│ id         │ name  │ email │"
    

def test_format_bottom_line():
    headers_and_sizes = [
        { "size": 5, "name": "id"} ,
        { "size": 5, "name": "name"} ,
        { "size": 5, "name": "email"} ,
    ]
    assert format_bottom_line(headers_and_sizes) == "└─────┴─────┴─────┘"

    headers_and_sizes = [
        { "size": 5, "name": "id"} ,
        { "size": 10, "name": "name"} ,
        { "size": 5, "name": "email"} ,
    ]
    assert format_bottom_line(headers_and_sizes) == "└─────┴──────────┴─────┘"


def test_format_separator_line():
    headers_and_sizes = [
        { "size": 5, "name": "id"} ,
        { "size": 5, "name": "name"} ,
        { "size": 5, "name": "email"} ,
    ]
    assert format_separator_line(headers_and_sizes) == "├─────┼─────┼─────┤"

    headers_and_sizes = [
        { "size": 5, "name": "id"} ,
        { "size": 10, "name": "name"} ,
        { "size": 5, "name": "email"} ,
    ]
    assert format_separator_line(headers_and_sizes) == "├─────┼──────────┼─────┤"


# def test_format_data_line():
#     data = [
#         {
#             "id": "6018975a-dde7-4666-9436-b171c5a11dde",
#             "name": "Jonh Doe",
#             "email": "jdoe@example.org",
#         },
#         {
#             "id": "f05b3da7-701b-40bd-87e8-780693a07b13",
#             "name": "Bob Dylan",
#             "email": "bdylan@example.org",
#         },
#     ]
#     headers = get_headers_and_sizes_from_data(data)

#     assert format_data_line(data[0], headers) == "│ 6018975a-dde7-4666-9436-b171c5a11dde │ Jonh Doe  │ jdoe@example.org   │"


# def test_format_lines():
#     data = [
#         {
#             "id": "6018975a-dde7-4666-9436-b171c5a11dde",
#             "name": "Jonh Doe",
#             "email": "jdoe@example.org",
#         },
#         {
#             "id": "f05b3da7-701b-40bd-87e8-780693a07b13",
#             "name": "Bob Dylan",
#             "email": "bdylan@example.org",
#         },
#     ]
    
#     assert format_lines(data) == [
#         "┌──────────────────────────────────────┬───────────┬────────────────────┐",
#         "│ id                                   │ name      │ email              │",
#         "├──────────────────────────────────────┼───────────┼────────────────────┤",
#         "│ 6018975a-dde7-4666-9436-b171c5a11dde │ Jonh Doe  │ jdoe@example.org   │",
#         "├──────────────────────────────────────┼───────────┼────────────────────┤",
#         "│ f05b3da7-701b-40bd-87e8-780693a07b13 │ Bob Dylan │ bdylan@example.org │",
#         "└──────────────────────────────────────┴───────────┴────────────────────┘",
#     ]


# def test_format_lines_with_int():
#     data = [
#         {
#             "name": "Jonh Doe",
#             "age": 32,
#         }
#     ]
#     assert format_lines(data) ==  [
#         "┌──────────┬─────┐",
#         "│ name     │ age │",
#         "├──────────┼─────┤",
#         "│ Jonh Doe │ 32  │",
#         "└──────────┴─────┘",
#     ]


def test_adjust_col_sizes_to_console():
    data = [
        { "size": 36, "name": "id" },
        { "size": 9, "name": "name" },
        { "size": 18, "name": "email" },
    ]

    expected_headers = [
        { "size": 18, "name": "id" },
        { "size": 4, "name": "name" },
        { "size": 9, "name": "email" },
    ]

    assert adjust_col_sizes_to_console(data, console_width=32) == expected_headers


    data = [
        { "size": 36, "name": "id" },
        { "size": 9, "name": "name" },
        { "size": 18, "name": "email" },
    ]

    expected_headers = [
        { "size": 26, "name": "id" },
        { "size": 6, "name": "name" },
        { "size": 13, "name": "email" },
    ]

    assert adjust_col_sizes_to_console(data, console_width=46) == expected_headers


def test_adjust_text():
    string = "Jonh Doe"
    assert adjust_text(string, column_width=5) == 'Jonh\nDoe'

    string = "6018975a-dde7-4666-9436-b171c5a11dde"    
    assert adjust_text(string, column_width=7) == '6018975\na-dde7-\n4666-94\n36-b171\nc5a11dd\ne'


def test_split_strings():
    data = ['6018975a-dde7-46\n66-9436-b171c5a1\n1dde', 'Jo\nnh\nDo\ne', 'jdoe@ex\nample.o\nrg']
    
    expected = [['6018975a-dde7-46', '66-9436-b171c5a1', '1dde'], ['Jo', 'nh', 'Do', 'e'], ['jdoe@ex', 'ample.o', 'rg']]
    
    assert split_strings(data) == expected


def test_create_line_content():
    data = [['6018975a-dde7-46', '66-9436-b171c5a1', '1dde'], ['Jo', 'nh', 'Do', 'e'], ['jdoe@ex', 'ample.o', 'rg']]
    
    expected = [['6018975a-dde7-46', 'Jo', 'jdoe@ex'], ['66-9436-b171c5a1', 'nh', 'ample.o'], ['1dde', 'Do', 'rg'], [' ', 'e', ' ']]
    
    assert create_line_content(data) == expected


def test_format_text_to_width():
    data = [
                {
                    "id": "6018975a-dde7-4666-9436-b171c5a11dde",
                    "name": "Jonh Doe",
                    "email": "jdoe@example.org",
                },
            ]    
    headers = get_headers_and_sizes_from_data(data)
    adjusted_headers = adjust_col_sizes_to_console(headers, console_width=32)

    assert format_text_to_width(data[0], adjusted_headers) == [['6018975a-dde7-466', '6-9436-b171c5a11d', 'de'], ['Jo', 'nh', 'Do', 'e'], ['jdoe@e', 'xample', '.org']]
    
    data = [
        {
            "id": "6018975a-dde7-4666-9436-b171c5a11dde",
            "name": "Jonh Doe",
            "email": "jdoe@example.org",
        },
        {
            "id": "f05b3da7-701b-40bd-87e8-780693a07b13",
            "name": "Bob Dylan",
            "email": "bdylan@example.org",
        },
    ]
    headers = get_headers_and_sizes_from_data(data)
    adjusted_headers = adjust_col_sizes_to_console(headers, console_width=32)
    
    assert format_text_to_width(data[1], adjusted_headers) == [['f05b3da7-701b-40', 'bd-87e8-780693a0', '7b13'], ['Bo', 'b', 'Dy', 'la', 'n'], ['bdylan@', 'example', '.org']]

def test_format_data_line():
    data = [
            {
                "id": "6018975a-dde7-4666-9436-b171c5a11dde",
                "name": "Jonh Doe",
                "email": "jdoe@example.org",
            },
        ]
    headers = get_headers_and_sizes_from_data(data)
    adjusted_headers = adjust_col_sizes_to_console(headers, console_width=32)

    assert format_data_line(data[0],adjusted_headers) == ['│ 6018975a-dde7-466 │ Jo │ jdoe@e │', '│ 6-9436-b171c5a11d │ nh │ xample │', '│ de                │ Do │ .org   │', '│                   │ e  │        │']