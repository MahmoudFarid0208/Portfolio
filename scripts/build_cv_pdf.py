#!/usr/bin/env python3
"""Build a clean one-page, role-targeted CV PDF."""
from pathlib import Path
import argparse
from xml.sax.saxutils import escape
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_RIGHT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable, Table, TableStyle, KeepTogether

NAVY = colors.HexColor("#17365D")
BLUE = colors.HexColor("#2754A5")
INK = colors.HexColor("#1F2937")
MUTED = colors.HexColor("#5B6573")
RULE = colors.HexColor("#D8E0EB")

def styles():
    b = getSampleStyleSheet()
    return {
        "name": ParagraphStyle("Name", parent=b["Normal"], fontName="Helvetica-Bold", fontSize=19, leading=21, textColor=NAVY, alignment=TA_CENTER, spaceAfter=2),
        "headline": ParagraphStyle("Headline", parent=b["Normal"], fontName="Helvetica-Bold", fontSize=8.8, leading=10.5, textColor=BLUE, alignment=TA_CENTER, spaceAfter=4),
        "contact": ParagraphStyle("Contact", parent=b["Normal"], fontName="Helvetica", fontSize=7.1, leading=9, textColor=MUTED, alignment=TA_CENTER, spaceAfter=2),
        "section": ParagraphStyle("Section", parent=b["Normal"], fontName="Helvetica-Bold", fontSize=8.5, leading=10, textColor=NAVY, spaceBefore=4, spaceAfter=2),
        "body": ParagraphStyle("Body", parent=b["Normal"], fontName="Helvetica", fontSize=7.35, leading=9, textColor=INK, spaceAfter=1.2),
        "skill": ParagraphStyle("Skill", parent=b["Normal"], fontName="Helvetica", fontSize=7.15, leading=8.65, textColor=INK, spaceAfter=1.1),
        "role": ParagraphStyle("Role", parent=b["Normal"], fontName="Helvetica-Bold", fontSize=7.7, leading=9.2, textColor=INK),
        "date": ParagraphStyle("Date", parent=b["Normal"], fontName="Helvetica-Bold", fontSize=7.1, leading=9, textColor=MUTED, alignment=TA_RIGHT),
        "bullet": ParagraphStyle("Bullet", parent=b["Normal"], fontName="Helvetica", fontSize=7.2, leading=8.7, textColor=INK, leftIndent=8, firstLineIndent=-6, spaceAfter=0.8),
        "small": ParagraphStyle("Small", parent=b["Normal"], fontName="Helvetica", fontSize=7, leading=8.5, textColor=INK, spaceAfter=1),
    }

def section(title, st):
    return [Spacer(1, 1.5), Paragraph(escape(title.upper()), st["section"]), HRFlowable(width="100%", thickness=.55, color=RULE, spaceBefore=0, spaceAfter=3)]

def bullet(text, st):
    return Paragraph("- " + escape(text), st["bullet"])

def role_header(title, dates, st):
    t = Table([[Paragraph(escape(title), st["role"]), Paragraph(escape(dates), st["date"])]], colWidths=[130*mm, 50*mm])
    t.setStyle(TableStyle([("VALIGN",(0,0),(-1,-1),"TOP"),("LEFTPADDING",(0,0),(-1,-1),0),("RIGHTPADDING",(0,0),(-1,-1),0),("TOPPADDING",(0,0),(-1,-1),0),("BOTTOMPADDING",(0,0),(-1,-1),0)]))
    return t

