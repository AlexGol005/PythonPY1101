def task() -> str:
    list_words = [
        "Goldenrod",
        "Purple",
        "Salmon",
        "Turquoise",
        "Cyan"
    ]

    return min(list(map(len, list_words)))


if __name__ == "__main__":
    print(task())
