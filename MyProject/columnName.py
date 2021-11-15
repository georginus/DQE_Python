from dataTypes import dataTypes
# clean headers
# remove whitespaces
# lowercase
# special characters


def columnName(df):
    df.columns = [x.lower() \
                      .replace(" ", "_") \
                      .replace("?", "") \
                      .replace("-", "_") \
                      .replace("~", "_") \
                      .replace(r"/", "") \
                      .replace(r"\\", "") \
                      .replace("$", "") \
                      .replace("&", "_and_") \
                      .replace(r"(", "").replace(r")", "") for x in df.columns]
    col_str = ", ".join("{} {}".format(n, d) for (n, d) in zip(df.columns, df.dtypes.replace(dataTypes())))
    return col_str
