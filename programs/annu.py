def print_pattern(text):
    # Define patterns for letters
    patterns = {
        "A": ["  *  ",
              " * * ",
              "*****",
              "*   *",
              "*   *"],
        "I": ["*****",
              "  *  ",
              "  *  ",
              "  *  ",
              "*****"],
        "L": ["*    ",
              "*    ",
              "*    ",
              "*    ",
              "*****"],
        "O": [" *** ",
              "*   *",
              "*   *",
              "*   *",
              " *** "],
        "V": ["*   *",
              "*   *",
              " * * ",
              " * * ",
              "  *  "],
        "E": ["*****",
              "*    ",
              "**** ",
              "*    ",
              "*****"],
        "Y": ["*   *",
              " * * ",
              "  *  ",
              "  *  ",
              "  *  "],
        "U": ["*   *",
              "*   *",
              "*   *",
              "*   *",
              " *** "],
        "N": ["*   *",
              "**  *",
              "* * *",
              "*  **",
              "*   *"],
        " ": ["     ",
              "     ",
              "     ",
              "     ",
              "     "],
    }

    # Convert to uppercase
    text = text.upper()

    # Print row by row
    for row in range(5):
        line = ""
        for char in text:
            line += patterns.get(char, ["     "]*5)[row] + "  "
        print(line)


# Run program
print_pattern("I LOVE YOU ANNU")
