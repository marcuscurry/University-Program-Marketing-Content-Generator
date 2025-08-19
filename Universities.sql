-- Create Major table
CREATE TABLE IF NOT EXISTS Major (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL UNIQUE
);

-- Create Institution table
CREATE TABLE IF NOT EXISTS Institution (
    id SERIAL PRIMARY KEY,
    university TEXT NOT NULL,
    program_name TEXT NOT NULL,
    url TEXT NOT NULL,
    major_id INTEGER NOT NULL REFERENCES Major(id)
);

INSERT INTO Major (name) VALUES
    ('Data Science'),
    ('Computer Science'),
    ('Business')
ON CONFLICT (name) DO NOTHING;


INSERT INTO Institution (university, program_name, url, major_id) VALUES
    ('University of Washington -- Seattle', 'MS in Data Science', 'https://www.washington.edu/datasciencemasters/', 1),
    ('University of Texas at Austin', 'MS in Data Science', 'https://cdso.utexas.edu/msds', 1),
    ('University of Chicago', 'MS in Data Science', 'https://codas.uchicago.edu/academics/ms-data-science/', 1);

INSERT INTO Institution (university, program_name, url, major_id) VALUES
    ('University of California -- Berkeley', 'MS in Computer Science', 'https://grad.berkeley.edu/program/computer-science/', 2),
    ('University of Texas at Austin', 'MS in Computer Science', 'https://cdso.utexas.edu/mscs', 2),
    ('Grand Canyon University', 'MS in Computer Science', 'https://www.gcu.edu/degree-programs/ms-computer-science', 2),
    ('University of Texas at San Antonio', 'MS in Computer Science', 'https://future.utsa.edu/programs/master/computer-science/', 2);

INSERT INTO Institution (university, program_name, url, major_id) VALUES
    ('University of Michigan -- Ann Arbor', 'MBA Program', 'https://michiganross.umich.edu/graduate/full-time-mba', 3),
    ('University of Florida', 'MBA Program', 'https://warrington.ufl.edu/mba/', 3),
    ('Indiana University -- Bloomington', 'MBA Program', 'https://kelley.iu.edu/programs/full-time-mba/index.cshtml', 3),
    ('University of North Carolina -- Chapel Hill', 'MBA Program', 'https://www.kenan-flagler.unc.edu/programs/mba/full-time-mba/', 3);
