start
    input name
    input age
    input grade
    input email
    input code

    if name is empty then
        print "------------------------------"
        print "REGISTRATION NOT ACCEPTED"
        print "------------------------------"
        print "Reason: Student name is required."
    else if age is not numeric then
        print "------------------------------"
        print "REGISTRATION NOT ACCEPTED"
        print "------------------------------"
        print "Reason: Age must be a number"
    else if age <= 11 or age >= 18 then
        print "------------------------------"
        print "REGISTRATION NOT ACCEPTED"
        print "------------------------------"
        print "Reason: Age must be from 11 to 18"
    else if grade is not in ["7", "8", "9", "10", "11", "12"] then
        print "------------------------------"
        print "REGISTRATION NOT ACCEPTED"
        print "------------------------------"
        print "Reason: Invalid level"
    else if "@" not in email or "." not in email then
        print "------------------------------"
        print "REGISTRATION NOT ACCEPTED"
        print "------------------------------"
        print "Reason: Invalid format"
    else if length(code) != 6 then
        print "------------------------------"
        print "REGISTRATION NOT ACCEPTED"
        print "------------------------------"
        print "Reason: Code should only have 6 characters"
    else
        print "------------------------------"
        print "REGISTRATION ACCEPTED"
        print "------------------------------"
        print "Student:", name
        print "Age:", age
        print "Grade Level:", grade
        print "Email:", email
        print "Registration Code:", code
    endif
end

