import streamlit as st

st.set_page_config(page_title="Pattern Explorer", layout="wide")

# --------------------- Pattern generators ---------------------

def square_pattern(rows=5):
    out = []
    for i in range(rows):
        out.append("* " * rows)
    return "\n".join(out)

def right_triangle(rows=5):
    out = []
    for i in range(1, rows + 1):
        out.append("* " * i)
    return "\n".join(out)


def inverted_right_triangle(rows=5):
    out = []
    for i in range(rows, 0, -1):
        out.append("* " * i)
    return "\n".join(out)


def pyramid(rows=5):
    out = []
    for i in range(1, rows + 1):
        out.append(" " * (rows - i) + "* " * i)
    return "\n".join(out)


def inverted_pyramid(rows=5):
    out = []
    for i in range(rows, 0, -1):
        out.append(" " * (rows - i) + "* " * i)
    return "\n".join(out)


def diamond(rows=5):
    out = []
    for i in range(1, rows + 1):
        out.append(" " * (rows - i) + "* " * i)
    for i in range(rows - 1, 0, -1):
        out.append(" " * (rows - i) + "* " * i)
    return "\n".join(out)


def hourglass(rows=5):
    out = []
    for i in range(rows, 0, -1):
        out.append(" " * (rows - i) + "* " * i)
    for i in range(2, rows + 1):
        out.append(" " * (rows - i) + "* " * i)
    return "\n".join(out)


def number_square(rows=5):
    out = []
    for i in range(1, rows + 1):
        out.append(" ".join(str(j) for j in range(1, rows + 1)))
    return "\n".join(out)


def increasing_number_triangle(rows=5):
    out = []
    for i in range(1, rows + 1):
        out.append(" ".join(str(j) for j in range(1, i + 1)))
    return "\n".join(out)


def floyds_triangle(rows=5):
    out = []
    num = 1
    for i in range(1, rows + 1):
        row = []
        for j in range(i):
            row.append(str(num))
            num += 1
        out.append(" ".join(row))
    return "\n".join(out)


def centered_number_pyramid(rows=5):
    out = []
    for i in range(1, rows + 1):
        left = "".join(str(j) for j in range(1, i + 1))
        right = "".join(str(j) for j in range(i - 1, 0, -1))
        out.append(" " * (rows - i) + left + right)
    return "\n".join(out)


def hollow_square(rows=5):
    out = []
    for i in range(rows):
        row = []
        for j in range(rows):
            if i == 0 or i == rows - 1 or j == 0 or j == rows - 1:
                row.append("*")
            else:
                row.append(" ")
        out.append(" ".join(row))
    return "\n".join(out)


def hollow_pyramid(rows=5):
    out = []
    for i in range(1, rows + 1):
        row = []
        row.append(" " * (rows - i))
        for j in range(1, 2 * i):
            if j == 1 or j == 2 * i - 1 or i == rows:
                row.append("*")
            else:
                row.append(" ")
        out.append("".join(row))
    return "\n".join(out)

hollow_pyramid_code = """
    for i in range(1, rows + 1):
        for j in range(1, rows - i + 1):
            print(" ", end="")
        for k in range(1, 2 * i):
            if k == 1 or k == 2 * i - 1 or i == rows:
                print("*", end="")
            else:
                print(" ", end="")
        print()
"""

def hollow_diamond(rows=5):
    out = []
    for i in range(1, rows + 1):
        row = []
        row.append(" " * (rows - i))
        for j in range(1, 2 * i):
            if j == 1 or j == 2 * i - 1:
                row.append("*")
            else:
                row.append(" ")
        out.append("".join(row))
    for i in range(rows - 1, 0, -1):
        row = []
        row.append(" " * (rows - i))
        for j in range(1, 2 * i):
            if j == 1 or j == 2 * i - 1:
                row.append("*")
            else:
                row.append(" ")
        out.append("".join(row))
    return "\n".join(out)

hollow_diamond_code = """
    # Upper half
    for i in range(1, rows + 1):
        print(" " * (rows - i), end="")
        for k in range(1, 2 * i):
            if k == 1 or k == 2 * i - 1:
                print("*", end="")
            else:
                print(" ", end="")
        print()
    # Lower half
    for i in range(rows - 1, 0, -1):
        print(" " * (rows - i), end="")
        for k in range(1, 2 * i):
            if k == 1 or k == 2 * i - 1:
                print("*", end="")
            else:
                print(" ", end="")
        print()
"""
def x_pattern(n):
    pattern = ""
    for i in range(n+1):
        for j in range(n):
            if j == i or j == n - i - 1:
                pattern += "*"
            else:
                pattern += " "
        pattern += "\n"
    return pattern

