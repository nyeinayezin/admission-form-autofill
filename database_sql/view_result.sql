SELECT
    s.id AS student_id,
    s.first_name AS student_first_name,
    s.last_name AS student_last_name,
    s.date_of_birth,
    s.gender,

    g.id AS guardian_id,
    g.first_name AS guardian_first_name,
    g.last_name AS guardian_last_name,
    g.phone AS guardian_phone,
    g.email AS guardian_email,
    g.address AS guardian_address,

    sg.relationship,
    sg.is_primary_contact

FROM students s

JOIN students_guardians sg
    ON s.id = sg.student_id

JOIN guardians g
    ON sg.guardian_id = g.id

ORDER BY s.id, g.id;