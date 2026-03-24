#!/usr/bin/python3
"""Task 0: Simple templating program."""


def generate_invitations(template, attendees):
	"""Generate invitation files from a template and attendees list."""
	if not isinstance(template, str):
		print(
			"Invalid input: template is not a string "
			f"(got {type(template).__name__})."
		)
		return

	if not isinstance(attendees, list):
		print(
			"Invalid input: attendees is not a list "
			f"(got {type(attendees).__name__})."
		)
		return

	if not all(isinstance(attendee, dict) for attendee in attendees):
		print("Invalid input: attendees must be a list of dictionaries.")
		return

	if template == "":
		print("Template is empty, no output files generated.")
		return

	if len(attendees) == 0:
		print("No data provided, no output files generated.")
		return

	placeholders = ["name", "event_title", "event_date", "event_location"]

	for index, attendee in enumerate(attendees, start=1):
		content = template
		for placeholder in placeholders:
			value = attendee.get(placeholder)
			if value is None:
				value = "N/A"
			content = content.replace("{" + placeholder + "}", str(value))

		with open(f"output_{index}.txt", "w", encoding="utf-8") as file:
			file.write(content)
