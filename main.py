from pdf_reader import extract_text


def main():
    pdf_path = "Thesisx.pdf"

    text = extract_text(pdf_path)

    print(text)


if __name__ == "__main__":
    main()