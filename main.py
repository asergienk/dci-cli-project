import shutil
from printer import format_lines_adjusted_to_console
from printer import printer

if __name__ == "__main__":
    data = [
        {
            "id": "6018975a-dde7-4666-9436-b171c5a11dde",
            "name": "Jonh Doe",
            "email": "jdoe@example.org",
        },
    ]

    console_width, rows = shutil.get_terminal_size()
    lines = format_lines_adjusted_to_console(data, console_width, "id", "name")
    printer(lines)
