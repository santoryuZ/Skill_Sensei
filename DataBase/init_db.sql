CREATE TABLE skills (
    skill_id SERIAL PRIMARY KEY,
    skill_name VARCHAR(100),
    proficiency_level VARCHAR(50),
    target_level VARCHAR(50),
    start_date DATE,
    target_date DATE
);

CREATE TABLE resources (
    resource_id SERIAL PRIMARY KEY,
    resource_name VARCHAR(100),
    resource_type VARCHAR(50),
    resource_link TEXT,
    skill_id INTEGER REFERENCES skills(skill_id) ON DELETE CASCADE
);
