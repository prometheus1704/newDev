def information_triage_system():
    print("=== Information Management Expert System ===")
    print("Welcome to the Information Triage Assistant\n")

    title = input("Enter Title or Subject of the Information: ")
    info_type = input("Type (Email/Document/Report/Message): ").lower()

    print("\nAnswer the following questions (Y/N):")

    urgency = input("Is this time-sensitive or urgent? ").lower() == 'y'
    sensitivity = input("Does it contain sensitive or confidential data? ").lower() == 'y'
    internal = input("Is it intended for internal use only? ").lower() == 'y'
    strategic = input("Is it related to strategy, planning, or decisions? ").lower() == 'y'
    legal = input("Is it related to legal matters or compliance? ").lower() == 'y'

    print("\nAnalyzing information...\n")

    # Decision logic based on responses
    if urgency and sensitivity:
        category = "Confidential & Urgent"
        action = "Send to Legal/Compliance Team immediately. Store in encrypted folder."
        priority = "High"
    elif urgency:
        category = "Urgent Only"
        action = "Forward to relevant department head. Review within 2 hours."
        priority = "High"
    elif sensitivity:
        category = "Sensitive"
        action = "Share with authorized personnel only. Use secure file transfer."
        priority = "Medium"
    elif strategic:
        category = "Strategic / Planning"
        action = "Distribute to management team. Schedule discussion."
        priority = "Medium"
    elif legal:
        category = "Legal / Compliance"
        action = "Notify Legal Department. Archive for audit trail."
        priority = "Medium"
    elif internal:
        category = "Internal Use"
        action = "Post in internal knowledge base. Notify team via email."
        priority = "Low"
    else:
        category = "General Information"
        action = "Store in public repository. No immediate action required."
        priority = "Low"

    # Output final decision
    print("=== Information Triage Report ===")
    print(f"Title: {title}")
    print(f"Type: {info_type.capitalize()}")
    print(f"Category: {category}")
    print(f"Priority: {priority}")
    print(f"Recommended Action: {action}")


# Run the system
if __name__ == "__main__":
    information_triage_system()
