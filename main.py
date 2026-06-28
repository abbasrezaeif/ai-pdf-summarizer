from pdf_reader import extract_text, get_page_count
from stats import count_characters, count_words, estimate_reading_time
from summarizer import create_basic_summary


def save_text_to_file(text, output_path):
    with open(output_path, "w", encoding="utf-8") as file:
        file.write(text)


def main():
    pdf_path = "thesis.pdf"
    extracted_text_path = "output/extracted_text.txt"
    summary_path = "output/summary.txt"

    text = extract_text(pdf_path)
    page_count = get_page_count(pdf_path)
    character_count = count_characters(text)
    word_count = count_words(text)
    reading_time = estimate_reading_time(word_count)
    summary = create_basic_summary(text)

    save_text_to_file(text, extracted_text_path)
    save_text_to_file(summary, summary_path)

    print("========================")
    print("AI PDF Summarizer")
    print("========================")
    print(f"File: {pdf_path}")
    print(f"Pages: {page_count}")
    print(f"Characters: {character_count}")
    print(f"Words: {word_count}")
    print(f"Estimated Reading Time: {reading_time}")
    print(f"Extracted text saved to: {extracted_text_path}")
    print(f"Summary saved to: {summary_path}")


if __name__ == "__main__":
    main()