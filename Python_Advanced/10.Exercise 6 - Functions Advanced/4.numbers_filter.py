def even_odd_filter(**number_set):

    if "even" in number_set:
        number_set["even"] = [n for n in number_set["even"] if n % 2 == 0]

    if "odd" in number_set:
        number_set["odd"] = [n for n in number_set["odd"] if n % 2 != 0]

    return dict(sorted(number_set.items(), key=lambda x:-len(x[1])))

print(even_odd_filter(odd=[1, 2, 3, 4, 10, 5],even=[3, 4, 5, 7, 10, 2, 5, 5, 2],))