COMMON_SKILLS = [
    "python",
    "java",
    "c",
    "c++",
    "sql",
    "html",
    "css",
    "javascript",
    "machine learning",
    "data analysis"
]


def analyze_resume(resume, jobdesc):

    detected_skills = []

    for skill in COMMON_SKILLS:
        if skill in resume:
            detected_skills.append(skill)

    jd_skills = []

    for skill in COMMON_SKILLS:
        if skill in jobdesc.lower():
            jd_skills.append(skill)

    missing_skills = []

    for skill in jd_skills:
        if skill not in detected_skills:
            missing_skills.append(skill)

    score = len(detected_skills)

    if score > 10:
        score = 10

    suggestions = []

    if score < 5:
        suggestions.append("Add more technical skills relevant to the job.")

    if "project" not in resume:
        suggestions.append("Include project descriptions in your resume.")

    if "experience" not in resume:
        suggestions.append("Mention internships or practical experience.")

    return {
        "skills": detected_skills,
        "missing": missing_skills,
        "score": score,
        "suggestions": suggestions
    }
