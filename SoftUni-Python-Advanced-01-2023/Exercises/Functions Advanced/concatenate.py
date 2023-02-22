def concatenate(*args, **kwargs):
    main_string = ''.join(args)

    for old_string, new_string in kwargs.items():
        if old_string in main_string:
            main_string = main_string.replace(old_string, new_string)

    return main_string

print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))