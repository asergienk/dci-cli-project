from printer import get_headers_and_sizes_from_data
from printer import format_top_line
from printer import format_headers
from printer import format_bottom_line
from printer import format_separator_line
from printer import format_data_line
from printer import format_lines


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
    assert format_top_line(headers_and_sizes) == "┌───────┬───────┬───────┐"

    headers_and_sizes = [
        { "size": 5, "name": "id"} ,
        { "size": 10, "name": "name"} ,
        { "size": 5, "name": "email"} ,
    ]
    assert format_top_line(headers_and_sizes) == "┌───────┬────────────┬───────┐"


def test_headers_line():
    headers_and_sizes = [
        { "size": 5, "name": "id"} ,
        { "size": 5, "name": "name"} ,
        { "size": 5, "name": "email"} ,
    ]
    assert format_headers(headers_and_sizes) == "│ id    │ name  │ email │"

    headers_and_sizes = [
        { "size": 10, "name": "id"} ,
        { "size": 5, "name": "name"} ,
        { "size": 5, "name": "email"} ,
    ]
    assert format_headers(headers_and_sizes) == "│ id         │ name  │ email │"
    

def test_format_bottom_line():
    headers_and_sizes = [
        { "size": 5, "name": "id"} ,
        { "size": 5, "name": "name"} ,
        { "size": 5, "name": "email"} ,
    ]
    assert format_bottom_line(headers_and_sizes) == "└───────┴───────┴───────┘"

    headers_and_sizes = [
        { "size": 5, "name": "id"} ,
        { "size": 10, "name": "name"} ,
        { "size": 5, "name": "email"} ,
    ]
    assert format_bottom_line(headers_and_sizes) == "└───────┴────────────┴───────┘"


def test_format_separator_line():
    headers_and_sizes = [
        { "size": 5, "name": "id"} ,
        { "size": 5, "name": "name"} ,
        { "size": 5, "name": "email"} ,
    ]
    assert format_separator_line(headers_and_sizes) == "├───────┼───────┼───────┤"

    headers_and_sizes = [
        { "size": 5, "name": "id"} ,
        { "size": 10, "name": "name"} ,
        { "size": 5, "name": "email"} ,
    ]
    assert format_separator_line(headers_and_sizes) == "├───────┼────────────┼───────┤"


def test_format_data_line():
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
    assert format_data_line(data[0], headers) == "│ 6018975a-dde7-4666-9436-b171c5a11dde │ Jonh Doe  │ jdoe@example.org   │"


def test_format_lines():
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
    
    assert format_lines(data) == [
        "┌──────────────────────────────────────┬───────────┬────────────────────┐",
        "│ id                                   │ name      │ email              │",
        "├──────────────────────────────────────┼───────────┼────────────────────┤",
        "│ 6018975a-dde7-4666-9436-b171c5a11dde │ Jonh Doe  │ jdoe@example.org   │",
        "├──────────────────────────────────────┼───────────┼────────────────────┤",
        "│ f05b3da7-701b-40bd-87e8-780693a07b13 │ Bob Dylan │ bdylan@example.org │",
        "└──────────────────────────────────────┴───────────┴────────────────────┘",
    ]