x_pattern_code = '''
    for i in range(n+1):
        for j in range(n):
            if j == i or j == n - i - 1:
                print("*", end="")
            else:
                print(" ", end="")
        print()
'''
def pascals_triangle(rows=5):
    out = []
    for i in range(rows):
        row_elems = []
        num = 1
        for j in range(i + 1):
            row_elems.append(str(num))
            num = num * (i - j) // (j + 1)
        out.append(" ".join(row_elems).center(rows * 2))
    return "\n".join(out)

# A dictionary mapping titles to generator functions and a small code snippet to display
PATTERNS = {
    "Square (stars)": (square_pattern, "rows = 5\nfor i in range(rows):\n    print('* ' * rows)"),
    "Right-Angled Triangle": (right_triangle, "rows = 5\nfor i in range(1, rows + 1):\n    print('* ' * i)"),
    "Inverted Right Triangle": (inverted_right_triangle, "rows = 5\nfor i in range(rows, 0, -1):\n    print('* ' * i)"),
    "Pyramid": (pyramid, "rows = 5\nfor i in range(1, rows + 1):\n    print(' ' * (rows - i) + '* ' * i)"),
    "Inverted Pyramid": (inverted_pyramid, "rows = 5\nfor i in range(rows, 0, -1):\n    print(' ' * (rows - i) + '* ' * i)"),
    "Diamond": (diamond, "rows = 5\nfor i in range(1, rows + 1):\n    print(' ' * (rows - i) + '* ' * i)\nfor i in range(rows - 1, 0, -1):\n    print(' ' * (rows - i) + '* ' * i)"),
    "Hourglass": (hourglass, "# hourglass pattern code..."),
    "X Pattern": (x_pattern, x_pattern_code),
    "Number: Square": (number_square, "rows = 5\nfor i in range(1, rows + 1):\n    print(' '.join(str(j) for j in range(1, rows + 1)))"),
    "Number: Increasing Triangle": (increasing_number_triangle, "rows = 5\nfor i in range(1, rows + 1):\n    print(' '.join(str(j) for j in range(1, i + 1)))"),
    "Number: Floyd's Triangle": (floyds_triangle, "rows = 5\nnum = 1\nfor i in range(1, rows + 1):\n    for j in range(i):\n        print(num, end=' ')\n        num += 1\n    print()"),
    "Centered Number Pyramid": (centered_number_pyramid, "rows = 5\nfor i in range(1, rows + 1):\n    print(' ' * (rows - i), end='')\n    for j in range(1, i + 1):\n        print(j, end='')\n    for j in range(i - 1, 0, -1):\n        print(j, end='')\n    print()"),
    "Hollow: Square": (hollow_square, "rows = 5\nfor i in range(rows):\n    for j in range(rows):\n        if i == 0 or i == rows - 1 or j == 0 or j == rows - 1:\n            print('*', end=' ')\n        else:\n            print(' ', end=' ')\n    print()"),
    "Hollow Pyramid": (hollow_pyramid, hollow_pyramid_code),
    "Hollow Diamond": (hollow_diamond, hollow_diamond_code),
    "Pascal's Triangle": (pascals_triangle, "rows = 5\nfor i in range(rows):\n    num = 1\n    for j in range(i + 1):\n        print(num, end=' ')\n        num = num * (i - j) // (j + 1)\n    print()")
}


# --------------------- Streamlit UI ---------------------

st.title("Pattern Explorer — Streamlit")
st.write("Choose a pattern on the left. The pattern output and the source code appear side-by-side.")

with st.sidebar:
    st.header("Controls")
    pattern_name = st.selectbox("Select pattern", list(PATTERNS.keys()))
    rows = st.slider("Rows / Size", min_value=1, max_value=20, value=6)
    show_code = st.checkbox("Show code", value=True)
    download_code = st.checkbox("Provide download button for code", value=True)
    monospace = st.checkbox("Use monospace font for output", value=True)

# Generate output
generator, code_snippet = PATTERNS[pattern_name]
pattern_output = generator(rows)

# Layout: side-by-side
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("Pattern Output")
    if monospace:
        st.code(pattern_output, language='text')
    else:
        st.text(pattern_output)

with col2:
    st.subheader("Source Code")
    if show_code:
        st.code(code_snippet, language='python')
        if download_code:
            st.download_button(label="Download code (.py)",
                               data=code_snippet,
                               file_name=f"{pattern_name.replace(' ', '_')}.py",
                               mime='text/x-python')
    else:
        st.info("Code hidden. Check 'Show code' in the sidebar to view it.")

st.markdown("---")
st.caption("Tip: Increase rows to see larger patterns. Use the download button to save snippets.")

# Footer: show combined file download (full app) if requested
if st.sidebar.button("Download full app file"):
    with open(__file__, 'r', encoding='utf-8') as f:
        code_all = f.read()
    st.download_button("Download app file", data=code_all, file_name="streamlit_patterns_app.py", mime='text/x-python')
