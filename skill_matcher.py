import re

COMMON_SKILLS = [
    "python","java","c++","machine learning",
    "sql","html","css","javascript",
    "data analysis","tensorflow","react"
]

def analyze_resume(resume_text, jd_text):

    found_skills = []
    
    for skill in COMMON_SKILLS:
        if skill in resume_text:
            found_skills.append(skill)

    jd_skills = []
    for skill in COMMON_SKILLS:
        if skill in jd_text.lower():
            jd_skills.append(skill)

    missing = list(set(jd_skills) - set(found_skills))

    score = min(10, len(found_skills))

    suggestions = []

    if score < 5:
        suggestions.append("Add more technical skills related to your field.")

    if "project" not in resume_text:
        suggestions.append("Include project descriptions with action verbs.")

    if len(resume_text.split()) < 200:
        suggestions.append("Resume looks short. Add achievements and experience.")

    return {
        "skills": found_skills,
        "missing_skills": missing,
        "score": score,
        "suggestions": suggestions
    }
