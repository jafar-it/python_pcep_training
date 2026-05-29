# Build a flexible report-generation system

def format_row(*values, sep=" | ", padding=12) -> str:
    return sep.join(str(v)[:padding].ljust(padding) for v in values)

def print_table(headers, *rows, title=None, **style):
    border_char = style.get("border_char", "=")
    header_sep  = style.get("header_sep", "-")
    width = ((14 * len(headers)) + (3 * (len(headers) - 1)))

    if title:
        print(border_char * width)
        print(title.center(width))
    print(border_char * width)
    print(format_row(*headers))
    print(header_sep * width)
    for row in rows:
        print(format_row(*row))
    print(border_char * width)

def generate_report(data, *fields, title="Report", **options):
    sort_by = options.get("sort_by")
    if sort_by:
        data = sorted(data, key=lambda r: r.get(sort_by, 0),
                       reverse=options.get("desc", False))
    rows = [tuple(str(r.get(f, "—")) for f in fields) for r in data]
    print_table(list(fields), *rows, title=title,
                border_char=options.get("border_char", "="))

# Test
sales = [
    {"rep": "Alice", "region": "North", "q1": 120000, "q2": 145000},
    {"rep": "Bob",   "region": "South", "q1": 98000,  "q2": 110000},
    {"rep": "Carol", "region": "East",  "q1": 175000, "q2": 162000},
]
generate_report(sales, "rep", "region", "q1", "q2",
                title="Sales Report Q1-Q2", sort_by="q2", desc=True)