SELECT
    s.id,
    s.first_name,
    s.last_name,
    s.date_of_birth,
    s.gender,
    g.id,
    g.first_name,
    g.last_name,
    g.phone,
    g.email,
    g.address,
    sg.relationship,
    sg.is_primary_contact

FROM students s

JOIN students_guardians sg
    ON s.id = sg.student_id

JOIN guardians g
    ON sg.guardian_id = g.id

WHERE s.id = ?

ORDER BY g.id;