def score_extreme_tag(exclusion_list,extreme_tags,current_score,count):
    '''
        reduces the cumulative score exponentially
        example:
        a person doesnt likes death in a movie
        if a movie is found with an extreme tag of death (saperate field than genre)
        then the score is reduced so that likelyhood of the movie
        being recommended is reduced greatly
    '''
    extreme_tags_names=list(extreme_tags.keys())
    for tags in exclusion_list:
        if(tags in extreme_tags_names):
            current_score=current_score-current_score/(20-count)
    return current_score        