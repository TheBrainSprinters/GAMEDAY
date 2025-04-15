def ranked_scores_by_rank_linear(min_score: int, max_score: int, num_scores: int) -> list[int]:
    """Returns the list of scores for each player would receive, from rank 
    1 to num_scores. Rank 1 player will receive max_score, rank n_scores player
    will receive min_score, in between ranks the score will be linearly 
    interpolated.

    Args:
        min_score (int): Minimum score, the score that will be given to the
        player with rank num_scores. 
        max_score (int): Maximum score, the score that will be given to the
        player with rank 1.
        num_scores (int): Number of players.

    Returns:
        list[int]: The list of scores for each player would receive, from 
        rank 1 to num_scores. The first player will receive max_score, the
        last player will receive min_score.
    """
    gap = (max_score - min_score) // (num_scores - 1)
    remainder = (max_score - min_score) % (num_scores - 1)
    scores = [(min_score + (i * gap)) for i in range (num_scores)]
    for i in range (remainder):
        scores[num_scores - 1 - i] += remainder - i
    scores.reverse()
    return scores

