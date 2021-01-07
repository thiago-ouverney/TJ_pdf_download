


def send_email(adress_to, subject, body, path_attachment=""):
    outlook = win32.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)
    mail.To = adress_to
    mail.Subject = subject
    mail.Body = body
    # mail.HTMLBody = '<h2>HTML Message body</h2>' #this field is optional

    # To attach a file to the email (optional):
    if len(path_attachment) > 0:
        attachment = path_attachment
        mail.Attachments.Add(attachment)

    mail.Send()