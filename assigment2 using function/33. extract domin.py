def extract_domains(emails):
    return [email.split('@')[1] for email in emails]

emails = ["a@x.com", "b@y.org"]
result = extract_domains(emails)
print(result)