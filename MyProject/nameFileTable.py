import re

# clean table name
# remove whitespaces
# lowercase
# special character


def fileName(file_name):
    clean_table_name = file_name.lower() \
        .replace(" ", "_") \
        .replace("?", "") \
        .replace("-", "") \
        .replace("~", "_") \
        .replace(r"/", "") \
        .replace(r"\\", "") \
        .replace("$", "") \
        .replace(r"(", "").replace(r")", "") \
        .replace("&", "_and_")
    file_name = re.sub(r'\d', "", clean_table_name)
    return file_name


def tableName(file_name):
    clean_table_name = file_name.lower() \
        .replace(" ", "_") \
        .replace("?", "") \
        .replace("-", "") \
        .replace("~", "_") \
        .replace(r"/", "") \
        .replace(r"\\", "") \
        .replace("$", "") \
        .replace(r"(", "").replace(r")", "") \
        .replace("&", "_and_") \
        .replace(".csv", "")
    table_name = re.sub(r'\d', "", clean_table_name)
    return table_name
