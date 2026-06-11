from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import (
    getSampleStyleSheet
)

from datetime import datetime

def generate_report(
    candidate_name,    
    score,
    semantic_score,
    grade,
    final_rank,
    decision,
    skills,
    missing_skills,
    recommendations,
    career,
    edu_score,
    impact
):

    pdf = SimpleDocTemplate(
        "report.pdf"
    )

    styles = getSampleStyleSheet()

    content = []

    content.append(
        Paragraph(
            "AI Resume Analysis Report",
            styles["Title"]
        )
    )

    content.append(
        Spacer(1, 12)
    )

    content.append(
        Paragraph(
            f"Candidate: {candidate_name}",
            styles["BodyText"]
        )
    )

    content.append(
        Spacer(1, 12)
    )

    content.append(
    Paragraph(
        "Analysis Summary",
        styles["Heading1"]
    )
)
    content.append(
        Paragraph(
            f"ATS Score: {score:.1f}%",
            styles["BodyText"]
        )
    )

    content.append(
        Paragraph(
            f"Semantic Score: {semantic_score:.1f}%",
            styles["BodyText"]
        )
    )

    content.append(
        Paragraph(
            f"Grade: {grade}",
            styles["BodyText"]
        )
    )

    content.append(
        Paragraph(
            f"Final Rank: {final_rank:.1f}%",
            styles["BodyText"]
        )
    )

    content.append(
        Paragraph(
            f"Hiring Decision: {decision}",
            styles["BodyText"]
        )
    )

    content.append(
        Paragraph(
            "Skill Analysis",
            styles["Heading1"]
        )
    )
    content.append(
        Paragraph(
            "Skills:",
            styles["Heading2"]
        )
    )

    content.append(
        Paragraph(
            ",".join(skills),
            styles["BodyText"]
        )
    )

    content.append(
        Paragraph(
            "Missing Skills:",
            styles["Heading2"]
        )
    )

    content.append(
        Paragraph(
            ",".join(
                missing_skills
                ),
            styles["BodyText"]
        )
    )

    content.append(
        Paragraph(
            "Recommendations",
            styles["Heading1"]
        )
    )
    
    for rec in recommendations:
        content.append(
            Paragraph(
                rec,
                styles["BodyText"]
            )
        )

    content.append(
        Paragraph(
            datetime.now().strftime(
                "%d-%m-%Y"
            ),
            styles["BodyText"]
        )
    )

    content.append(
        Paragraph(
            "Advanced ATS Analysis",
            styles["Heading1"]
        )
    )

    content.append(
        Paragraph(
            f"Career Score: {career}%",
            styles["BodyText"]
        )
    )

    content.append(
        Paragraph(
            f"Education Score: {edu_score}%",
            styles["BodyText"]
        )
    )

    content.append(
        Paragraph(
            "Achievemnet Analysis",
            styles["Heading1"]
        )
    )

    content.append(
        Paragraph(
            f"Imapct Score: {impact}%",
            styles["BodyText"]
        )
    )


    pdf.build(
        content
    )