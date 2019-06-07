from reportlab.pdfgen import canvas
from position import position
from name import name
from education import education
from address import address
from current_email import email
from phone_number import phone_number
from work_experience import work_experience
from projects import projects
from extracuricular_activities import activities
from extra_training import training
training = training.split('\n')
activities = activities.split('\n')
projects = projects.split('\n')
work_experience = work_experience.split('\n')
education = education.split('\n')
current_height = 841.89
inch = current_height / 11
c = canvas.Canvas('New_pdf.pdf')
c.setFont("Helvetica", 26)
current_height -= inch
c.drawString(inch, current_height, name)
current_height -= 26
c.setFont('Helvetica', 11)
c.drawString(inch, current_height, position)
current_height -= 11
current_height -= 22
c.drawString(1.5 * inch, current_height, address)
current_height -= 11
c.drawString(1.5 * inch, current_height, email)
current_height -= 11
c.drawString(1.5 * inch, current_height, phone_number)
current_height -= 11
current_height -= 22
c.setFont('Helvetica', 14)
c.drawString(inch, current_height, 'Education')
current_height -= 14
c.setFont('Helvetica', 11)
for i in range(len(education)):
  c.drawString(inch, current_height, education[i])
  current_height -= 11
current_height -= 11
c.setFont('Helvetica', 14)
c.drawString(inch, current_height, 'Work Experience')
current_height -= 14
c.setFont('Helvetica', 11)
for i in range(len(work_experience)):
  c.drawString(inch, current_height, work_experience[i])
  current_height -= 11
current_height -= 11
c.setFont('Helvetica', 14)
c.drawString(inch, current_height, "Projects")
current_height -= 14
c.setFont('Helvetica', 11)
for i in range(len(projects)):
  c.drawString(inch, current_height, projects[i])
  current_height -= 11
current_height -= 11
c.setFont('Helvetica', 14)
c.drawString(inch, current_height, "Extra Curicular Avtivities")
current_height -= 14
c.setFont('Helvetica', 11)
for i in range(len(activities)):
  c.drawString(inch, current_height, activities[i])
  current_height -= 11
current_height -= 11
if training[0] != 'None':
  c.setFont('Helvetica', 14)
  c.drawString(inch, current_height, 'Other Training')
  current_height -= 14
  c.setFont('Helvetica', 11)
  for i in range(len(training)):
    c.drawString(inch, current_height, training[i])
    current_height -= 11
c.save()
