def _to_float(value):
    try:
        return float(str(value).strip())
    except (TypeError, ValueError):
        return None


def _academic_band(percentage):
    score = _to_float(percentage)
    if score is None:
        return "unknown"
    if score <= 4.0:
        score *= 25
    if score >= 80:
        return "high"
    if score >= 60:
        return "medium"
    return "foundation"


def _grade_band(grade):
    text = str(grade or "").lower()
    if any(token in text for token in ["bachelor", "undergraduate", "year", "11", "12", "college"]):
        return "advanced"
    if any(token in text for token in ["master", "phd", "postgraduate"]):
        return "expert"
    return "school"


def _specialized_boost(stream, title, interests, skills):
    boost = 0

    if stream == "Science":
        if title == "Software Engineer":
            if {"Technology", "Technical"}.issubset(interests.union(skills)):
                boost += 3
            if "Communication" in skills:
                boost -= 1
        elif title == "Data Scientist":
            if {"Analytical", "Technology"}.issubset(interests.union(skills)):
                boost += 4
            if "Literature" in interests:
                boost -= 1
        elif title == "Research Scientist":
            if "Science" in interests and {"Analytical", "Communication"}.issubset(skills):
                boost += 4
            if "Literature" in interests:
                boost += 2
        elif title == "Doctor":
            if "Social" in interests and {"Communication", "Teamwork"}.issubset(skills):
                boost += 4

    if stream == "Management":
        if title == "Product Manager" and {"Leadership", "Communication"}.issubset(skills):
            boost += 4
        elif title == "Financial Analyst" and {"Analytical", "Technical"}.issubset(skills):
            boost += 4
        elif title == "Digital Marketing Specialist" and {"Creativity", "Communication"}.issubset(skills):
            boost += 4

    if stream == "Humanities":
        if title == "Lawyer" and {"Analytical", "Communication", "Problem"}.issubset(skills):
            boost += 4
        elif title == "Teacher" and {"Communication", "Leadership"}.issubset(skills):
            boost += 4
        elif title == "Journalist" and {"Literature", "Social"}.intersection(interests):
            boost += 2

    if stream == "Arts":
        if title in {"Graphic Designer", "UI/UX Designer"} and {"Creativity", "Technical"}.issubset(skills):
            boost += 4
        elif title == "Content Creator" and {"Creativity", "Communication"}.issubset(skills):
            boost += 4
        elif title == "Video Editor" and {"Technical", "Time"}.issubset(skills):
            boost += 4

    return boost


