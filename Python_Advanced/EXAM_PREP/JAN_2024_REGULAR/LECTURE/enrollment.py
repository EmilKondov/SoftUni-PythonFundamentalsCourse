def gather_credits(number_of_credits, *name_credits):
    current_credits = 0
    courses_enrolled = {}

    for name, value in name_credits:
        if current_credits < number_of_credits:
            if name in courses_enrolled:
                continue
            courses_enrolled[name] = value
            current_credits += value
        else:
            break

    if current_credits >= number_of_credits:
        return (f"Enrollment finished! Maximum credits: {current_credits}.\n"
                f"Courses: {', '.join(sorted(courses_enrolled))}")
    return f"You need to enroll in more courses! You have to gather {number_of_credits - current_credits} credits more."




# print(gather_credits(80,("Basics", 27),))

print(gather_credits(
60,
("Basics", 27),
("Fundamentals", 27),
("Advanced", 30),
("Web", 30)
))