use poly_professors;

SET FOREIGN_KEY_CHECKS = 0;

DROP TABLE IF EXISTS professors;
DROP TABLE IF EXISTS courses;
DROP TABLE IF EXISTS reviews;

CREATE TABLE professors (
    id INT NOT NULL AUTO_INCREMENT,
    firstName VARCHAR(255) NOT NULL,
    lastName VARCHAR(255) NOT NULL,
    department VARCHAR(40) NOT NULL,
    rating DECIMAL(3, 2),
    PRIMARY KEY (id)
);

CREATE TABLE courses (
    courseDepartment VARCHAR(8) NOT NULL,
    courseNumber VARCHAR(8) NOT NULL,
    PRIMARY KEY (courseDepartment, courseNumber)
) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin;

CREATE TABLE reviews (
    id INT NOT NULL AUTO_INCREMENT,
    courseDepartment VARCHAR(8) NOT NULL,
    courseNumber VARCHAR(8) NOT NULL,
    professorId INT NOT NULL,
    studentYear INT(1) NOT NULL,
    courseRequirement INT(1) NOT NULL,
    studentGrade VARCHAR(16),
    dateTaken DATE NOT NULL,
    rating DECIMAL(3, 2),
    review VARCHAR(10000),
    numEvalutions INT DEFAULT 0,
    PRIMARY KEY (id),
    CONSTRAINT courseId_fk FOREIGN KEY (courseDepartment, courseNumber) REFERENCES courses(courseDepartment, courseNumber),
    CONSTRAINT professorId_fk FOREIGN KEY (professorId) REFERENCES professors(id)
) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin;

SET FOREIGN_KEY_CHECKS = 1;
