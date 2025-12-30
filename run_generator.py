# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel

import argparse
from generator.core import generate_migration_file

def main():
    parser = argparse.ArgumentParser(description="Generate SQL migration file.")
    parser.add_argument("description", help="Short description of the migration (e.g. 'create users table')")
    
    args = parser.parse_args()
    
    try:
        filepath = generate_migration_file(args.description)
        print(f"Created migration file: {filepath}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel
