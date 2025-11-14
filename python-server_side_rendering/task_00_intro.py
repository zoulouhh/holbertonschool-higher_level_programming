#!/usr/bin/python3
"""Module for generating invitation files from a template."""


def generate_invitations(template, attendees):
    """
    Generate personalized invitation files from a template and list of attendees.

    Args:
        template (str): The template string
        attendees (list): List of dictionaries

    Returns:
        None
    """
    # Check input types
    if not isinstance(template, str):
        print("Error: Template must be a string")
        return

    if not isinstance(attendees, list):
        print("Error: Attendees must be a list")
        return

    # Check for empty inputs
    if not template.strip():
        print("Template is empty, no output files generated.")
        return

    if not attendees:
        print("No data provided, no output files generated.")
        return

    # Process each attendee
    for index, attendee in enumerate(attendees, 1):
        if not isinstance(attendee, dict):
            print(f"Error: Attendee {index} is not a dictionary")
            continue

        # Create a copy of the template
        invitation = template

        # Replace placeholders with values, using N/A for missing or None values
        for field in ['name', 'event_title', 'event_date', 'event_location']:
            value = attendee.get(field)
            value = "N/A" if value is None else str(value)
            placeholder = f"{{{field}}}"
            invitation = invitation.replace(placeholder, value)

        # Write to output file
        output_filename = f"output_{index}.txt"
        try:
            with open(output_filename, 'w') as f:
                f.write(invitation)
        except IOError as e:
            print(f"Error writing to file {output_filename}: {e}")