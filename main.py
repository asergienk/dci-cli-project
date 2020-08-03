from printer import format_lines_adjusted_to_console
from printer import printer

if __name__ == "__main__":
    data = [
        {
            "id": "6018975a-dde7-4666-9436-b171c5a11dde",
            "name": "Jonh Doe",
            "email": "jdoe@example.org",
        },
        # {
        #     "id": "f05b3da7-701b-40bd-87e8-780693a07b13",
        #     "name": "Bob Dylan",
        #     "email": "bdylan@example.org",
        # },
    ]
    # lines = format_lines_adjusted_to_console(data, options)
    # printer(lines)

    
    lines = format_lines_adjusted_to_console(data)
    printer(lines)

   