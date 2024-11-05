def player(prev_play, opponent_history=[], play_order=None):
    # Track opponent's history
    if prev_play:
        opponent_history.append(prev_play)
    
    # Dictionary to counter each move
    counter_moves = {'R': 'P', 'P': 'S', 'S': 'R'}
    
    # Initialize play order tracking for Abbey's strategy
    if play_order is None:
        play_order = {
            "RR": 0, "RP": 0, "RS": 0,
            "PR": 0, "PP": 0, "PS": 0,
            "SR": 0, "SP": 0, "SS": 0,
        }

    # Strategy 1: Counter Quincy's Pattern
    quincy_pattern = ["R", "R", "P", "P", "S"]
    if len(opponent_history) < 5:
        guess = "R"  # Initial guess for first few moves
    else:
        quincy_index = len(opponent_history) % len(quincy_pattern)
        guess = counter_moves[quincy_pattern[quincy_index]]

    # Strategy 2: Frequency Analysis for Mrugesh (Track recent moves)
    if len(opponent_history) >= 10:
        last_ten = opponent_history[-10:]
        most_common_move = max(set(last_ten), key=last_ten.count)
        guess = counter_moves[most_common_move]

    # Strategy 3: Countering Kris by guessing his counter
    if len(opponent_history) > 1:
        kris_predicted = counter_moves[opponent_history[-1]]
        guess = counter_moves[kris_predicted]

    # Strategy 4: Abbey's Sequence Prediction (Track two-move sequences)
    if len(opponent_history) > 1:
        last_two = "".join(opponent_history[-2:])
        if len(last_two) == 2:
            play_order[last_two] += 1

        # Determine the most likely next move based on Abbey's sequence
        possible_plays = [prev_play + "R", prev_play + "P", prev_play + "S"]
        prediction_counts = {play: play_order[play] for play in possible_plays if play in play_order}
        
        if prediction_counts:
            predicted_move = max(prediction_counts, key=prediction_counts.get)[-1]
            guess = counter_moves[predicted_move]

    return guess
