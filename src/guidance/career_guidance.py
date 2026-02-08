# Career Guidance for Class 12
# Matches notebook logic exactly

def recommend_career_class12(stream, avg_500, activity_score):

    percent = (avg_500 / 500) * 100

    # -------------------------------
    # HIGH SCORE (>= 75%)
    # -------------------------------
    if percent >= 75:

        if stream == "Non-Medical":
            return (
                [
                    "Engineering (BTech)",
                    "Data Science / AI",
                    "Core Engineering (Mechanical / Electrical / Civil)"
                ],
                [
                    "IGU Meerpur",
                    "DTU Delhi",
                    "NSUT Delhi",
                    "NIT Kurukshetra",
                    "IIIT Hyderabad (High Rank Only)"
                ],
                [
                    "Strong PCM foundation",
                    "JEE Main / State CET recommended",
                    "Top colleges depend on entrance rank"
                ]
            )

        elif stream == "Medical":
            return (
                [
                    "MBBS",
                    "BDS (Dental)",
                    "Nursing",
                    "Physiotherapy",
                    "Pharmacy"
                ],
                [
                    "IGU Meerpur (Pharmacy)",
                    "State Government Medical Colleges",
                    "Private Medical Colleges",
                    "Nursing Colleges"
                ],
                [
                    "NEET qualification required",
                    "MBBS depends on rank & category",
                    "Healthcare career path"
                ]
            )

        elif stream == "Commerce":
            return (
                [
                    "CA / CS",
                    "BCom",
                    "MBA (Future)",
                    "Finance / Business Analytics"
                ],
                [
                    "IGU Meerpur",
                    "Delhi University (Mid Colleges)",
                    "NMIMS",
                    "Christ University"
                ],
                [
                    "Strong finance & business foundation",
                    "Professional courses recommended"
                ]
            )

        elif stream == "Arts":
            return (
                [
                    "Law",
                    "UPSC Preparation",
                    "Psychology",
                    "Journalism"
                ],
                [
                    "IGU Meerpur",
                    "Delhi University",
                    "Jamia Millia Islamia",
                    "TISS Mumbai"
                ],
                [
                    "Good communication & humanities skills"
                ]
            )

    # -------------------------------
    # MEDIUM SCORE (60% – 74%)
    # -------------------------------
    if 60 <= percent < 75:

        if stream == "Non-Medical":
            return (
                [
                    "Private / Tier-2 Engineering",
                    "Diploma / Polytechnic",
                    "Software / IT",
                    "BCA / MCA Path"
                ],
                [
                    "IGU Meerpur",
                    "VIT Vellore",
                    "UPES Dehradun",
                    "Amity University",
                    "State Engineering Colleges"
                ],
                [
                    "Tier-1 IIT/NIT unlikely",
                    "Focus on coding & internships"
                ]
            )

        elif stream == "Medical":
            return (
                [
                    "Nursing",
                    "Pharmacy",
                    "Paramedical",
                    "Biotechnology"
                ],
                [
                    "IGU Meerpur",
                    "State Nursing Colleges",
                    "Private Pharmacy Colleges",
                    "Paramedical Institutes"
                ],
                [
                    "MBBS unlikely — allied health is realistic"
                ]
            )

        elif stream == "Commerce":
            return (
                [
                    "BCom",
                    "Banking",
                    "Accounting",
                    "MBA (Later)",
                    "Tally / GST"
                ],
                [
                    "IGU Meerpur",
                    "Delhi University (Mid Colleges)",
                    "State Commerce Colleges",
                    "Private Business Colleges"
                ],
                [
                    "Commerce + skill certification recommended"
                ]
            )

        elif stream == "Arts":
            return (
                [
                    "BA",
                    "Teaching",
                    "Government Exams",
                    "Media / Content"
                ],
                [
                    "IGU Meerpur",
                    "Delhi University",
                    "IGNOU",
                    "State Colleges"
                ],
                [
                    "Govt exams & teaching are common paths"
                ]
            )

    # -------------------------------
    # LOW SCORE + HIGH ACTIVITY (<60%)
    # -------------------------------
    if percent < 60 and activity_score > 5:
        return (
            [
                "Sports Training",
                "Dance / Music",
                "YouTube / Content Creation",
                "Photography / Video Editing",
                "Event Crew / Media Production",
                "Gym Trainer / Fitness Coach"
            ],
            [
                "Local Sports Academies",
                "AAFT Noida",
                "Whistling Woods",
                "State Sports Hostels",
                "Media Training Institutes"
            ],
            [
                "Success depends on skill & discipline",
                "Portfolio + daily practice required",
                "Income may start low initially"
            ]
        )

    # -------------------------------
    # LOW SCORE + LOW ACTIVITY (<60%)
    # -------------------------------
    if percent < 60 and activity_score <= 5:
        return (
            [
                "ITI Trades (Electrician / Mechanic)",
                "Polytechnic Diploma",
                "Retail / Sales Jobs",
                "Call Center / BPO",
                "Delivery / Logistics",
                "Mobile Repair / Technician",
                "Railway / SSC Group D Jobs",
                "Small Business / Shop Work"
            ],
            [
                "Government ITI Colleges",
                "State Polytechnic Institutes",
                "PMKVY Skill Centers",
                "NSDC Training Centers",
                "Local Apprenticeship Programs"
            ],
            [
                "Focus on earning early",
                "Learn one practical skill for stability",
                "Career growth depends on experience"
            ]
        )

    # -------------------------------
    # FALLBACK SAFE RETURN
    # -------------------------------
    return (
        ["Career Exploration"],
        ["Career Counseling / Aptitude Test"],
        ["More data needed for accurate guidance"]
    )