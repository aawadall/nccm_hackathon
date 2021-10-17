"""Escalation Thresaholds"""

hate_categories = ['islamophobia', 'anti-black', 'anti-woman']

escalation_matrix = [[0.1, 0.1, 0.1],
                     [0.2, 0.15, 0.11],
                     [0.4, 0.3, 0.22]]

media_library = {
    0: ['Islamophobia response 1', 'Islamophobia response 2', 'Islamophobia response 3'],
    1: ['Anti-black response 1', 'Anti-black response 2', 'Anti-black response 3'],
    2: ['Anti-woman response 1', 'Anti-woman response 2', 'Anti-woman response 3']
}


def get_escalations(violations):
    """from violations vector, find escalation level for each categoty"""
    result = {}
    category = 0

    print("violations")
    print(violations)
    for violation in violations:
        # take a slice of the escalation matrix
        print(violation)
        escalation_slice = escalation_matrix[category]
        # find the escalation level where the violation is greater than the threshold and and the next level
        # escalation_level = escalation_slice.index(
        #     max(escalation_slice[:violation]))
        escalation_level = [idx for idx in range(
            len(escalation_slice)) if escalation_slice[idx] < violation]
        print(escalation_level)
        if escalation_level:
            result[hate_categories[category]] = {
                "level": escalation_level,
                "response": media_library[category][escalation_level]}

        # increment the category
        category += 1

    return result
