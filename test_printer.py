from printer import get_headers_and_sizes_from_data
from printer import format_top_line
from printer import format_headers
from printer import format_bottom_line
from printer import format_separator_line
from printer import format_data_line
from printer import adjust_col_sizes_to_console
from printer import adjust_text
from printer import split_strings
from printer import create_line_content
from printer import format_text_to_width
from printer import format_lines_adjusted_to_console
from printer import format_text



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


def test_format_text():
    headers = [
        { "size": 18, "name": "id" },
        { "size": 4, "name": "name" },
        { "size": 9, "name": "email" },
    ]
    splitted_strings =  [['id'], ['na', 'me'], ['email']]
    assert format_text(headers, splitted_strings) == ['│ id               │ na │ email   │', '│                  │ me │         │']


    headers = [
        { "size": 18, "name": "id" },
        { "size": 4, "name": "name" },
        { "size": 9, "name": "email" },
    ]
    splitted_strings =  [['6018975a-dde7-46', '66-9436-b171c5a1', '1dde'], ['Jo', 'nh', 'Do', 'e'], ['jdoe@ex', 'ample.o', 'rg']]
    assert format_text(headers, splitted_strings) == ['│ 6018975a-dde7-46 │ Jo │ jdoe@ex │', '│ 66-9436-b171c5a1 │ nh │ ample.o │', '│ 1dde             │ Do │ rg      │', '│                  │ e  │         │']



def test_format_headers():
    headers = [
        { "size": 18, "name": "id" },
        { "size": 4, "name": "name" },
        { "size": 9, "name": "email" },
    ]
    expected = ["│ id               │ na │ email   │", "│                  │ me │         │"]

    assert format_headers(headers) == expected


def test_format_lines_adjusted_to_console():
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

    expected = [
        "┌──────────────────┬────┬─────────┐",
        "│ id               │ na │ email   │",
        "│                  │ me │         │",
        "├──────────────────┼────┼─────────┤",
        "│ 6018975a-dde7-46 │ Jo │ jdoe@ex │",
        "│ 66-9436-b171c5a1 │ nh │ ample.o │",
        "│ 1dde             │ Do │ rg      │",
        "│                  │ e  │         │",
        "├──────────────────┼────┼─────────┤",
        "│ f05b3da7-701b-40 │ Bo │ bdylan@ │",
        "│ bd-87e8-780693a0 │ b  │ example │",
        "│ 7b13             │ Dy │ .org    │",
        "│                  │ la │         │",
        "│                  │ n  │         │",
        "└──────────────────┴────┴─────────┘",
    ]
    assert format_lines_adjusted_to_console(data, console_width=32) == expected

    data = [
        {
            "id": "6018975a-dde7-4666-9436-b171c5a11dde",
            "name": "Jonh Doe",
            "email": "jdoe@example.org",
        },
    ]
    expected = [
        "┌─────────────────────────┬─────┬───────────┐",
        "│ id                      │ nam │ email     │",
        "│                         │ e   │           │",
        "├─────────────────────────┼─────┼───────────┤",
        "│ 6018975a-dde7-4666-9436 │ Jon │ jdoe@exam │",
        "│ -b171c5a11dde           │ h D │ ple.org   │",
        "│                         │ oe  │           │",
        "└─────────────────────────┴─────┴───────────┘",
    ]
    assert format_lines_adjusted_to_console(data, console_width=42) == expected