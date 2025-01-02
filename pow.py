import hashlib

def solve_pow(zero_count, input_data, complexity, challenge_type):
    """Solve proof-of-work challenge."""
    solutions = []
    postfix = 0
    while len(solutions) < zero_count:
        postfix += 1
        hash_value = hashlib.sha256(f"{input_data}{postfix}".encode('utf-8')).hexdigest()
        if hash_value[:complexity] == '0' * complexity:
            solutions.append({'hash': hash_value, 'postfix': postfix})
    return {'hash': solutions, 'type': challenge_type}