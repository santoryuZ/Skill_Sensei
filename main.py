
from logic.skill_tracker import add_skill, list_skills, update_skill, delete_skill, search_skill, get_skill_id_by_name
from logic.resourse_tracker import  add_resource, list_resources, update_resource, delete_resource, search_resource

def skill_sensei_cli():
    while True:
        print("\n=== Skill Sensei CLI ===")
        print("1. Add Skill")
        print("2. List Skills")
        print("3. Update Skill")
        print("4. Delete Skill")
        print("5. Search Skill")
        print("6. Add Resource")
        print("7. List Resources")
        print("8. Update Resource")
        print("9. Delete Resource")
        print("10. Search Resource")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            skill_name = input("Enter skill name: ")
            proficiency_level = input("Enter current proficiency level: ")
            target_level = input("Enter target proficiency level: ")
            start_date = input("Enter start date (YYYY-MM-DD): ")
            target_date = input("Enter target date (YYYY-MM-DD): ")
            add_skill(skill_name, proficiency_level, target_level, start_date, target_date)

        elif choice == "2":
            list_skills()

        elif choice == "3":
            skill_id = input("Enter skill ID to update: ")
            field = input("Which field do you want to update? (skill_name, proficiency_level, target_level, start_date, target_date): ")
            new_value = input("Enter new value: ")
            update_skill(skill_id, field, new_value)

        elif choice == "4":
            skill_name = input("Enter skill name to delete: ")
            delete_skill(skill_name)

        elif choice == "5":
            skill_name = input("Enter skill name to search: ")
            search_skill(skill_name)


        elif choice == "6":
            resource_name = input("Enter resource name: ")
            resource_type = input("Enter resource type (e.g., Book, Video, Course): ")
            skill_name = input("Enter associated skill name: ")
            url = input("Enter resource URL: ")
            skill_id = get_skill_id_by_name(skill_name)

            if skill_id:
                add_resource(resource_name, resource_type, url, skill_id)

            else:
                print("Skill not found. Please add the skill first.")

        elif choice == "7":
            list_resources()

        elif choice == "8":
            resource_id = input("Enter resource ID to update: ")
            field = input("Which field do you want to update? (resource_name, resource_type, skill_name, url): ")
            new_value = input("Enter new value: ")
            update_resource(resource_id, field, new_value)

        elif choice == "9":
            resource_id = input("Enter resource ID to delete: ")
            delete_resource(resource_id)

        elif choice == "10":
            resource_id = input("Enter resource ID or name to search: ")
            search_resource(resource_id)

        elif choice == "0":
            print("Exiting Skill Sensei. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    skill_sensei_cli()

