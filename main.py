from printer import format_lines_adjusted_to_console
from printer import printer

if __name__ == "__main__":
    
    
    def _sort_headers(headers):
        """Ensure the column order is always the same."""
        headers = set(headers)
        default_order = ["id", "name", "email"]
        sorted_headers = []
        for i in default_order:
            if i not in headers:
                continue
            headers.remove(i)
            sorted_headers.append(i)
        sorted_headers += sorted(headers)
        return sorted_headers


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
    
    headers = data[0].keys()
    headers = _sort_headers(headers)
    lines = format_lines_adjusted_to_console(data, headers)
    printer(lines)



