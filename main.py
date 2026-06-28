from pdf_reader import extract_text, get_page_count
from stats import count_characters, count_words, estimate_reading_time


def save_text_to_file(text, output_path):
    with open(output_path, "w", encoding="utf-8") as file:
        file.write(text)


def main():
    pdf_path = "thesis.pdf"
    output_path = "output/extracted_text.txt"

    text = extract_text(pdf_path)
    page_count = get_page_count(pdf_path)
    character_count = count_characters(text)
    word_count = count_words(text)
    reading_time = estimate_reading_time(word_count)

    save_text_to_file(text, output_path)

    print("========================")
    print("AI PDF Summarizer")
    print("========================")
    print(f"File: {pdf_path}")
    print(f"Pages: {page_count}")
    print(f"Characters: {character_count}")
    print(f"Words: {word_count}")
    print(f"Estimated Reading Time: {reading_time}")
    print(f"Output saved to: {output_path}")


if __name__ == "__main__":
    main()