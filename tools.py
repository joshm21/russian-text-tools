import csv
import logging
import argparse


EQUIVALENT_LETTERS = [
  { "bare": "А", "apostraphe": "А'", "accent": "А́" },
  { "bare": "Е", "apostraphe": "Е'", "accent": "Е́" },
  { "bare": "И", "apostraphe": "И'", "accent": "И́" },
  { "bare": "О", "apostraphe": "О'", "accent": "О́" },
  { "bare": "У", "apostraphe": "У'", "accent": "У́" },
  { "bare": "Ы", "apostraphe": "Ы'", "accent": "Ы́" },
  { "bare": "Э", "apostraphe": "Э'", "accent": "Э́" },
  { "bare": "Ю", "apostraphe": "Ю'", "accent": "Ю́" },
  { "bare": "Я", "apostraphe": "Я'", "accent": "Я́" },
  { "bare": "а", "apostraphe": "а'", "accent": "а́" },
  { "bare": "е", "apostraphe": "е'", "accent": "е́" },
  { "bare": "и", "apostraphe": "и'", "accent": "и́" },
  { "bare": "о", "apostraphe": "о'", "accent": "о́" },
  { "bare": "у", "apostraphe": "у'", "accent": "у́" },
  { "bare": "ы", "apostraphe": "ы'", "accent": "ы́" },
  { "bare": "э", "apostraphe": "э'", "accent": "э́" },
  { "bare": "ю", "apostraphe": "ю'", "accent": "ю́" },
  { "bare": "я", "apostraphe": "я'", "accent": "я́" }
]


def remove_accents_and_apostraphes(input_str):
    # but don't change ё to е
    result = input_str
    for letter in EQUIVALENT_LETTERS:
        logging.debug(f'replacing {letter["apostraphe"]} with {letter["bare"]}')
        result = result.replace(letter["apostraphe"], letter["bare"])
        logging.debug(f'replacing {letter["accent"]} with {letter["bare"]}')
        result = result.replace(letter["accent"], letter["bare"])
    return result


def replace_apostraphes_with_accents(input_str):
    result = input_str
    for letter in EQUIVALENT_LETTERS:
        logging.debug(f'replacing {letter["apostraphe"]} with {letter["accent"]}')
        result = result.replace(letter["apostraphe"], letter["accent"])
    return result


def replace_accents_with_apostraphes(input_str):
    result = input_str
    for letter in EQUIVALENT_LETTERS:
        logging.debug(f'replacing {letter["accent"]} with {letter["apostraphe"]}')
        result = result.replace(letter["accent"], letter["apostraphe"])
    return result


def add_stress_marks(input_str):
    bare_to_stressed = csv_to_dict("russian3 - words_forms.csv", 5, 4) # _form_bare, form
    words = list(filter(None, input_str.split(" ")))
    result = []
    for word in words:
        without_punctuation = remove_leading_trailing_punctuation(word)
        stressed = bare_to_stressed.get(without_punctuation.lower(), False)
        if stressed:
            if len(stressed) > 1:
                logging.debug(f"Multiple possible stressed forms for {without_punctuation}")
            replacement = "|".join(stressed)
            logging.debug(f"Replacing {without_punctuation.lower()} with {replacement}")
            result.append(replace_lower_upper_title_cases(word, without_punctuation, replacement))
        else:
            logging.debug(f"Not replacing {without_punctuation}; did not find stressed equivalent")
            result.append(word)
    return " ".join(result)


def convert_to_dictionary_forms(input_str):
    logging.debug("starting...")
    bare_to_id = csv_to_dict("russian3 - words_forms.csv", 5, 1) # _form_bare, word_id
    id_to_dictionary = csv_to_dict("russian3 - words.csv", 0, 3) # id, accented 
    words = list(filter(None, input_str.split(" ")))
    result = []
    for word in words:
        without_punctuation = remove_leading_trailing_punctuation(word)
        logging.debug(without_punctuation)
        word_ids = bare_to_id.get(without_punctuation.lower(), False)
        if word_ids:
            if len(word_ids) > 1:
                logging.debug(f"Multiple possible word ids for {without_punctuation.lower()}: {word_ids}")
            all_dictionary_forms = []
            for id_ in word_ids:
                dict_form = id_to_dictionary[id_]
                if len(dict_form) > 1:
                    logging.debug(f"Multiple possible dictionary forms found for {id_}: {dict_form}")
                all_dictionary_forms += dict_form
            replacement = "|".join(all_dictionary_forms)
            logging.debug(f"Replacing {without_punctuation.lower()} with {replacement}")
            result.append(replace_lower_upper_title_cases(word, without_punctuation, replacement))
        else:
            logging.debug(f"Not replacing {without_punctuation.lower()}; did not find in words_forms.csv")
            result.append(word)
    return " ".join(result)


def csv_to_dict(csv_filename, key_index, value_index):
    logging.info(f"Loading {csv_filename}; this may take a few seconds...")
    result = {}
    with open(csv_filename, "r", encoding="utf-8-sig") as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            key = row[key_index]
            val = row[value_index]
            if not key in result:
                result[key] = []
            if not val in result[key]:
                result[key].append(val)
    return result


def remove_leading_trailing_punctuation(input_str):
    # but not punctuation in middle of input_str
    punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~«»'''

    index_first_nonpunctuation = 0
    for ndx, char in enumerate(input_str):
        if char in punctuation:
            index_first_nonpunctuation = ndx + 1
        else:
            break

    index_last_nonpunctiaton = len(input_str)
    for ndx, char in enumerate(input_str):
        if not char in punctuation:
            index_last_nonpunctiaton = ndx 

    return input_str[index_first_nonpunctuation:index_last_nonpunctiaton+1]


def capitalize_first_letter(input_str):
    # upper capitalizes after every punctuation mark, even mid word
    return input_str[:1].upper() + input_str[1:]


def replace_lower_upper_title_cases(input_str, replace_str, replace_with):
    return input_str \
        .replace(replace_str.lower(), replace_with.lower()) \
        .replace(replace_str.upper(), replace_with.upper()) \
        .replace(capitalize_first_letter(replace_str), capitalize_first_letter(replace_with))


if __name__ == "__main__":
    tools = ['strip_bare', 'to_accent', 'to_apostraphe', 'add_stress', 'to_dictionary_form']
    tool_functions = ['remove_accents_and_apostraphes', 'replace_apostraphes_with_accents', 'replace_accents_with_apostraphes', 'add_stress_marks', 'convert_to_dictionary_forms']
    log_levels = ['debug', 'info', 'warning', 'error', 'critical']
    parser = argparse.ArgumentParser(
            epilog="""For using input and output files, use the following syntax (linux):
            python3 tools.py to_accent input.txt > output.txt""")
    parser.add_argument("tool", help="the tool to run; one of " + ", ".join(tools), choices = tools, metavar="tool")
    parser.add_argument("input", nargs="?", type=argparse.FileType('r'), help="the text to run the tool on")
    parser.add_argument("-l", "--log", help="debug level; defaults to warning; one of " + ", ".join(log_levels), choices= log_levels, metavar="")
    args = parser.parse_args()
    if args.log:
        numeric_level = getattr(logging, args.log.upper(), None)
        if not isinstance(numeric_level, int):
            raise ValueError(f"Invalid log level: {args.log}")
        logging.basicConfig(level=numeric_level)
    function_to_run = locals()[tool_functions[tools.index(args.tool)]]
    print(function_to_run(args.input.read()))
