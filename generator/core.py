# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel

import os
import re
from datetime import datetime

MIGRATIONS_DIR = "migrations"

def generate_migration_file(description):
    if not os.path.exists(MIGRATIONS_DIR):
        os.makedirs(MIGRATIONS_DIR)
        
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Sanitize description
    slug = re.sub(r'[^a-z0-9]+', '_', description.lower()).strip('_')
    
    filename = f"{timestamp}_{slug}.sql"
    filepath = os.path.join(MIGRATIONS_DIR, filename)
    
    template = f"""-- Migration: {description}
-- Created: {datetime.now()}

-- UP (Apply changes)
-- SQL statements here...

-- DOWN (Revert changes)
-- SQL statements here...
"""
    
    with open(filepath, "w") as f:
        f.write(template)
        
    return filepath

# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel
