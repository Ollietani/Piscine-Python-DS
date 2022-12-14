#!/usr/bin/env python3
def get_tuple():
    tuples = [
        ('Russia', '25'),
        ('France', '132'),
        ('Germany', '132'),
        ('Spain', '178'),
        ('Italy', '162'),
        ('Portugal', '17'),
        ('Finland', '3'),
        ('Hungary', '2'),
        ('The Netherlands', '28'),
        ('The USA', '610'),
        ('The United Kingdom', '95'),
        ('China', '83'),
        ('Iran', '76'),
        ('Turkey', '65'),
        ('Belgium', '34'),
        ('Canada', '28'),
        ('Switzerland', '26'),
        ('Brazil', '25'),
        ('Austria', '14'),
        ('Israel', '12')
    ]
    return tuples


def tuple_to_dict(tupl):
    dict_data = {}
    for x, y in tupl:
        dict_data.setdefault(y, []).append(x)
    return dict_data


def main():
    d = tuple_to_dict(get_tuple())
    for k, v in d.items():
        for vv in v:
            print(f"'{k}' : '{vv}'")


if __name__ == '__main__':
    main()
