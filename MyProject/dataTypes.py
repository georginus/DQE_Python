# change csv data types to postgres data types

def dataTypes():
    replacements = {
        'object': 'varchar'
        , 'float': 'decimal(29,6)'
        , 'int64': 'integer'
        , 'datetime64': 'timestamp'
        , 'timedelta64': 'varchar'
    }
    return replacements
