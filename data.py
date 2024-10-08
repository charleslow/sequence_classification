import rich
import random
import string
import nltk
from nltk.corpus import words

nltk.download('words', quiet=True)

MIN_SENTENCE_LENGTH = 15
MAX_SENTENCE_LENGTH = 30

ENGLISH_WORDS = list(words.words())
SUBSET_WORDS = random.sample(ENGLISH_WORDS, 1000)

class DataGenerator:
    """Generate rows for the dataset."""

    @staticmethod
    def generate_random_word():
        return random.choice(SUBSET_WORDS)

    @classmethod
    def generate_random_sentence(cls, word_count):
        return ' '.join(cls.generate_random_word() for _ in range(word_count))

    @staticmethod
    def generate_random_spans(sentence, num_spans):
        words = sentence.split()
        spans = []
        last_word_index = -1
        for _ in range(num_spans):
            if last_word_index >= len(words) - 1:
                break
            start_word = random.randint(last_word_index + 1, last_word_index + 5)
            num_words = random.randint(1, 3)
            end_word = start_word + num_words
            if end_word >= len(words):
                break

            start_char = len(' '.join(words[:start_word]))
            if start_word > 0:
                start_char += 1  # Add space before the first word of the span
            end_char = len(' '.join(words[:end_word + 1]))

            spans.append((start_char, end_char))
            last_word_index = end_word
        return spans

    @classmethod
    def generate_row(cls):
        sentence = cls.generate_random_sentence(random.randint(MIN_SENTENCE_LENGTH, MAX_SENTENCE_LENGTH))
        spans = cls.generate_random_spans(sentence, random.randint(1, 3))
        return {
            "text": sentence,
            "spans": spans,
        }

    @classmethod
    def generate_dataset(cls, num_rows):
        results = []
        i = 0
        while i < num_rows:
            row = cls.generate_row()
            if len(row["spans"]) > 0:
                results.append(row)
                i += 1
        return results


if __name__ == "__main__":
    generator = DataGenerator()
    dataset = generator.generate_dataset(5)
    rich.print(dataset)


