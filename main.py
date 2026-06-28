from pdf_reader import extract_text


def save_text_to_file(text, output_path):
    with open(output_path, "w", encoding="utf-8") as file:
        file.write(text)


def main():
    pdf_path = "Thesisx.pdf"
    output_path = "output/extracted_text.txt"

    text = extract_text(pdf_path)
    save_text_to_file(text, output_path)

    print("AI PDF Summarizer")
    print("-----------------")
    print(f"Text extracted successfully.")
    print(f"Output saved to: {output_path}")


if __name__ == "__main__":
    main()