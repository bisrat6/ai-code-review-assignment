from typing import List, Any
import re

def count_valid_emails(emails: List[Any]) -> int:

    if not isinstance(emails, list):
        return 0

    count = 0

    # Regex pattern for a valid local part: letters, numbers, dots, underscores, plus, hyphen
    local_part_pattern = re.compile(r'^[A-Za-z0-9._+-]+$')

    for email in emails:
        # Skip non-string entries
        if not isinstance(email, str):
            continue

        # Remove leading/trailing spaces
        email = email.strip()

        # Must contain exactly one '@' and at least one '.' in the domain
        if email.count("@") != 1:
            continue

        local_part, domain_part = email.split("@")

        # Local and domain parts must be non-empty
        if not local_part or not domain_part:
            continue

        # Local part validation
        if not local_part_pattern.match(local_part):
            continue

        # Domain must contain a dot, cannot start or end with a dot, and no consecutive dots
        if (
            "." in domain_part
            and not domain_part.startswith(".")
            and not domain_part.endswith(".")
            and ".." not in domain_part
        ):
            count += 1

    return count
