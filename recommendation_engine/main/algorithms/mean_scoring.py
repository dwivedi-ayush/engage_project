def score_mean(preferred_mean_value,current_value,constraint_parameter):
    mean_diff_score=(constraint_parameter-abs(float(preferred_mean_value)-int(current_value)))/constraint_parameter
    return mean_diff_score