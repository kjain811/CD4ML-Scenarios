from cd4ml.date_utils import ymd_to_date_string, add_to_date_string


def get_cutoff_dates(pipeline_params):
    days_back = pipeline_params['problem_params']['days_back']
    max_date = pipeline_params['problem_params']['max_date']
    date_cutoff = add_to_date_string(max_date, days=-days_back)
    return date_cutoff, max_date


def get_date_from_row(row):
    numbers = (int(row['year']), int(row['month']), int(row['day']))
    return ymd_to_date_string(numbers)


def get_training_validation_filters(pipeline_params):
    cutoff_date, max_date = get_cutoff_dates(pipeline_params)

    def train_filter(row):
        return get_date_from_row(row) < cutoff_date

    def validate_filter(row):
        return cutoff_date <= get_date_from_row(row) <= max_date

    return train_filter, validate_filter
