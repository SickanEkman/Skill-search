import re


def open_file(filename):
    """
    Open a file and return it's content
    :param filename: String with path to file
    :return: String with file content
    """
    with open(filename, "r") as fin:
        text = fin.read()
        return text


def text_to_set(text):
    """
    Split string by new line, save the elements to a set
    :param text: String
    :return: Set with lines as elements
    """
    set_w_items = set()
    list_w_items = text.split("\n")
    for i in list_w_items:
        if len(i) > 0:
            set_w_items.add(i)
    return set_w_items


def clean_text(text):
    """
    Remove most punctuation from string and make it lowercase
    :param text: String
    :return: String with cleaned up text
    """
    text = text.lower()
    text = text.replace("!", " ")
    text = text.replace("?", " ")
    text = text.replace(";", " ")
    text = text.replace('"', " ")
    text = text.replace("(", " ")
    text = text.replace(")", " ")
    return text


def match_skills(skills, ad):
    """
    Find elements in a text through regex
    :param skills: Set
    :param ad: String
    :return: Print item, start position, end position
    """
    set_to_print = set()
    for skill in skills:
        my_regex = r"(^|\s|/|-)" + re.escape(skill) + r"(or|ar|er|r|n|en|et)?(\s|/|:|\.|-|,|'|$)"
        for hit in re.finditer(my_regex, ad):
            start = hit.start()
            end = hit.end()
            set_to_print.add((skill, start, end))
    return set_to_print


def print_result(result):
    for i in result:
        print(i[0], i[1], i[2])


if __name__ == '__main__':

    text_w_skills = open_file("skills.txt")
    set_w_skills = text_to_set(text_w_skills)

    job_ad = open_file("job-posting.txt")
    cleaned_ad = clean_text(job_ad)

    matches = match_skills(set_w_skills, cleaned_ad)
    print_result(matches)
