import os
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet

def generate_report(train_number):
    doc = SimpleDocTemplate("output/Final_Report.pdf", pagesize=A4)
    styles = getSampleStyleSheet()
    story = []

    # Summary
    story.append(Paragraph(f"Train {train_number} – Summary Report", styles["Title"]))
    story.append(Spacer(1, 20))

    # Add coach images
    detections = "output/detections"
    for folder in sorted(os.listdir(detections)):
        folder_path = os.path.join(detections, folder)
        if not os.path.isdir(folder_path): continue
        story.append(Paragraph(f"Coach {folder}", styles["Heading2"]))
        for img_file in os.listdir(folder_path)[:3]:  # only 3 images per coach
            story.append(Image(os.path.join(folder_path, img_file), width=200, height=150))
        story.append(Spacer(1, 15))

    doc.build(story)
    print("✅ Final_Report.pdf generated")