def build(output: Path):
    output.parent.mkdir(parents=True, exist_ok=True)
    doc = SimpleDocTemplate(str(output), pagesize=A4, rightMargin=14*mm, leftMargin=14*mm, topMargin=10*mm, bottomMargin=9*mm,
        title="Mahmoud Farid - Software Developer CV", author="Mahmoud Farid", subject="Software Developer | Android, Backend and AI Integration")
    st, story = styles(), []
    story += [Paragraph("MAHMOUD FARID", st["name"]), Paragraph("SOFTWARE DEVELOPER | ANDROID, BACKEND &amp; AI INTEGRATION", st["headline"]),
        Paragraph('Cairo, Egypt &nbsp;|&nbsp; +20 115 712 4733 &nbsp;|&nbsp; <link href="mailto:mahmoud.farid620@gmail.com" color="#5B6573">mahmoud.farid620@gmail.com</link>', st["contact"]),
        Paragraph('<link href="https://mahmoudfarid0208.github.io/Portfolio/" color="#2754A5">Portfolio</link> &nbsp;|&nbsp; <link href="https://github.com/MahmoudFarid0208" color="#2754A5">GitHub</link> &nbsp;|&nbsp; Military Service: Completed', st["contact"]), Spacer(1,2)]
    story += section("Professional Summary", st)
    story.append(Paragraph("Software Developer with 2+ years of experience building and deploying production Android applications and integrated business systems. Strong foundation in Kotlin, OOP, REST APIs, Clean Architecture, MVVM, Firebase, Ktor backend development, CRM integrations, and AWS Lightsail. Developed connected business applications and AI-powered request classification and knowledge-base chatbot features. Interested in building reliable software and expanding into AI-assisted development and broader application engineering.", st["body"]))
    story += section("Technical Skills", st)
    for label, value in [
        ("Programming &amp; Architecture", "Kotlin, OOP, SOLID, Clean Architecture, MVVM"),
        ("Android", "Android SDK, Jetpack Compose, Coroutines, Navigation Compose, Dagger Hilt, Material Design"),
        ("Backend &amp; APIs", "Ktor, REST APIs, Retrofit, Firebase Realtime Database, third-party integrations"),
        ("CRM, AI &amp; Cloud", "Vtiger CRM integration/customization, Zoho CRM customization and workflow automation, AI-powered request classification and knowledge-base chatbot integration, AWS Lightsail, deployment and DevOps"),
    ]:
        story.append(Paragraph(f"<b>{label}:</b> {value}", st["skill"]))
    story += section("Professional Experience", st)
    story.append(KeepTogether([
        role_header("Android & CRM Developer - Arabia Holding", "Feb 2025 - Present", st),
        bullet("Built and deployed a connected suite of Android applications on a shared Ktor backend integrated with Vtiger CRM.", st),
        bullet("Developed AI-powered request classification and a knowledge-base chatbot that guides residents and can submit CRM tickets.", st),
        bullet("Built resident, sales, and operations workflows including real-time unit availability, lead capture, ticketing, payment-plan viewing, approval/rejection flows, and NPV-based payment proposals.", st),
        bullet("Implemented QR visitor access, gate validation, real-time notifications, community features, and support workflows.", st),
        bullet("Integrated the platform with Vtiger CRM and managed deployment and infrastructure on AWS Lightsail.", st), Spacer(1,2)]))
    story.append(KeepTogether([
        role_header("Android & CRM Developer - El-Shark Textile", "Jun 2024 - Jan 2025", st),
        bullet("Customized Zoho CRM to streamline sales and customer-service workflows and automate key business processes.", st),
        bullet("Developed Android applications for real-time communication between sales and customer-service teams; integrated Firebase for live data, push notifications, and messaging.", st)]))
    story += section("Education & Projects", st)
    story.append(Paragraph("<b>B.Sc. in Computer Science</b> - Mansoura University | 2018-2022 | Grade: Good. <b>Graduation Project:</b> BabyCare App (Excellent).", st["small"]))
    story.append(Paragraph("<b>Weathering With You - Personal Android Project:</b> Weather app using device location services, REST APIs, dynamic visuals, and city search; built with Clean Architecture, Dagger Hilt, and Navigation Compose.", st["small"]))
    story += section("Languages", st)
    story.append(Paragraph("Arabic: Native &nbsp;|&nbsp; English: Very Good", st["small"]))
    def page(canvas, d):
        canvas.saveState()
        canvas.setFillColor(BLUE)
        canvas.rect(d.leftMargin, A4[1]-7*mm, A4[0]-d.leftMargin-d.rightMargin, 1.4, stroke=0, fill=1)
        canvas.restoreState()
    doc.build(story, onFirstPage=page, onLaterPages=page)

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--output", type=Path, default=Path(__file__).resolve().parents[1] / "Mahmoud_Farid_CV.pdf")
    build(p.parse_args().output)
