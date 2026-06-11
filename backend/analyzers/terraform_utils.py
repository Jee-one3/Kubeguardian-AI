def clean_string(value):

    if isinstance(value, str):

        return value.strip('"')

    return value