def get_recommendation(stream, interests, skills, percentage=None, grade=None):
    interest_set = {str(item).strip() for item in (interests or []) if str(item).strip()}
    skill_set = {str(item).strip() for item in (skills or []) if str(item).strip()}
    academic_band = _academic_band(percentage)
    grade_band = _grade_band(grade)

    recommendations = {
        "Science": [
            {"title": "Software Engineer", "description": "Build applications and digital systems that solve real-world problems.", "salary": "$70,000 - $140,000", "future_study": "Computer Engineering / Computer Science", "interests": {"Technology", "Science"}, "skills": {"Technical", "Problem", "Analytical"}, "academic": {"medium", "high"}},
            {"title": "Data Scientist", "description": "Analyze data to find insights and support smart decisions.", "salary": "$75,000 - $150,000", "future_study": "Data Science / Statistics", "interests": {"Science", "Technology"}, "skills": {"Analytical", "Technical", "Problem"}, "academic": {"high"}},
            {"title": "Doctor", "description": "Diagnose, treat, and prevent diseases while caring for patients.", "salary": "$100,000 - $220,000", "future_study": "Medical School", "interests": {"Science", "Social"}, "skills": {"Communication", "Problem", "Teamwork"}, "academic": {"high"}},
            {"title": "Biotechnologist", "description": "Use biology and technology to create medical and industrial innovations.", "salary": "$65,000 - $120,000", "future_study": "Biotechnology / Life Sciences", "interests": {"Science", "Technology"}, "skills": {"Analytical", "Technical"}, "academic": {"medium", "high"}},
            {"title": "Environmental Scientist", "description": "Work on climate, pollution, and sustainability challenges.", "salary": "$60,000 - $110,000", "future_study": "Environmental Science", "interests": {"Science", "Social"}, "skills": {"Analytical", "Problem"}, "academic": {"medium", "high"}},
            {"title": "Lab Technician", "description": "Perform lab testing and support scientific and medical diagnostics.", "salary": "$45,000 - $75,000", "future_study": "Diploma / BSc in Laboratory Technology", "interests": {"Science"}, "skills": {"Technical", "Time", "Teamwork"}, "academic": {"foundation", "medium", "high"}},
            {"title": "Pharmacist", "description": "Prepare medicines and guide patients on safe medication usage.", "salary": "$80,000 - $140,000", "future_study": "Pharmacy Degree", "interests": {"Science", "Social"}, "skills": {"Communication", "Analytical"}, "academic": {"medium", "high"}},
            {"title": "Research Scientist", "description": "Conduct experiments and publish findings in scientific fields.", "salary": "$70,000 - $130,000", "future_study": "MSc / PhD", "interests": {"Science", "Literature"}, "skills": {"Analytical", "Problem", "Communication"}, "academic": {"high"}}
        ],
        "Management": [
            {"title": "Business Analyst", "description": "Bridge business needs and technical teams with data-driven planning.", "salary": "$60,000 - $110,000", "future_study": "BBA / MBA", "interests": {"Business", "Technology"}, "skills": {"Analytical", "Communication"}, "academic": {"medium", "high"}},
            {"title": "Product Manager", "description": "Lead product strategy, roadmap, and team execution.", "salary": "$75,000 - $150,000", "future_study": "MBA / Product Management", "interests": {"Business", "Technology"}, "skills": {"Leadership", "Communication", "Problem"}, "academic": {"medium", "high"}},
            {"title": "Financial Analyst", "description": "Evaluate financial data, budgets, and investment performance.", "salary": "$55,000 - $100,000", "future_study": "Finance / Accounting", "interests": {"Business"}, "skills": {"Analytical", "Technical"}, "academic": {"medium", "high"}},
            {"title": "Digital Marketing Specialist", "description": "Run online campaigns, branding, and growth strategies.", "salary": "$50,000 - $95,000", "future_study": "Marketing / Communications", "interests": {"Business", "Technology", "Arts"}, "skills": {"Creativity", "Communication", "Analytical"}, "academic": {"foundation", "medium", "high"}},
            {"title": "Entrepreneur", "description": "Create and scale business ideas from concept to market.", "salary": "$40,000 - $200,000+", "future_study": "Business Incubation / Startup Courses", "interests": {"Business"}, "skills": {"Leadership", "Problem", "Communication"}, "academic": {"foundation", "medium", "high"}},
            {"title": "Operations Manager", "description": "Improve workflows, productivity, and resource management.", "salary": "$60,000 - $110,000", "future_study": "Operations / Supply Chain", "interests": {"Business"}, "skills": {"Leadership", "Time", "Teamwork"}, "academic": {"medium", "high"}},
            {"title": "HR Manager", "description": "Manage talent, culture, and employee development.", "salary": "$55,000 - $100,000", "future_study": "HR Management", "interests": {"Social", "Business"}, "skills": {"Communication", "Leadership", "Teamwork"}, "academic": {"foundation", "medium", "high"}},
            {"title": "Account Manager", "description": "Build client relationships and grow business accounts.", "salary": "$50,000 - $100,000", "future_study": "Business Administration", "interests": {"Business", "Social"}, "skills": {"Communication", "Leadership"}, "academic": {"foundation", "medium", "high"}}
        ],
        "Humanities": [
            {"title": "Journalist", "description": "Research, verify, and report stories across media platforms.", "salary": "$40,000 - $85,000", "future_study": "Journalism / Mass Communication", "interests": {"Literature", "Social"}, "skills": {"Communication", "Analytical"}, "academic": {"foundation", "medium", "high"}},
            {"title": "Teacher", "description": "Educate and mentor students across academic levels.", "salary": "$40,000 - $75,000", "future_study": "Education Degree", "interests": {"Social", "Literature"}, "skills": {"Communication", "Leadership", "Teamwork"}, "academic": {"foundation", "medium", "high"}},
            {"title": "Lawyer", "description": "Represent clients and solve legal disputes using legal frameworks.", "salary": "$60,000 - $160,000", "future_study": "Law School", "interests": {"Literature", "Social"}, "skills": {"Communication", "Analytical", "Problem"}, "academic": {"high"}},
            {"title": "Psychologist", "description": "Understand behavior and provide mental health guidance.", "salary": "$55,000 - $110,000", "future_study": "Psychology Degree", "interests": {"Social", "Science"}, "skills": {"Communication", "Analytical"}, "academic": {"medium", "high"}},
            {"title": "Social Worker", "description": "Support individuals and communities through social programs.", "salary": "$40,000 - $70,000", "future_study": "Social Work Degree", "interests": {"Social"}, "skills": {"Communication", "Teamwork"}, "academic": {"foundation", "medium", "high"}},
            {"title": "Public Policy Analyst", "description": "Study policies and recommend solutions for public issues.", "salary": "$55,000 - $100,000", "future_study": "Public Policy / Political Science", "interests": {"Social", "Literature"}, "skills": {"Analytical", "Communication"}, "academic": {"medium", "high"}},
            {"title": "Content Strategist", "description": "Plan impactful content for education, media, or brands.", "salary": "$50,000 - $95,000", "future_study": "Communications / Content Marketing", "interests": {"Literature", "Arts"}, "skills": {"Communication", "Creativity", "Analytical"}, "academic": {"foundation", "medium", "high"}},
            {"title": "Historian", "description": "Research historical events and interpret their social impact.", "salary": "$45,000 - $80,000", "future_study": "History / Research", "interests": {"Literature", "Social"}, "skills": {"Analytical", "Communication"}, "academic": {"medium", "high"}}
        ],
        "Arts": [
            {"title": "Graphic Designer", "description": "Create visual identities, digital assets, and communication designs.", "salary": "$45,000 - $90,000", "future_study": "Graphic Design / Multimedia", "interests": {"Arts", "Technology"}, "skills": {"Creativity", "Technical"}, "academic": {"foundation", "medium", "high"}},
            {"title": "UI/UX Designer", "description": "Design user-friendly digital product experiences.", "salary": "$60,000 - $120,000", "future_study": "UX Design / Human-Computer Interaction", "interests": {"Arts", "Technology"}, "skills": {"Creativity", "Analytical", "Communication"}, "academic": {"medium", "high"}},
            {"title": "Animator", "description": "Create motion graphics and animated visual storytelling.", "salary": "$50,000 - $100,000", "future_study": "Animation / Visual Effects", "interests": {"Arts", "Music"}, "skills": {"Creativity", "Technical", "Time"}, "academic": {"foundation", "medium", "high"}},
            {"title": "Photographer", "description": "Capture, edit, and curate professional visual content.", "salary": "$35,000 - $80,000", "future_study": "Photography / Media Arts", "interests": {"Arts"}, "skills": {"Creativity", "Technical"}, "academic": {"foundation", "medium", "high"}},
            {"title": "Content Creator", "description": "Produce digital content for social, education, or entertainment platforms.", "salary": "$35,000 - $120,000+", "future_study": "Media / Digital Production", "interests": {"Arts", "Social", "Music"}, "skills": {"Creativity", "Communication"}, "academic": {"foundation", "medium", "high"}},
            {"title": "Interior Designer", "description": "Design functional and aesthetic indoor spaces.", "salary": "$50,000 - $95,000", "future_study": "Interior Design", "interests": {"Arts"}, "skills": {"Creativity", "Problem", "Communication"}, "academic": {"foundation", "medium", "high"}},
            {"title": "Video Editor", "description": "Edit video storytelling for media, ads, and online platforms.", "salary": "$45,000 - $90,000", "future_study": "Film / Media Production", "interests": {"Arts", "Music"}, "skills": {"Technical", "Creativity", "Time"}, "academic": {"foundation", "medium", "high"}},
            {"title": "Creative Writer", "description": "Write stories, scripts, and creative media content.", "salary": "$40,000 - $85,000", "future_study": "Creative Writing / Literature", "interests": {"Literature", "Arts"}, "skills": {"Creativity", "Communication"}, "academic": {"foundation", "medium", "high"}}
        ]
    }

    recs = recommendations.get(stream, [])
    if not recs:
        return {
            "title": "General Professional",
            "description": "Based on your profile, choose a role that matches your strongest interests and skill growth plan.",
            "salary": "$40,000 - $85,000",
            "future_study": "Further education in your most preferred domain."
        }

    best_score = -999
    best_rank = None
    best_rec = recs[0]

    for rec in recs:
        rec_interests = rec.get("interests", set())
        rec_skills = rec.get("skills", set())

        interest_hits = len(interest_set.intersection(rec_interests))
        skill_hits = len(skill_set.intersection(rec_skills))
        academic_fit = academic_band in rec.get("academic", set())

        score = 0
        score += interest_hits * 5
        score += skill_hits * 6

        # Penalize weak overlap so results change more clearly with input changes.
        if interest_hits == 0:
            score -= 5
        if skill_hits == 0:
            score -= 6

        if academic_fit:
            score += 3

        if grade_band == "expert":
            score += 2
        elif grade_band == "advanced":
            score += 1

        score += _specialized_boost(stream, rec["title"], interest_set, skill_set)

        # Tie-break by depth of match, then by profile-specificity.
        interest_depth = (interest_hits / len(rec_interests)) if rec_interests else 0
        skill_depth = (skill_hits / len(rec_skills)) if rec_skills else 0
        rank = (
            score,
            skill_hits,
            interest_hits,
            round(skill_depth, 3),
            round(interest_depth, 3),
            1 if academic_fit else 0,
        )

        if best_rank is None or rank > best_rank:
            best_rank = rank
            best_score = score
            best_rec = rec

    return {
        "title": best_rec["title"],
        "description": best_rec["description"],
        "salary": best_rec["salary"],
        "future_study": best_rec["future_study"]
    }
